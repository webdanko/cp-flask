from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Timeweb Cloud + FastAPI = ❤️"

@app.get("/api/{entity_type}/")
def get_entity_list(entity_type: str):
    return_list = []
    return_list.append({
        'type' : entity_type,
        'id' : 1,
        'name' : 'name_1'
    })
    return return_list