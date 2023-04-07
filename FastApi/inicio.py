
from fastapi import FastAPI
# -------------------------------------------
#  DOCUMENTACION OFICIAL FAST API https://fastapi.tiangolo.com/
# ---------------------------------------------



# 
# 
#  ACTIVATE (PARA EL ENTORNO DE DESARROLLO)
#  python -m pip install --upgrade pip (PARA ACTUALIZAR EL PIP)
#  pip install uvicorn  (ESTO ES PARA EL SERVIDOR LEVANTADO)
#  uvicorn main:app --reload (PARA ARRANCAR SIN ESTAR CERRANDO)
#  uvicorn main:app --reload --port 5000  (PARA CAMBIAR EL PUERTO Y CORRER)
#   uvicorn main:app --reload --port 6000 --host 0.0.0.0



app = FastAPI()
app.title = "aplicaciones de venta"
app.version = '2.0.0'


#  CREAR PUNTO DE ENTRADA O ENDPOIT

@app.get('/',tags=['inicio'])
def mensaje():
    return 'Hola Bienvenido a mi FastAPi x1000 ya okis x2'



