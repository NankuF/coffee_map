import json
from typing import Tuple, Union, List

import environs
import folium
import requests
from geopy import distance

from app import run_site


def fetch_coordinates(apikey: str, address: str) -> Union[Tuple, None]:
    """
    Получить координаты указанного адреса, из сервиса Яндекс "JavaScript API и HTTP Геокодер"
    (https://developer.tech.yandex.ru/services/3).

    :param apikey: ключ, полученный в кабинете разработчика Яндекс.
    :param address: адрес, по которому необходимо получить координаты.
    :return: координаты адреса - широта и долгота.
    """
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lat, lon


def fetch_nearest_cafes(address: tuple, cafes: list, count: int) -> List[dict]:
    """
    Получить список ближайших кафе.

    :param address: широта и долгота вашего местоположения.
    :param cafes: список кафе с географическими данными.
    :param count: количество ближайших кафе.
    :return: список ближайших кафе.
    """

    cafes_coords = []
    for cafe in cafes:
        cafes_coords.append({
            'title': cafe['Name'],
            'distance': distance.distance(address, (cafe['Latitude_WGS84'], cafe['Longitude_WGS84'])).km,
            'latitude': cafe['Latitude_WGS84'],
            'longitude': cafe['Longitude_WGS84'],
            'address': cafe['Address'],
        })
    return sorted(cafes_coords, key=lambda cafe: cafe['distance'])[:count]


def build_map(address: tuple, nearest_cafes: list) -> None:
    """
    Создать карту с вашим местоположением и ближайшими к нему кафе.

    :param address: широта и долгота вашего местоположения.
    :param nearest_cafes: список ближайших кафе.
    """

    map_ = folium.Map(location=[*address])

    for cafe in nearest_cafes:
        folium.Marker(
            [cafe['latitude'], cafe['longitude']],
            popup=f"<i>{cafe['address']}</i>", tooltip=cafe['title']
        ).add_to(map_)

    map_.save('map.html')


def main():
    env = environs.Env()
    env.read_env()
    ya_apikey = env.str('YA_APIKEY')

    with open('coffee.json', 'r', encoding='CP1251') as file:
        cafes = json.loads(file.read())

    address = fetch_coordinates(ya_apikey, input('Где вы находитесь?: '))
    nearest_cafes = fetch_nearest_cafes(address, cafes=cafes, count=5)
    build_map(address, nearest_cafes)
    run_site()


if __name__ == '__main__':
    main()
