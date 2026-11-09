"""Ponto de entrada da API."""

from fastapi import FastAPI

app = FastAPI(title="Validador de MVP", version="0.0.1")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
