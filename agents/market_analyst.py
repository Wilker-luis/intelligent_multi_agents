import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def market_analyst(query: str) -> str:
    """Especialista em produtos financeiros brasileiros."""
    
    knowledge_base = {
        "cdb": "CDB (Certificado de Deposito Bancario): Renda fixa emitida por bancos. Rendimento indexado ao CDI. Garantido pelo FGC ate R$ 250.000. IR regressivo de 22,5% a 15%.",
        "tesouro": "Tesouro Direto: Titulos publicos federais. Tipos: Selic (liquidez diaria), IPCA+ (protecao inflacao), Prefixado (taxa fixa). Garantido pelo governo federal.",
        "fii": "FIIs (Fundos Imobiliarios): Negociados na B3. Rendimentos mensais isentos de IR para PF. Diversificacao em imoveis sem comprar fisicamente.",
        "lci": "LCI (Letra de Credito Imobiliario): Renda fixa isenta de IR para PF. Garantida pelo FGC ate R$ 250.000.",
        "lca": "LCA (Letra de Credito do Agronegocio): Similar a LCI, isenta de IR. Recursos para agronegocio.",
        "acoes": "Acoes: Participacao em empresas. Renda variavel. Ganho de capital tributado a 15%. Dividendos isentos de IR.",
    }
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""Voce e um especialista em produtos financeiros brasileiros.
Use as informacoes da base de conhecimento abaixo para responder:

""" + "\n".join(knowledge_base.values()) + """

Seja claro, didatico e objetivo. Nao invente informacoes.""",
        messages=[{"role": "user", "content": query}]
    )
    
    return message.content[0].text
