from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from model import *
from adapters.cbioportalRoutes import router as cbioportalRouter


app = FastAPI()

# Include the router from the adapter_routes file
app.include_router(cbioportalRouter, prefix="/cbio", tags=["cbio"])

@app.get("/", response_class=HTMLResponse)
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}