from fastapi import FastAPI
from config.dbConnection import client
from dotenv import dotenv_values

from routes.products_route import products_router

config = dotenv_values(".env")

app = FastAPI()

app.include_router(products_router)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = client
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

@app.get("/")
def read_root():
    return {"Project": "Initialized"}
