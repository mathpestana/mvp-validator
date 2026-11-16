# Referência · nota-de-sessao

## Nome do arquivo

`docs/sessoes/AAAA-MM-DD-assunto-curto.md`, minúsculas, sem acento, palavras separadas por hífen. Exemplo: `2026-11-09-ideacao-e-planejamento.md`. Duas sessões no mesmo dia: acrescente o assunto de cada uma.

## Modelo

```markdown
# Sessão N · Título curto

**Data:** AAAA-MM-DD · **Ferramenta:** Claude Code · **Próxima sessão:** onde e como continua

## O que foi feito

- Itens curtos, cada um com o resultado (o que existe agora).

## Decisões tomadas

| Decisão | Escolha | Onde está registrada |
| --- | --- | --- |

## Decisões em aberto

- [ ] Pergunta ainda sem resposta

## Estado atual

- **Fase:** qual, e quais itens do Gate 0 estão concluídos.
- **Existe:** o que funciona e foi verificado.
- **Não testado:** o que foi escrito mas não rodou.
- **Não feito:** o que falta da sprint.
- **Git:** último commit e se há remoto.

## Próximos passos

1. Lista ordenada, o primeiro item sendo o que a próxima sessão faz ao abrir.

## Como começar a próxima sessão

Primeira mensagem sugerida, pronta para colar.

## Lições desta sessão

- Só o que surpreendeu e vale lembrar. Apague a seção se não houver nenhuma.
```

## O que entra em cada seção

- **O que foi feito:** resultados, não esforço. "Alembic configurado, migração 0001 aplicada" e não "mexi no Alembic".
- **Decisões tomadas:** só decisões que não estão óbvias no código. Se for grande, o certo é um ADR em `docs/decisoes/` e a nota apenas aponta para ele.
- **Estado atual:** a seção mais importante. Separar "existe", "não testado" e "não feito" evita a próxima sessão assumir que algo funciona sem prova.
- **Próximos passos:** acionáveis. Cada um deve caber numa instrução ao Claude.
- **Lições:** erros e surpresas reais (ex.: caminho longo no Windows quebrando dependência), não generalidades.

## Erros comuns

- Escrever "tudo funcionando" sem ter rodado `uv run pytest` e `uv run ruff check .`. Registre o resultado real.
- Repetir o `AGENTS.md` ou o diff do git. A nota guarda só o que não está lá.
- Deixar de levar adiante as decisões em aberto da nota anterior.
- Esquecer de dizer se o gate avançou e se o item foi marcado no `AGENTS.md`.

## Checklist final

- [ ] Nome do arquivo no padrão, sem sobrescrever nota existente
- [ ] "Estado atual" separa existe, não testado e não feito
- [ ] Resultado de pytest e ruff citado, ou dito que não rodaram
- [ ] Decisões em aberto herdadas da nota anterior
- [ ] Primeiro próximo passo é claro o bastante para abrir a sessão seguinte
