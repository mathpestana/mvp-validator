"""Contrato comum a todos os provedores de LLM."""

from dataclasses import dataclass
from typing import Literal, Protocol


@dataclass(frozen=True)
class Mensagem:
    papel: Literal["user", "assistant"]
    conteudo: str


@dataclass(frozen=True)
class RespostaLLM:
    texto: str
    modelo: str
    tokens_entrada: int
    tokens_saida: int
    custo_usd: float
    latencia_ms: int


class ProvedorLLM(Protocol):
    async def gerar(
        self, *, sistema: str, mensagens: list[Mensagem], modelo: str
    ) -> RespostaLLM: ...
