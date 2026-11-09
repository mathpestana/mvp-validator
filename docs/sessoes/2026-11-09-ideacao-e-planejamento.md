# Sessão 1 · Ideação e planejamento

**Data:** 2026-11-09 · **Ferramenta:** Claude (app desktop) · **Próxima sessão:** Claude Code, aberto na pasta do projeto

## Por que esta sessão termina aqui

Esta sessão serviu para transformar a ideia em plano: analisar o conceito, estudar o MiroFish, escrever o documento do projeto e criar a estrutura inicial do repositório. A próxima etapa é implementar, e ela continua numa sessão nova do Claude Code, por três motivos:

1. **Contexto limpo.** Esta conversa ficou longa e cheia de discussão que já virou decisão. Uma sessão nova começa só com o que importa, sem gastar contexto relendo o caminho até aqui.
2. **As instruções carregam sozinhas.** Aberto em `validador-mvp/`, o Claude Code lê o `CLAUDE.md`, que importa o `AGENTS.md`. Regras, comandos e fase atual entram automaticamente, sem precisar repetir nada.
3. **Este arquivo é a ponte.** O que foi decidido aqui e não está no código está resumido abaixo.

## O que foi feito

- **Ideia analisada:** pontos fortes, riscos e como os agentes usam o produto em 4 níveis de fidelidade (texto, telas, navegador e API).
- **MiroFish estudado:** aproveitamos as ideias de personas geradas a partir de dados reais, agente de relatório com ferramentas, entrevista depois da simulação e injeção de variáveis para comparar. Evitamos o foco em rede social, a falta de limites declarados e o código (licença AGPL-3.0).
- **Documento do projeto escrito:** [Validador de MVP — Documento do Projeto](https://claude.ai/artifact/DwrdKujynsooPqscNtsVLX) (link privado). Tem visão, princípios de validade, arquitetura, stack, modelo de dados com 17 tabelas, plano em 7 fases, KPIs por gate e riscos.
- **Repositório criado:** estrutura de pastas, README, `AGENTS.md`, `CLAUDE.md`, backend mínimo e docker-compose. Os 2 testes e o lint passam. Primeiro commit: `9d464cd` na `main`.

## Decisões tomadas

| Decisão | Escolha | Onde está registrada |
| --- | --- | --- |
| Posicionamento | Gerador de hipóteses e caçador de atrito, não validação de mercado | Documento, seção "Princípios e limites de validade" |
| Banco | Postgres relacional com JSONB e pgvector, desde a Sprint 0 | `docs/decisoes/0001-postgres-relacional.md` |
| Agentes | Sem framework; ciclo do agente escrito à mão | `docs/decisoes/0002-sem-framework-de-agentes.md` |
| Backend | Python 3.12 + FastAPI + uv | Documento, seção "Stack" |
| Interface | Streamlit nas fases 1 e 2, Next.js a partir da 3 | Documento, seção "Stack" |
| Gabarito | `app-exemplo/` com pelo menos 10 bugs plantados | `app-exemplo/` |
| Plano | 7 fases, 15 sprints de 2 semanas, gates com KPIs | Documento, seções "Plano de construção" e "KPIs" |
| MiroFish | Só ideias, nenhum código | Documento, seção "Por que existe" |

## Decisões em aberto

- [ ] Nome do produto ("Validador de MVP" é provisório)
- [ ] Ritmo: sprints de 1 ou de 2 semanas (há um comentário aberto sobre isso no documento)
- [ ] Público inicial: devs independentes ou estudantes e bootcamps
- [ ] Provedor de LLM e orçamento mensal de API
- [ ] Objetivo: projeto de aprendizado, portfólio ou produto comercial

## Estado atual

- **Fase 0 · Fundação.** Nenhum item do Gate 0 concluído ainda.
- **Existe:** rota `/health`, configuração via `.env`, contrato da camada de LLM, provedor falso e 2 testes.
- **Não testado:** o Postgres no Docker (`docker compose up -d db` ainda não foi rodado).
- **Não feito:** Alembic, modelos do banco, provedor real de LLM, registro de custo e o `app-exemplo`.
- **Git:** sem repositório remoto; nada foi enviado ao GitHub.

## Próximos passos (Sprint 0)

1. Subir o banco com `docker compose up -d db` e confirmar a conexão.
2. Configurar o Alembic e criar a primeira migração, com `CREATE EXTENSION IF NOT EXISTS vector` e as tabelas `projeto`, `bug_plantado` e `chamada_llm`.
3. Implementar o provedor da Anthropic em `backend/app/llm/`, gravando cada chamada em `chamada_llm`.
4. Construir o `app-exemplo` e plantar 10 bugs, catalogando cada um em `app-exemplo/BUGS.md`.
5. (Opcional) Criar o repositório no GitHub e enviar a `main`.

## Como começar a próxima sessão

No terminal:

```bash
cd C:\Users\mathe\projects\validador-mvp
claude
```

Primeira mensagem sugerida:

> Leia `docs/sessoes/2026-11-09-ideacao-e-planejamento.md`. Estamos na Sprint 0. Proponha um plano para os passos 1 e 2 (banco e Alembic) antes de escrever código.

## Lições desta sessão

- **Caminhos longos no Windows quebram dependências.** Com o projeto numa pasta muito funda, o caminho de um arquivo do pydantic passou de 260 caracteres e os testes falharam. Mover para `C:\Users\mathe\projects\validador-mvp` resolveu.
- **Documentar o porquê junto com o quê.** Cada decisão tem o seu motivo registrado (documento ou `docs/decisoes/`), para não ser rediscutida em toda sessão nova.
