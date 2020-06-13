import csv
from links_work import links_work


def csv_exporter() -> None:
    """
    Функция пополняет csv файл новой строкой, содержащей редиректы через запятую.
    Если файла нет, создает его.
    """
    with open('litres.csv', 'a', newline='') as csvfile:
        row = csv.writer(csvfile, delimiter=',')
        for lst in links_work():
            row.writerow(lst)


if __name__ == '__main__':
    csv_exporter()
