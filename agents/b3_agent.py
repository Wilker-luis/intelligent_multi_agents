import anthropic
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def get_stock_data(ticker: str) -> dict:
    """Busca dados reais da B3 via brapi.dev."""
    try:
        url = f"https://brapi.dev/api/quote/{ticker.upper()}"
        with httpx.Client(timeout=10.0) as http:
            response = http.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get("results"):
                    r = data["results"][0]
                    return {
                        "ticker": r.get("symbol"),
                        "nome": r.get("longName"),
                        "preco_atual": r.get("regularMarketPrice"),
                        "variacao_dia": r.get("regularMarketChangePercent"),
                        "abertura": r.get("regularMarketOpen"),
                        "maxima": r.get("regularMarketDayHigh"),
                        "minima": r.get("regularMarketDayLow"),
                        "volume": r.get("regularMarketVolume"),
                        "mercado": r.get("marketCap"),
                        "fonte": "brapi.dev / B3"
                    }
            return {"error": f"Ticker {ticker} nao encontrado"}
    except Exception as e:
        return {"error": str(e)}

def b3_agent(query: str, tickers: list = []) -> str:
    """Especialista em acoes da B3."""
    
    stock_data = ""
    for ticker in tickers:
        data = get_stock_data(ticker)
        if "error" not in data:
            stock_data += f"""
{data['ticker']} - {data['nome']}:
- Preco atual: R$ {data['preco_atual']}
- Variacao hoje: {data['variacao_dia']:.2f}%
- Abertura: R$ {data['abertura']}
- Maxima do dia: R$ {data['maxima']}
- Minima do dia: R$ {data['minima']}
- Volume: {data['volume']:,}
- Fonte: {data['fonte']}
"""
        else:
            stock_data += f"\n{ticker}: dados nao disponiveis no momento"
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""Voce e um especialista em acoes da B3 brasileira.
Use APENAS os dados reais fornecidos abaixo para sua analise.
NUNCA invente cotacoes ou dados financeiros.
Dados reais da B3:""" + (stock_data if stock_data else " Nenhum ticker informado."),
        messages=[{"role": "user", "content": query}]
    )
    
    return message.content[0].text