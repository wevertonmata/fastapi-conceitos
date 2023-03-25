from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes import calculadora_v1, cursos_v1

app = FastAPI(
    title="Crud FastAPI Cursos",
    version='0.0.5',
    description="API de estudo FastAPI."
)

# Redirect to docs

@app.get("/",  include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')


## Routes

app.include_router(cursos_v1.router, tags=['cursos'], prefix="/api/v1/cursos")
app.include_router(calculadora_v1.router, tags=['calculadora'], prefix="/api/v1/calculadora")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)