from fastapi import FastAPI, Request
import init_response

app = FastAPI()


@app.get("/cotizacion")
async def create_item(req: Request):
    api_response = init_response.init()
    return api_response