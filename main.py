from fastapi import FastAPI
from structapi.config.params import Item

app = FastAPI()


@app.get("/")
async def root():
    return "This is the root from FastAPI"


@app.post("/items")
async def create_item(item: Item):
    return item


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"deleted": item_id}
