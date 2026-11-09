"""Camada de LLM: o único lugar do projeto que conversa com provedores de modelo.

Regra (AGENTS.md): nenhum outro módulo importa o SDK de um provedor.
Toda chamada deve ser registrada na tabela chamada_llm (Gate 0).
"""

from app.llm.base import Mensagem, ProvedorLLM, RespostaLLM

__all__ = ["Mensagem", "ProvedorLLM", "RespostaLLM"]
