from fastapi import FastAPI
from routers import auth

app = FastAPI()
app.include_router(auth.router)

@app.get('/')
def func():
    return {
        'Message' : "API is Working"
    }


# from fastapi import FastAPI
# # Import your router module
# from routers import items
#
# app = FastAPI()
#
# # Call and register the router
# app.include_router(items.router)
#
# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}


# from fastapi import APIRouter
#
# # Initialize the router instance
# router = APIRouter()
#
# @router.get("/items")
# def get_items():
#     return {"message": "List of items"}
