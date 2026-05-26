# src/main.py
# MVP Asistente IA – TiendaYa
# Sesión 10: Estructura base del proyecto

from fastapi import FastAPI

app = FastAPI(title='Asistente IA MVP - TiendaYa')

@app.get('/')
def raiz():
    return {
        'mensaje': 'Asistente de TiendaYa activo y operando', 
        'version': '0.1.0'
    }

# TODO: implementar endpoint /chat para interactuar con los clientes en la siguiente sesión