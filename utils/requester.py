import requests


def get_data_by_url(url: str):
    response = requests.get(url)

    if response.status_code != 200:
        return {'data': 'Bad Request'}

    return response
