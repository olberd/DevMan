import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, bitly_url, link):
    headers = {
      'Authorization': f'Bearer {token}'
    }
    data = {
      'long_url': link,
    }
    response = requests.post(bitly_url, headers=headers, json=data)
    response.raise_for_status()
    short_link = response.json()
    return short_link['link']


def count_clicks(token, bitly_url, link):
    link_parse = urlparse(link)
    link = f'{link_parse.netloc}{link_parse.path}'
    url_for_link = f'{bitly_url}{link}/clicks/summary'
    headers = {
      'Authorization': f'Bearer {token}'
    }
    response = requests.get(url_for_link, headers=headers)
    response.raise_for_status()
    response_json = response.json()
    clicks_count = response_json['total_clicks']
    return clicks_count


def is_bitlink(token, bitly_url, link):
    headers = {
      'Authorization': f'Bearer {token}'
    }
    parsed_url = urlparse(link)
    link = f'{parsed_url.netloc}{parsed_url.path}'
    response = requests.get(f'{bitly_url}{link}', headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.environ['TOKEN_BITLY']
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    parser = argparse.ArgumentParser(description='Сокращение ссылок')
    parser.add_argument('link', help='Введите ссылку')
    args = parser.parse_args()
    link = args.link
    try:
        if is_bitlink(bitly_token, bitly_url, link):
            print(
                'По вашей ссылке прошли:',
                count_clicks(bitly_token, bitly_url, link),
                'раз(а)'
            )
        else:
            print('Битлинк', shorten_link(bitly_token, bitly_url, link))
    except requests.exceptions.HTTPError:
        print('Исправьте ссылку')


if __name__ == '__main__':
    main()
