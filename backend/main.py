from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()


TMDB_API_KEY = "aba898c11299b0f3286b86468b71dcfd"
TMDB_BASE_URL = "https://api.themoviedb.org/3"

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/movies/popular")
def get_popular_movies():
    url = f"{TMDB_BASE_URL}/movie/popular?api_key={TMDB_API_KEY}&language=pt-BR"
    response = requests.get(url)
    return response.json()

@app.get("/movies/{movie_id}")
def get_movie_details(movie_id: int):
    url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&language=pt-BR"
    response = requests.get(url)
    return response.json()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)