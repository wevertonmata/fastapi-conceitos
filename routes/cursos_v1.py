from time import sleep
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import Response
from fastapi import Path

from models import Curso, cursos
from typing import Any, List, Optional

router = APIRouter()

def fake_db():
    try:
        print("Abrindo conexão com banco de dados")
        sleep(1)
    finally:
        print("Fechando conexão")
        sleep(1)


@router.get('', 
         description="Retorna todos os cursos ou uma lista vazia", 
         summary="Retorna todos os cursos",
         response_model=List[Curso],
         response_description="Cursos encontrados com sucesso.",
         status_code=status.HTTP_200_OK)
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@router.get('/{curso_id}')
async def get_cursos(
    curso_id: int = Path(title="ID do curso",description=f"Deve ser entre 1 e {len(cursos)}",gt=0,lt=len(cursos)),
    db: Any = Depends(fake_db)
    ):
    
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')


@router.post("", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
          
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso

@router.put('/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso não encontrado com id {curso_id}.')

@router.delete('/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso não encontrado com id {curso_id}.')