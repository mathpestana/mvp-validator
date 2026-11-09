"""Provedor falso para testes: responde sem chamar nenhuma API."""

from app.llm.base import Mensagem, RespostaLLM


class ProvedorFalso:
    def __init__(self, resposta: str = "resposta falsa") -> None:
        self.resposta = resposta
        self.chamadas: list[list[Mensagem]] = []

    async def gerar(self, *, sistema: str, mensagens: list[Mensagem], modelo: str) -> RespostaLLM:
        self.chamadas.append(mensagens)
        return RespostaLLM(
            texto=self.resposta,
            modelo=modelo,
            tokens_entrada=0,
            tokens_saida=0,
            custo_usd=0.0,
            latencia_ms=0,
        )
