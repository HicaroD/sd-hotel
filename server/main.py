import uvicorn
from fastapi import FastAPI

from db import DBConnection

app = FastAPI()
db_connection = DBConnection()


@app.get("/rooms")
def get_all_rooms():
    rooms = db_connection.get_all_rooms()
    return {"rooms": rooms}


@app.patch("/rooms/{id}/checkin/")
def check_in(id: int):
    db_connection.check_in(id)
    return {"detail": f"Seu check-in no quarto de número {id} foi efetuado com sucesso"}


@app.patch("/rooms/{id}/checkout/")
def check_out(id: int):
    db_connection.check_out(id)
    return {"detail": f"Seu check-out no quarto de número {id} foi efetuado com sucesso. Volte sempre!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8900,
        reload=True,
    )
