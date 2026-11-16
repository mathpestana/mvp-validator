# Referência · plantar-bug

## Formato da linha no BUGS.md

| Coluna | O que escrever |
| --- | --- |
| ID | `BUG-01`, `BUG-02`... sequencial. Acidentais: `BUG-xx (acidental)` |
| Tipo | `quebrado`, `ux` ou `acessibilidade` |
| Descrição | O sintoma como a persona vê, sem revelar a causa no código |
| Onde | Tela ou rota, mais arquivo e linha (`cadastro.py:42`) |
| Como reproduzir | Passos numerados curtos, com os dados exatos (ex.: e-mail `Ana@exemplo.com`) |
| Severidade | `alta`, `media` ou `baixa` (escala abaixo) |

## Escala de severidade

- **alta:** impede concluir uma tarefa principal (cadastro, compra, login).
- **media:** a tarefa é concluída, mas com erro, confusão ou perda de dados digitados.
- **baixa:** incômodo ou falha pequena, sem bloquear ninguém.

## Tipos

- **quebrado:** a funcionalidade falha (erro, ação sem efeito, dado perdido).
- **ux:** funciona, mas confunde ou atrapalha (texto vago, botão com aparência errada, informação tardia).
- **acessibilidade:** exclui quem usa teclado, leitor de tela ou tem baixa visão (sem texto alternativo, contraste baixo, foco impossível).

## Um bom bug plantado

- Tem causa única e clara: um agente que o encontra sabe dizer o que viu.
- É reproduzível sempre, nunca intermitente.
- Pode ser achado pelo nível de fidelidade pretendido (texto, telas, navegador ou API). Anote qual no campo "Onde" se for específico de um nível.
- Parece defeito real de um MVP, não pegadinha artificial.

## Um mau bug plantado

- Depende de sorte, tempo ou ambiente para aparecer.
- Duas causas misturadas no mesmo defeito (impede medir o acerto).
- Só quem leu o código acharia.
- Perigoso de verdade: nada de falha de segurança real, só dados de teste.

## Checklist final

- [ ] ID novo, sem repetir nenhum existente
- [ ] Comentário `BUG-xx` no código, na linha do defeito
- [ ] Linha completa na tabela "Catalogados" e ideia removida de "Ideias para plantar"
- [ ] Passos de reprodução testados (ou, se ainda não há como rodar o app, dito explicitamente)
- [ ] Nenhum bug catalogado anterior foi alterado
- [ ] Se chegou a 10 bugs com os 3 tipos, marcar o item no Gate 0 do `AGENTS.md`
