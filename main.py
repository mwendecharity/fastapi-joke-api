# main.py - A Simple Joke API built with FastAPI

from fastapi import FastAPI
from pydantic import BaseModel
import random

# Initialize the FastAPI application
app = FastAPI(
    title="Joke API",
    description="A beginner-friendly API that serves random jokes",
    version="1.0.0"
)

# Our joke database
jokes = [
    {"id": 1, "category": "programming", "joke": "Why do programmers prefer dark mode? Because light attracts bugs!"},
    {"id": 2, "category": "programming", "joke": "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'"},
    {"id": 3, "category": "general", "joke": "Why don't scientists trust atoms? Because they make up everything!"},
    {"id": 4, "category": "general", "joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."},
    {"id": 5, "category": "programming", "joke": "There are only 10 types of people in the world: those who understand binary and those who don't."},
]

# Root endpoint
@app.get("/")
def read_root():
    """Welcome message for the API"""
    return {
        "message": "Welcome to the Joke API!",
        "endpoints": {
            "/jokes": "Get all jokes",
            "/jokes/random": "Get a random joke",
            "/jokes/{id}": "Get a specific joke by ID",
            "/jokes/category/{category}": "Get jokes by category"
        }
    }

# GET all jokes
@app.get("/jokes")
def get_all_jokes():
    """Return all jokes in the database"""
    return {"total": len(jokes), "jokes": jokes}

# GET a random joke
@app.get("/jokes/random")
def get_random_joke():
    """Return a randomly selected joke"""
    return random.choice(jokes)

# GET joke by ID
@app.get("/jokes/{joke_id}")
def get_joke_by_id(joke_id: int):
    """Return a specific joke by its ID"""
    for joke in jokes:
        if joke["id"] == joke_id:
            return joke
    return {"error": "Joke not found", "requested_id": joke_id}

# GET jokes by category
@app.get("/jokes/category/{category}")
def get_jokes_by_category(category: str):
    """Return all jokes in a specific category"""
    filtered = [j for j in jokes if j["category"].lower() == category.lower()]
    if filtered:
        return {"category": category, "total": len(filtered), "jokes": filtered}
    return {"error": f"No jokes found in category: {category}"}

# POST endpoint to add a new joke
class JokeCreate(BaseModel):
    category: str
    joke: str

@app.post("/jokes")
def create_joke(new_joke: JokeCreate):
    """Add a new joke to the database"""
    joke_entry = {
        "id": len(jokes) + 1,
        "category": new_joke.category,
        "joke": new_joke.joke
    }
    jokes.append(joke_entry)
    return {"message": "Joke added successfully!", "joke": joke_entry}
