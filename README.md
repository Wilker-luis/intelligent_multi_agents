# Quantum Finance - Sistema Multiagente de Consultoria Financeira

## Sobre o Projeto

Sistema de IA Agêntica desenvolvido como trabalho final da disciplina **Intelligent Multi Agents** do MBA em Data Science & AI da FIAP.

O Quantum Finance é um consultor financeiro inteligente baseado em múltiplos agentes de IA que colaboram para gerar recomendações personalizadas de investimento para o mercado brasileiro.

## Arquitetura Multiagente

O sistema é composto por 3 agentes especializados:

| Agente | Responsabilidade |
|--------|-----------------|
| **Lead Advisor** | Orquestrador principal. Coleta o perfil do cliente, coordena os demais agentes e gera a recomendação final consolidada |
| **Market Analyst** | Especialista em produtos financeiros brasileiros: CDB, Tesouro Direto, FIIs, LCI, LCA |
| **B3 Agent** | Especialista em acoes da B3. Busca cotacoes reais via brapi.dev e analisa fundamentos |

## Tecnologias Utilizadas

- **Python 3.11**
- **Claude Sonnet (Anthropic API)** - Modelo de IA para cada agente
- **Flask** - Servidor web e API REST
- **brapi.dev** - API gratuita para cotacoes reais da B3
- **HTML/CSS/JavaScript** - Interface web do chat

## Estrutura do Projeto
intelligent_multi_agents/
├── agents/
│   ├── lead_advisor.py      # Agente orquestrador
│   ├── market_analyst.py    # Agente de produtos financeiros
│   └── b3_agent.py          # Agente de acoes da B3
├── templates/
│   └── index.html           # Interface web do chat
├── app.py                   # Servidor Flask
├── .env.example             # Exemplo de variaveis de ambiente
├── .gitignore
└── README.md## Como Executar

### Pre-requisitos

- Python 3.11+
- Conta na [Anthropic](https://console.anthropic.com) com creditos

### Instalacao

1. Clone o repositorio:
`ash
git clone https://github.com/seu-usuario/quantum-finance.git
cd quantum-finance
`

2. Instale as dependencias:
`ash
pip install anthropic httpx python-dotenv flask
`

3. Configure as variaveis de ambiente:
`ash
cp .env.example .env
`
Edite o arquivo .env com sua chave da Anthropic.

4. Execute o servidor:
`ash
python app.py
`

5. Acesse no navegador: http://localhost:5000

## Variaveis de Ambiente

Crie um arquivo .env com:ANTHROPIC_API_KEY=sua_chave_aqui
BOLSAI_API_KEY=opcional## Funcionalidades

- Coleta de perfil do investidor (valor, objetivo, perfil de risco)
- Analise de produtos de renda fixa (CDB, Tesouro Direto, LCI, LCA, FIIs)
- Cotacoes reais de acoes da B3 via brapi.dev
- Recomendacao personalizada com alocacao de carteira
- Interface web com chat em tempo real
- Aviso legal em todas as respostas

## Exemplo de Uso

Digite no chat:Sou investidor moderado, tenho R$ 80.000 e quero analisar PETR4, VALE3 e ITUB4, alem de Tesouro Direto e FIIs.O sistema acionara os 3 agentes e retornara uma analise completa com cotacoes reais e recomendacao personalizada.


## Demo

[![Quantum Finance Demo](https://img.youtube.com/vi/1ghM6pEmrQc/0.jpg)](https://youtu.be/1ghM6pEmrQc)

> Clique na imagem para assistir a demonstracao completa do sistema.
## Autor

Desenvolvido para o MBA Data Science & AI - FIAP  
Disciplina: Intelligent Multi Agents  
Professor: Alexandre Alves

## Licenca

Este projeto foi desenvolvido com base na estrutura do [google/adk-samples](https://github.com/google/adk-samples), licenca Apache 2.0.
