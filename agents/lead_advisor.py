import anthropic
import os
import re
from dotenv import load_dotenv
from agents.market_analyst import market_analyst
from agents.b3_agent import b3_agent

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extract_tickers(text: str) -> list:
    """Extrai tickers de acoes do texto."""
    pattern = r'\b[A-Z]{4}[0-9]{1,2}\b'
    return list(set(re.findall(pattern, text.upper())))

def lead_advisor(user_message: str, conversation_history: list) -> str:
    """Orquestrador principal da Quantum Finance."""
    
    tickers = extract_tickers(user_message)
    
    market_info = ""
    b3_info = ""
    
    keywords_market = ["cdb", "tesouro", "fii", "lci", "lca", "renda fixa", "fundo", "investimento"]
    keywords_b3 = tickers or ["acao", "acoes", "bolsa", "b3", "ticker"]
    
    needs_market = any(kw in user_message.lower() for kw in keywords_market)
    needs_b3 = bool(tickers) or any(kw in user_message.lower() for kw in ["acao", "acoes", "bolsa", "b3"])
    
    if needs_market:
        market_info = market_analyst(user_message)
    
    if needs_b3:
        b3_info = b3_agent(user_message, tickers)
    
    system_prompt = """Voce e o Lead Advisor da Quantum Finance, uma consultoria financeira premium brasileira.

Quando o usuario iniciar com saudacao, apresente-se com:
- Boas-vindas a Quantum Finance
- Pergunte: valor disponivel, objetivo, perfil (conservador/moderado/arrojado) e acoes de interesse

Apos receber o perfil, gere recomendacao com:
### Perfil do Cliente
### Analise de Mercado
### Dados da B3
### Recomendacao Personalizada
### Aviso Legal

Nossa equipe de especialistas ja analisou:
"""
    
    if market_info:
        system_prompt += f"\nANALISE DE MERCADO (Market Analyst):\n{market_info}\n"
    
    if b3_info:
        system_prompt += f"\nDADOS DA B3 (B3 Agent):\n{b3_info}\n"
    
    system_prompt += "\nConsolide as analises e gere uma recomendacao personalizada. NUNCA invente cotacoes."
    
    messages = conversation_history + [{"role": "user", "content": user_message}]
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=system_prompt,
        messages=messages
    )
    
    return response.content[0].text
