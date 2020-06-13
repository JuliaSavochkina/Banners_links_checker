import requests
from typing import Generator
from get_data import get_banners


def links_work() -> Generator:
    """
    Функция совершает переход по ссылке перехода для каждого баннера и отдает генератор, содержащий списки редиректов.
    :return: генератор со списками редиректов для каждой ссылки.
    """
    banners_lists: list = get_banners()
    for banners_list in banners_lists:
        for banner in banners_list:
            response = requests.get(banner['direct_link'])
            banner_redirects = []
            for resp in response.history:
                banner_redirects.append(resp.url)
            yield banner_redirects


if __name__ == '__main__':
    for lst in links_work():
        print(lst)
