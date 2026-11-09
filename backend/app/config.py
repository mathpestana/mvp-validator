"""Configuração lida do arquivo .env (veja .env.example na raiz)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuracao(BaseSettings):
    model_config = SettingsConfigDict(env_file=("../.env", ".env"), extra="ignore")

    database_url: str = "postgresql+psycopg://validador:validador@localhost:5432/validador"
    anthropic_api_key: str = ""
    modelo_persona: str = "claude-haiku-5-5"
    modelo_relatorio: str = "claude-sonnet-5-5"
    chave_cifra_credenciais: str = ""
    limite_passos_execucao: int = 30


configuracao = Configuracao()
