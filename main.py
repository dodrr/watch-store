from fastapi import FastAPI

app = FastAPI()

@app.get("/product")
def get_product():
    return [
        {"name": "Casio", "price": 19000},
        {"name": "Hublot", "price": 20000},
        {"name": "Patek Philippe", "price": 21234}
    ]

