from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import overpass

def get_overpass_around(lat, lon, radius):
    api = overpass.API(endpoint="https://maps.mail.ru/osm/tools/overpass/api/interpreter")
    request = "nwr(around:%s, %s, %s)" % (radius, lat, lon)
    api.get()
    result = []
    return result

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Timeweb Cloud + FastAPI = ❤️"


@app.get("/api/around/{lat}/{lon}/{radius}")
def get_entity_list(lat: float, lon: float, radius: float):
    result = get_overpass_around(lat, lon, radius)
    return result
