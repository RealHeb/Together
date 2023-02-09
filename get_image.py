import sys
import requests


def getImage(scale):
    coordinates = '37.530887,55.70311'

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": coordinates,
        "z": scale,
        "l": "map"
    }
    response = requests.get(map_api_server, map_params)

    if not response:
        return
        # print("Ошибка выполнения запроса.")
        # print("Http статус:", response.status_code, "(", response.reason, ")")
        # sys.exit(1)

    if response:
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
