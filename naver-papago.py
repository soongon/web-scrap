import requests

headers = {
    'X-Naver-Client-Id': 'ZLgcTCdqj5xHhj9eXyCL',
    'X-Naver-Client-Secret': '_nxyGYlNwU'
}

text = '''
Federal prosecutors accused two former Twitter employees of 
spying on behalf of Saudi Arabia on Wednesday.
Ali Alzabarah, a Saudi national, and Ahmad Abouammo, 
a US citizen, used their access at the social media giant 
to gather sensitive and nonpublic information on dissidents 
of the Saudi regime, the Justice Department alleged in a 
criminal complaint.
The case, unsealed in San Francisco federal court, 
underscores allegations the Saudi government tries to 
control anti-regime voices abroad. It also recalls a move 
reportedly directed by the country's controversial leader
 to weaponize online platforms against critics.
'''

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text
}

res = requests.post('https://openapi.naver.com/v1/papago/n2mt',
              headers=headers, data=payload)

print(res.json()['message']['result']['translatedText'])