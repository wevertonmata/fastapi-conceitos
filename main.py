from fastapi import FastAPI

from routes import calculadora_v1, cursos_v1

app = FastAPI(
    title="Crud FastAPI Cursos",
    version='0.0.5',
    description="API de estudo FastAPI."
)

app.include_router(cursos_v1.router, tags=['cursos'], prefix="/api/v1/cursos")
app.include_router(calculadora_v1.router, tags=['calculadora'], prefix="/api/v1/calculadora")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)