from fastapi import FastAPI  # pyright: ignore[reportMissingImports]
from routers import auth

app = FastAPI()
app.include_router(auth.router)

@app.get('/')
def func():
    return {
        'Message' : "API is Working"
    }
