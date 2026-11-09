# AGENTS.md · app-exemplo

Este app é o **gabarito** do projeto. Ele tem bugs colocados de propósito para medir quantos problemas as personas encontram (cobertura) e quantos alarmes são falsos (precisão).

## Regras

1. **Nunca corrija um bug catalogado em `BUGS.md`**, nem como "melhoria de passagem". Corrigir um bug estraga a medição.
2. Todo bug novo entra em `BUGS.md` com ID, tipo, onde está e como reproduzir, no mesmo commit em que é criado.
3. O mesmo ID vai como comentário no código (`# BUG-03`), para achar o bug depois.
4. Se um bug **não** catalogado for encontrado aqui, registre-o como `BUG-xx (acidental)` e pergunte se ele deve ficar ou sair.
5. Para testar comparação A/B (Fase 4), crie uma versão corrigida numa pasta ou rota separada (`v2/`), nunca alterando a original.
