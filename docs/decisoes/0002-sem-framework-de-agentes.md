# 0002 · Sem framework de agentes

**Status:** aceita · 2026-11-09

## Contexto

Frameworks como LangChain e CrewAI aceleram o começo, mas escondem o ciclo do agente (observar → decidir → agir → registrar). Esse ciclo é o coração do produto, precisa de limites rígidos de passos, tempo e custo, e entendê-lo por dentro é um dos objetivos de aprendizado do projeto.

## Decisão

Chamar os SDKs dos provedores direto, através da camada própria em `backend/app/llm/`, e escrever o ciclo do agente à mão.

## Consequências

- Controle total sobre prompts, limites, registro de custo e formato dos eventos.
- Mais código para escrever no início (ferramentas, laço do agente, novas tentativas).
- Reavaliar se algum framework passar a poupar trabalho de verdade; a mudança exigiria uma nova decisão registrada aqui.
