import asyncio

from app.llm import Mensagem
from app.llm.falso import ProvedorFalso


def test_provedor_falso_registra_chamada_e_responde() -> None:
    provedor = ProvedorFalso(resposta="olá")
    mensagens = [Mensagem(papel="user", conteudo="oi")]

    resposta = asyncio.run(
        provedor.gerar(sistema="teste", mensagens=mensagens, modelo="modelo-teste")
    )

    assert resposta.texto == "olá"
    assert resposta.modelo == "modelo-teste"
    assert provedor.chamadas == [mensagens]
