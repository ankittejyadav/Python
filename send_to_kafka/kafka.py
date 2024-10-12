import requests
import json
from quixstreams import Application


def response():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": 51.5, "longitude": -0.11, "current": "temperature_2m"},
    )

    return response


response = response()
weather = response.json()

app = Application(broker_address="localhost:9092", loglevel="DEBUG")

with app.get_producer() as producer:
    producer.produce(topic="weather_data_demo", key="london", value=json.dumps(weather))

print(weather_report().json())
