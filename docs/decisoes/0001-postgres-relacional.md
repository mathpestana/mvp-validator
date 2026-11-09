# 0001 · Postgres relacional desde a Sprint 0

**Status:** aceita · 2026-11-09

## Contexto

Os dados formam uma cadeia de relações (projeto → versão → experimento → execução → evento → achado), e quase todo KPI depende de juntar e agregar essa cadeia. Alguns campos variam muito (perfil da persona, variáveis do experimento), e a Fase 1 já precisa de embeddings para medir a diversidade das respostas.

## Decisão

Usar Postgres com a extensão pgvector, rodando em Docker desde a Sprint 0. Campos flexíveis ficam em JSONB. Embeddings ficam no mesmo banco.

## Consequências

- Integridade garantida por chaves estrangeiras; KPIs e comparações A/B saem de SQL simples.
- Não há migração de SQLite para Postgres depois.
- As execuções em paralelo da Fase 3 não esbarram em travas de escrita.
- Exige Docker para desenvolver.
- A primeira migração precisa rodar `CREATE EXTENSION IF NOT EXISTS vector`.
