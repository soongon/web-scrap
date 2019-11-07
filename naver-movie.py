import requests

params = {
    'query': '조커',
    'display': 100
}
headers = {
    'X-Naver-Client-Id': 'ZLgcTCdqj5xHhj9eXyCL',
    'X-Naver-Client-Secret': '_nxyGYlNwU'
}
res = requests.get('https://openapi.naver.com/v1/search/movie.json'
             , params=params, headers=headers)

movies = []
for movie in res.json()['items']:
    movies.append([
        movie['title'],
        movie['subtitle'],
        movie['actor']
    ])

print(len(movies))