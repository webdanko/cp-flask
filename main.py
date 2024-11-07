import overpass
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Timeweb Cloud + FastAPI = ❤️"

@app.get("/api/around/{lat}/{lon}/{radius}")
def get_overpass_around(lat, lon, radius):
    api = overpass.API(endpoint="https://maps.mail.ru/osm/tools/overpass/api/interpreter")
    request = "nwr(around:%s, %s, %s)" % (radius, lat, lon)
    result = api.get(request)
    return result
