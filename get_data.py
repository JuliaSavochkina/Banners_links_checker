import requests
import json
from keys import key, client_id


def get_token(scope: str = 'banners_for_website') -> str:
    """
    Получает токен для работы с API.
    :param scope: перечень методов, для которых запрашивается токен, методы подаются через пробел;
    :return: строка - токен.
    """
    url: str = 'https://api.admitad.com/token/'
    params: dict = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'scope': scope
    }
    headers = {'Authorization': key}
    r = requests.post(url, params=params, headers=headers)
    json_r: dict = json.loads(r.text)
    return json_r['access_token']


def get_banners(c_id: str = '1721', w_id: str = '22162') -> list:
    """
    Функция постранично абирает информацию по баннерам, формируя лист словарей. Словарь = информация по баннеру.
    :param c_id: номер программы рекламодателя;
    :param w_id: номер площадки веб-мастера;
    :return: список словарея, один словарь - один баннер.
    """
    lst: list = []
    for i in range(5):
        url: str = f'https://api.admitad.com/banners/{c_id}/website/{w_id}/?limit=500&offset={i*500}'
        headers = {'Authorization': f'Bearer {get_token()}'}
        r = requests.get(url, headers=headers)
        json_r: dict = json.loads(r.text)
        lst.append(json_r['results'])
    return lst


if __name__ == '__main__':
    print(get_banners())
