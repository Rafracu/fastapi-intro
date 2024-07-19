from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()




movies = [
    {
"id": 1,
  "name": "Doofus Rick",
  "status": "unknown",
  "species": "Human",
  "type": 10,
  "gender": "Male",
  "origin": "werty",

    }
  ,     
     {
"id": 2,
  "name": "SEAL Team Rick",
  "status": "Dead",
  "species": "Human",
  "type": 20,
  "gender": "Male",
  "origin": ""

    }
]

@app.get('/', tags=['Home'])
def rase():
    
    return "HOLA juan"

@app.get('/movies', tags=['Movies'])
def get_movies():
    
   return movies

@app.get('/movies/{id}', tags=['Movies'])
def get_name(id:int):
    for name in movies:
        if name ['id'] == id:
            return name
        return[]

#ruta hasta el momento hasta cap 6 local host:8000/movies/name/?(define parametro query)id=1

@app.get('/movies/', tags=['Movies'])
def get_name_gender(gender:str, type:int):
  for name in movies:
        if name ['gender'] == gender:
            return name
        return[]
    

@app.post('/movies',tags=['Movies']) 
def create_movie(
    id:int=Body(), 
    name:str=Body(),
    status:str=Body(),
    species:str=Body(),
    type:int=Body(),
    gender:str=Body(),
    origin:str=Body()):
    
    movies.append({
       'id':id,
       'name':name,
       'status':status,
       'species':species,
        'type':type,
        'gender':gender,
        'origin':origin
    })  
    
    return movies


@app.put('/movies/{id}',tags=['Movies'])
def update_movie( 
    
    name:str=Body(),
    status:str=Body(),
    species:str=Body(),
    type:int=Body(),
    gender:str=Body(),
    origin:str=Body()
    ):
 for name in movies:
        if name ['id'] == id:
            name['name']=name
            status['status']=status
            species['species']=species
            type['type']=type
            gender['gender']=gender
            origin['origin']=origin
            
            return movies
        

@app.delete('/movies/{id}',tags=['Movies'])
def delete_movie (id:int):
 for name in movies:
        if name ['id'] == id:
            movies.remove(name)
            return movies