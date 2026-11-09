"""Orquestrador e executores.

- Orquestrador: cria uma execução por persona e tarefa, roda em paralelo
  e aplica limites de passos, tempo e custo.
- Executores, um por nível de fidelidade:
  - conceito (Fase 1): a persona lê um texto ou landing page;
  - visual: a persona olha telas;
  - navegador (Fase 2): a persona usa o produto via Playwright,
    no ciclo observar -> decidir -> agir -> registrar;
  - api: a especificação OpenAPI vira ferramentas para a persona.
- Cada passo vira um registro na tabela evento.
"""
