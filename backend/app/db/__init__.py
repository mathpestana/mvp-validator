"""Banco de dados: Postgres + pgvector, via SQLAlchemy 2 e Alembic.

Tabelas previstas (detalhes no documento do projeto):
projeto, versao_mvp, bug_plantado, fonte_dados, persona, painel, painel_persona,
credencial, memoria, experimento, execucao, evento, achado, resposta_preco,
relatorio, chamada_llm, embedding.

Sprint 0: criar os modelos de chamada_llm, projeto e bug_plantado e a primeira
migração (que também roda CREATE EXTENSION vector).
"""
