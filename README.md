# Validador de MVP

> **Status:** Fase 0 (fundação). Ainda não há nada funcionando; esta é a estrutura inicial do projeto.

## Em poucas palavras

Quem cria um aplicativo ou site novo raramente tem tempo ou dinheiro para chamar pessoas de verdade para testar antes de lançar, e acaba descobrindo os problemas só depois, quando os clientes já desistiram. O Validador de MVP cria um grupo de "usuários de mentira" com jeitos bem diferentes, como uma senhora com pouca paciência para tecnologia ou um estudante com um celular simples e internet fraca, e coloca esse grupo para usar o seu produto. Em poucos minutos, você recebe uma lista do que travou, do que confundiu e de quanto essas pessoas aceitariam pagar. Isso não substitui conversar com clientes reais, mas mostra os erros mais óbvios antes que eles custem caro. Assim, você chega aos primeiros clientes de verdade com um produto melhor e sabendo exatamente o que perguntar.

## Como funciona

1. **Painel:** você monta um grupo de personas com perfis diferentes (idade, região, renda, aparelho, familiaridade com tecnologia).
2. **Teste:** as personas usam o seu produto, lendo a página, olhando as telas ou navegando nele de verdade.
3. **Relatório:** você recebe defeitos, pontos de confusão e opiniões, separados por tipo de pessoa.
4. **Entrevista:** você pode conversar com qualquer persona para entender por que ela desistiu.
5. **Comparação:** muda algo (preço, tela, texto), roda de novo e vê se melhorou.

## Estrutura do projeto

```text
.
├── AGENTS.md              instruções para agentes de IA (Claude Code, Codex, Cursor...)
├── CLAUDE.md              instruções específicas do Claude Code (importa o AGENTS.md)
├── README.md
├── docker-compose.yml     Postgres + pgvector para desenvolvimento
├── .env.example           variáveis de ambiente (copie para .env)
├── backend/               API em Python (FastAPI)
│   ├── app/
│   │   ├── api/           rotas
│   │   ├── personas/      fábrica de personas e métricas de diversidade
│   │   ├── execucao/      orquestrador e executores (conceito, visual, navegador, API)
│   │   ├── analise/       agente de relatório, entrevista e preço
│   │   ├── llm/           único ponto de contato com os modelos de IA
│   │   └── db/            modelos do banco e migrações
│   └── tests/
├── frontend/              Streamlit nas fases 1 e 2, Next.js a partir da 3
├── app-exemplo/           app com bugs plantados de propósito (o gabarito)
├── mcp/                   servidor MCP (fase 5)
└── docs/
    └── decisoes/          registro das decisões de arquitetura
```

## Rodando localmente

Pré-requisitos: [Docker](https://www.docker.com/), Python 3.12+ e [uv](https://docs.astral.sh/uv/).

> **Windows:** deixe o projeto numa pasta de caminho curto (ex.: `C:\dev\validador-mvp`). Caminhos com mais de 260 caracteres quebram a instalação de algumas dependências.

```bash
cp .env.example .env
```

```bash
docker compose up -d db
```

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

A API sobe em http://localhost:8000 e a rota `/health` responde `{"status": "ok"}`.

Testes e lint, dentro de `backend/`:

```bash
uv run pytest
```

```bash
uv run ruff check .
```

## Plano de construção

Cada fase só começa quando o gate da anterior passa.

| Fase | O que entrega | Gate para avançar |
| --- | --- | --- |
| 0 · Fundação | Repositório, camada de LLM, banco, registro de custo, app de exemplo | ≥ 10 bugs catalogados · 100% das chamadas com custo registrado |
| 1 · Personas e conceito | Personas a partir de dados reais, teste de landing page | Personas mais diversas que sem perfil · landing ruim perde em ≥ 80% |
| 2 · Agente navegador | Uma persona usa o app de verdade pelo Playwright | ≥ 80% das tarefas concluídas · ≥ 50% dos bugs plantados achados |
| 3 · Painel e dashboard | Várias personas em paralelo, relatórios, entrevista | ≥ 70% dos bugs · 10 personas em ≤ 15 min e ≤ US$ 5 |
| 4 · Experimentos e preço | Versões, comparação A/B, módulo de preço, memória | A/B certo em ≥ 9 de 10 rodadas |
| 5 · MCP e API | Agentes de código chamam o simulador | Agente roda teste e lê relatório sozinho em 3 de 3 |
| 6 · Calibração e beta | Comparação com 5 usuários reais, primeiros usuários beta | ≥ 60% dos problemas reais aparecem na simulação |

O documento completo do projeto (visão, arquitetura, modelo de dados, KPIs e riscos) está em [Validador de MVP — Documento do Projeto](https://claude.ai/artifact/DwrdKujynsooPqscNtsVLX) (link privado).

## Limites

Os resultados vêm de personas simuladas por IA. Eles servem para encontrar problemas cedo e gerar hipóteses, não para provar que um produto vai dar certo. Defeitos e fluxos quebrados são confiáveis; opiniões e números como "quantos comprariam" devem ser confirmados com pessoas reais.
