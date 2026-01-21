# Funciones de persistencia de datos (lectura y escritura en JSON).

import json
import os

RUTA_ARCHIVO = "data/siniestros.json"


def leer_siniestros():
    if not os.path.exists(RUTA_ARCHIVO):
        return []

    with open(RUTA_ARCHIVO, "r", encoding="utf=8") as f:
        return json.load(f)


def guardar_siniestros(siniestros):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(siniestros, f, indent=4, ensure_ascii=False)
        
        
