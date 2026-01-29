from utils.requester import get_data_by_url


def main():
    url = f'http://{input("Введите адрес сайта: ")}'
    print(f'Отправляем запрос к {url}')
    data = get_data_by_url(url)
    print('Пришел ответ со статусом:', data.status_code)


if __name__ == '__main__':
    main()
