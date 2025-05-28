from fastapi import APIRouter
from app.model.cliente import Cliente
from app.util.responsehelper import jsonc
from app.controller.avaliacao_controller import calc_nucleo

router = APIRouter()

@router.get("/health")
def read_health():
    return {"status": "funcionando"}

# Endpoint
@router.post("/avaliar")
async def avaliacao(cliente: Cliente):
    print(f"Iniciando a avaliação:{cliente}")
    r = calc_nucleo(cliente)
    print(f"Resultado: {r.resposta}")
    return jsonc(r)
