from fastapi import FastAPI

from routes import cursos_router, calculadora_router

app = FastAPI(
    title="Crud FastAPI Cursos",
    version='0.0.5',
    description="API de estudo FastAPI."
)

app.include_router(cursos_router.router, tags=['cursos'])
app.include_router(calculadora_router.router, tags=['calculadora'])


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)