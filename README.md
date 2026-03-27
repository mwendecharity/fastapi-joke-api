# fastapi-joke-api
A beginner-friendly REST API built with FastAPI that allows users to retrieve, filter, and add jokes. Demonstrates API development, HTTP methods, and data validation.
# Joke API 😂

A beginner-friendly REST API built using FastAPI that allows users to retrieve, filter, and add jokes.

---

## 🚀 Features

* Get all jokes
* Get a random joke
* Retrieve a joke by ID
* Filter jokes by category
* Add new jokes
* Interactive API documentation

---

## 🛠️ Built With

* Python
* FastAPI
* Uvicorn

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/yourusername/fastapi-joke-api.git
cd fastapi-joke-api

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

---

## 🌐 Open in Browser

Visit:

http://127.0.0.1:8000/docs

This opens the interactive API documentation.

---

## 📌 Example Endpoint

GET /jokes/random

Response:

```json
{
  "id": 2,
  "category": "programming",
  "joke": "A SQL query walks into a bar..."
}
```

---

## 📚 What I Learned

* Building APIs using FastAPI
* Understanding GET and POST requests
* Using Pydantic for data validation
* Working with virtual environments
* Debugging and fixing errors

---

## 🎓 Project Purpose

This project was created as part of a learning journey to understand backend development and API design using modern Python tools.

---
