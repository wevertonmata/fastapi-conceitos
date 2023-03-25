from fastapi import APIRouter

from fastapi import Query, Header

from typing import Optional

router = APIRouter(tags=['calculadora'], prefix="/calculadora",responses={404: {"description": "Not found"}},)

@router.get('')
async def soma(a: int = Query(gt=0), b: int = Query(default=None, gt=0), c: Optional[int] = None, x_geek: str = Header(default=None)):
    soma: int = a + b
    if c:
        soma += c
    print(f"X_GEEK: {x_geek}")
    
    return {"Resultado": soma}