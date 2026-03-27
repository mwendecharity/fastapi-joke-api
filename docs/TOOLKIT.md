# Getting Started with FastAPI – A Beginner's Toolkit

## 1. Title & Objective

**Technology:** FastAPI (Python Web Framework)

**Why I chose it:**

* FastAPI is beginner-friendly and uses Python
* It automatically generates interactive API documentation
* APIs are widely used in real-world applications

**End Goal:**
To build a simple Joke API that demonstrates GET and POST requests, filtering data, and working with JSON responses.

---

## 2. Quick Summary of the Technology

FastAPI is a modern Python framework used to build APIs quickly and efficiently. It allows developers to create endpoints that send and receive data over the web.

It is commonly used in:

* Web applications
* Mobile app backends
* Machine learning APIs

---

## 3. System Requirements

* Python 3.8+
* VS Code or any code editor
* Internet connection
* Terminal (Command Prompt or Bash)

---

## 4. Installation & Setup

```bash
python --version
mkdir fastapi-joke-api
cd fastapi-joke-api

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## 5. Minimal Working Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}
```

---

## 6. AI Prompt Journal

**Prompt 1:** Explain FastAPI to a beginner
**What I learned:** FastAPI is used to build APIs and is easy to use with Python.

**Prompt 2:** How to set up a FastAPI project
**What I learned:** I learned how to create a virtual environment and install dependencies.

**Prompt 3:** What does @app.get("/") mean?
**What I learned:** It defines an endpoint that responds to GET requests.

**Prompt 4:** How to fix module not found error
**What I learned:** I needed to activate my virtual environment.

**Prompt 5:** How to create a POST endpoint
**What I learned:** I learned how to accept user input using Pydantic models.

---

## 7. Common Issues & Fixes

* FastAPI not found → install using pip
* Server not running → use uvicorn command
* Changes not updating → use --reload
* Errors in POST → check request format

---

## 8. References

* FastAPI Documentation
* Python Documentation
* AI assistance (ChatGPT)

---

## 9. Learning Reflection

**What I learned:**

* How APIs work
* Difference between GET and POST
* How to run a backend server

**How AI helped me:**

* Guided me step-by-step
* Helped debug errors
* Explained difficult concepts simply

**What I would improve:**

* Practice more projects
* Explore database integration

---

## 10. Skills Demonstrated

* API development
* Problem-solving
* Debugging
* Technical documentation

---

