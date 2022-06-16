import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, link):
    headers = {
      'Authorization': f'Bearer {token}'
    }
    data = {
      'long_url': link,
    }
    response = requests.post(BITLY_URL, headers=headers, json=data)
    response.raise_for_status()
    short_link = response.json()
    return short_link['link']


def count_clicks(token, link):
    link_parse = urlparse(link)
    link = link_parse.netloc + link_parse.path
    url_for_link = f'{BITLY_URL}{link}/clicks/summary'
    headers = {
      'Authorization': f'Bearer {token}'
    }
    response = requests.get(url_for_link, headers=headers)
    response.raise_for_status()
    response_json = response.json()
    clicks_count = response_json['total_clicks']
    return clicks_count


def is_bitlink(token, link):
    headers = {
      'Authorization': f'Bearer {token}'
    }
    parsed_url = urlparse(link)
    link = parsed_url.netloc + parsed_url.path
    response = requests.get(f'{BITLY_URL}{link}', headers=headers)
    return response.ok


def main():
    parser = argparse.ArgumentParser(description='Сокращение ссылок')
    parser.add_argument('link', help='Введите ссылку')
    args = parser.parse_args()
    link = args.link
    try:
        if is_bitlink(BITLY_TOKEN, link):
            print(
                'По вашей ссылке прошли:',
                count_clicks(BITLY_TOKEN, link),
                'раз(а)'
            )
        else:
            print('Битлинк', shorten_link(BITLY_TOKEN, link))
    except requests.exceptions.HTTPError:
        print('Исправьте ссылку')


if __name__ == '__main__':
    load_dotenv()
    BITLY_TOKEN = os.environ['TOKEN_BITLY']
    BITLY_URL = 'https://api-ssl.bitly.com/v4/bitlinks/'
    main()
