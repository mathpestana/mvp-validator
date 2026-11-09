# AGENTS.md

Instruções para agentes de IA (Claude Code, Codex, Cursor e similares) que trabalham neste repositório. Leia este arquivo inteiro antes de mudar qualquer coisa.

## O projeto

O Validador de MVP coloca personas de IA com perfis diferentes para usar o MVP de alguém. Elas reportam defeitos, pontos de atrito e reação a preço, e os resultados ficam num histórico que permite comparar versões. O documento completo (visão, arquitetura, modelo de dados, KPIs e riscos) é a fonte de verdade de escopo: https://claude.ai/artifact/DwrdKujynsooPqscNtsVLX

## Fase atual

**Fase 0 · Fundação.** Para sair dela (Gate 0):

- [ ] `app-exemplo/` com pelo menos 10 bugs plantados e catalogados em `app-exemplo/BUGS.md`
- [ ] 100% das chamadas de LLM com custo registrado na tabela `chamada_llm`
- [ ] Postgres + pgvector rodando via `docker compose`, com o esquema inicial migrado pelo Alembic

Não construa funcionalidades de fases futuras sem pedido explícito. Quando um item do gate for concluído, marque-o aqui.

## Comandos

Todos os comandos Python rodam dentro de `backend/`.

| Para | Comando |
| --- | --- |
| Subir o banco | `docker compose up -d db` (na raiz) |
| Instalar dependências | `uv sync` |
| Rodar a API | `uv run uvicorn app.main:app --reload` |
| Rodar os testes | `uv run pytest` |
| Lint | `uv run ruff check . --fix` |
| Formatar | `uv run ruff format .` |
| Criar migração | `uv run alembic revision --autogenerate -m "descricao"` |
| Aplicar migrações | `uv run alembic upgrade head` |

O Alembic ainda não foi inicializado; isso faz parte da Sprint 0.

## Mapa do repositório

| Pasta | Responsabilidade | Entra na fase |
| --- | --- | --- |
| `backend/app/llm/` | Único ponto de contato com provedores de LLM; registra custo de cada chamada | 0 |
| `backend/app/db/` | Modelos SQLAlchemy e migrações Alembic | 0 |
| `backend/app/api/` | Rotas FastAPI | 0 |
| `backend/app/personas/` | Fábrica de personas e métricas de diversidade | 1 |
| `backend/app/execucao/` | Orquestrador e executores (conceito, visual, navegador, API) | 1 e 2 |
| `backend/app/analise/` | Agente de relatório, entrevista e módulo de preço | 1, 3 e 4 |
| `frontend/` | Streamlit nas fases 1 e 2; Next.js a partir da 3 | 1 |
| `app-exemplo/` | App com bugs plantados de propósito: o gabarito dos testes | 0 |
| `mcp/` | Servidor MCP | 5 |
| `docs/decisoes/` | Registro de decisões de arquitetura (ADRs) | sempre |

## Regras que não se negociam

1. **Toda chamada de LLM passa por `backend/app/llm/`.** Nenhum outro módulo importa o SDK de um provedor. É essa camada que grava modelo, tokens, custo e latência em `chamada_llm`.
2. **Não corrija os bugs de `app-exemplo/`.** Eles existem de propósito e servem de gabarito para medir os agentes. Leia `app-exemplo/AGENTS.md` antes de mexer lá.
3. **Números saem do banco, nunca do LLM.** Taxas, contagens e médias de relatório são calculadas em SQL ou Python. O LLM só interpreta e escreve o texto.
4. **O esquema só muda por migração Alembic.** Nunca altere o banco à mão.
5. **Só dados de teste.** As credenciais das personas são contas de teste, guardadas cifradas com `CHAVE_CIFRA_CREDENCIAIS`. O agente navegador só acessa URLs cadastradas no projeto pelo usuário.
6. **Segredos fora do código.** Chaves só no `.env`, que nunca é commitado. Ao criar uma variável nova, adicione-a ao `.env.example`.
7. **Sem framework de agentes** (LangChain, CrewAI e similares). O ciclo do agente é escrito à mão, de propósito. Veja `docs/decisoes/0002-sem-framework-de-agentes.md`. Toda dependência nova precisa de justificativa.
8. **Toda execução tem limite** de passos (`LIMITE_PASSOS_EXECUCAO`), de tempo e de custo. Nenhum loop de agente roda sem teto.

## Regras de validade das personas

- **Demografia vira comportamento.** Idade, gênero, raça e classe são traduzidos em fatores concretos: aparelho, conexão, renda disponível, letramento digital, tempo livre e contexto de uso. Nunca descreva uma persona por estereótipo.
- **Toda persona é reprodutível:** guarda `fonte_id` (de onde vieram os dados) e `semente`.
- **Todo painel tem personas céticas e impacientes,** e os prompts pedem crítica concreta, não elogio.
- **Todo achado tem nível de confiança.** Relatórios nunca mostram número absoluto ("% que compraria", "preço ideal") sem aviso.

## Convenções de código

- Python 3.12, type hints em tudo, `async` nas rotas e em todo I/O.
- Saídas estruturadas de LLM são sempre validadas com modelos Pydantic.
- SQLAlchemy 2 no estilo `Mapped[...]`, com UUID como chave primária.
- Termos de domínio em português, sem acento e iguais aos nomes das tabelas: `persona`, `painel`, `experimento`, `execucao`, `evento`, `achado`. Comentários e docstrings em português.
- Prompts ficam em arquivos próprios (`prompts/*.md` dentro do módulo que os usa), nunca como strings longas no meio do código.
- Prefira funções pequenas e código simples a abstrações antecipadas.

## Testes

- Todo módulo novo vem com testes em `backend/tests/`.
- Testes nunca chamam um LLM de verdade: use `app.llm.falso.ProvedorFalso`.
- Testes do agente navegador rodam contra o `app-exemplo/`, nunca contra sites externos.

## Pronto quer dizer

- [ ] `uv run pytest` passa
- [ ] `uv run ruff check .` sem erros
- [ ] Migração criada, se o esquema mudou
- [ ] `.env.example`, `README.md` ou este arquivo atualizados, se algo mudou para quem chega ao projeto
