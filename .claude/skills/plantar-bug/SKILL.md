---
name: plantar-bug
description: Planta e cataloga um bug de propósito no app-exemplo/ do Validador de MVP. Use quando o pedido for plantar, adicionar, inventar ou catalogar um bug, ou avançar o item "10 bugs plantados" do Gate 0. Também use ao achar um defeito não catalogado no app-exemplo/ (vira BUG-xx acidental). Não use para corrigir bugs: eles são o gabarito.
allowed-tools: Read Grep Glob Edit Write
---

# plantar-bug

O `app-exemplo/` é o gabarito que mede os agentes: cada bug catalogado é uma resposta certa que as personas devem encontrar. Esta skill planta um bug por vez, sempre catalogado.

## Antes de começar

1. Leia `app-exemplo/AGENTS.md` e `app-exemplo/BUGS.md`.
2. Descubra o próximo ID livre (`BUG-01`, `BUG-02`, ...) e quantos bugs já existem de cada tipo. A meta é pelo menos 10, dos 3 tipos: **quebrado**, **UX confusa** e **acessibilidade**.
3. Escolha o tipo menos representado. Se o usuário pediu um bug específico, siga o pedido.

## Passos

1. Escolha uma ideia da seção "Ideias para plantar" do `BUGS.md` (ou proponha uma nova, no mesmo estilo).
2. Implemente o bug no `app-exemplo/` com o menor código possível, em um ponto onde uma persona realista tropeçaria.
3. Marque o código com o comentário `# BUG-xx` (ou o equivalente da linguagem) na linha do defeito.
4. Na mesma mudança, mova a ideia da seção "Ideias para plantar" para a tabela "Catalogados" do `BUGS.md`, com ID, tipo, descrição, onde, como reproduzir e severidade.
5. Confira o checklist de [reference.md](reference.md).

## Nunca

- Corrigir um bug já catalogado, nem "de passagem".
- Plantar bug sem catalogar, ou catalogar sem o comentário no código.
- Mexer fora de `app-exemplo/`, a não ser para marcar o item no Gate 0 do `AGENTS.md` quando a meta de 10 for atingida.

## Defeito não catalogado

Se encontrar um bug que não está no catálogo, registre-o como `BUG-xx (acidental)` e pergunte ao usuário se ele fica ou sai. Não decida sozinho.

Formato das colunas, escala de severidade, exemplos de bugs bons e ruins e o checklist final estão em [reference.md](reference.md).
