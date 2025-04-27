# solver_remoto.py
from cliente import query
import json  # o re, según el formato de respuesta

def resolver_n_reinas(n: int) -> list[list[int]]:
    raw = query(str(n))        # envía "8\n", "10\n", etc.
    # Supongamos que el servidor responde un JSON, p.ej. "[[1,5,8,6,3,7,2,4], …]"
    try:
        soluciones = json.loads(raw)
    except json.JSONDecodeError:
        # Si viene otro formato, implementa aquí tu parser
        raise ValueError(f"Respuesta inválida del servidor: {raw!r}")
    return soluciones
