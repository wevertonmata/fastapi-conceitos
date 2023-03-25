from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @validator('titulo')
    def validar_titulo(cls, value: str):
        words = value.split(' ')
        if len(words) < 2: 
            raise ValueError('O titulo deve ter pelo menos 2 palavras')
        return value  
    
    @validator('aulas')
    def validar_aulas(cls, value: int):
        if value < 8: 
            raise ValueError('Deve ter mais de 8 aulas')
        return value  
    
    @validator('horas')
    def validar_horas(cls, value: int):
        if value < 12: 
            raise ValueError('Deve ter mais de 12 horas')
    
        if value > 100: 
            raise ValueError('Deve ter menos de 100 horas')
        return value 
    
          
cursos = [
    Curso(id=1,titulo="Curso Informatica Avançada ",aulas= 112,horas=58),
    Curso(id=2,titulo="Curso De Geometria",aulas= 60,horas=20),
    Curso(id=3,titulo="Curso De C#",aulas= 80,horas=80),
]