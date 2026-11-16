---
name: nota-de-sessao
description: Escreve a nota de encerramento de uma sessão de trabalho em docs/sessoes/, no formato das notas anteriores do Validador de MVP. Use quando o usuário pedir para encerrar a sessão, registrar o que foi feito, escrever a nota da sessão ou deixar o próximo passo anotado. Também use ao final de uma sessão com trabalho relevante, como o CLAUDE.md exige.
allowed-tools: Read Glob Grep Write Bash(git log:*) Bash(git status:*)
---

# nota-de-sessao

A nota é a ponte entre sessões: a próxima começa lendo-a para saber onde esta parou. Ela registra o que foi feito, o que foi decidido e o que vem a seguir, sem repetir o que o código ou o git já mostram.

## Passos

1. Liste `docs/sessoes/` e leia a nota mais recente, para herdar as decisões em aberto e os próximos passos.
2. Veja o que mudou: `git log` desde a nota anterior e `git status`. Use também o que foi dito na conversa.
3. Leia a seção "Fase atual" do `AGENTS.md` e confira quais itens do Gate 0 estão marcados.
4. Escreva a nota nova em `docs/sessoes/AAAA-MM-DD-assunto-curto.md`, seguindo o modelo de [reference.md](reference.md).
5. Mostre ao usuário o caminho do arquivo e um resumo de duas linhas.

## Regras

- Só conte como feito o que foi verificado. Se um teste não rodou ou algo não foi testado, diga isso em "Estado atual".
- Cada decisão leva o seu motivo ou aponta para onde está registrada (ADR em `docs/decisoes/`, documento do projeto).
- Decisões em aberto da nota anterior que continuam abertas são copiadas; as resolvidas saem ou vão para "Decisões tomadas".
- Não edite notas antigas: cada sessão ganha um arquivo novo.
- Não commite sem o usuário pedir.

Modelo completo, o que entra em cada seção e erros comuns estão em [reference.md](reference.md).
