import requests
from settings import ACCESS_TOKEN
from typing import Optional
from schemas import PagesResponseModel, ResponseAPIModel


def fetch(url: str, params: dict) -> dict:
    response = requests.get(url=url, params=params)
    return response.json()


def get_api_pages(access_token: str) -> PagesResponseModel:
    url = f'https://graph.facebook.com/v20.0/me/accounts'
    params = {'access_token': access_token}
    response = fetch(url=url, params=params)
    pages = PagesResponseModel(**response)
    return pages


def get_posts(page_token: str, page_id: str, limit: Optional[int] = 50) -> ResponseAPIModel:
    url = f'GET https://graph.facebook.com/v20.0/{page_id}/posts'
    params = {'access_token': page_token, 'limit': limit}
    response = fetch(url=url, params=params)
    posts = ResponseAPIModel(**response)
    return posts


def get_reviews(page_token: str, comment_id: str, limit: Optional[int] = 50):
    url = f'GET https://graph.facebook.com/v20.0/{comment_id}/comments'
    params = {'access_token': page_token, 'limit': limit}
    response = fetch(url=url, params=params)
    reviews = ResponseAPIModel(**response)
    return reviews


def answer_from_reviews():
    pass


def main():
    access_token = ACCESS_TOKEN
    pages = get_api_pages(access_token=access_token)
    all_posts = []
    for page in pages.data:
        page_id = page.id
        page_token = page.access_token
        posts = get_posts(page_token=page_token, page_id=page_id)
        all_posts.append(posts)


if __name__ == '__main__':
    main()
