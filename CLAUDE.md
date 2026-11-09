@AGENTS.md

## Específico do Claude Code

- Antes de uma mudança que toque mais de um módulo, proponha um plano curto e espere confirmação.
- O documento do projeto (link no AGENTS.md) define escopo, fases e KPIs. Se o pedido ou o código divergir dele, pergunte antes de seguir.
- Rode `uv run pytest` e `uv run ruff check .` dentro de `backend/` antes de dizer que terminou, e diga o resultado.
- Ao concluir um item do gate da fase atual, marque-o na seção "Fase atual" do AGENTS.md.
