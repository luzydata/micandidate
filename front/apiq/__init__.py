import pandas as pd
import requests


##############################################################################
################## API BASE ##################################################
##############################################################################
BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'

def get_token():
    token=''
    print('--Getting token from file.')
    with open("./apiq/token.txt") as fp:
        token = fp.readlines()[0].strip()
    return token


def querry_for(endpoint="area", value='0'):
    """
    area
    contest_id
    person
    membership
    party
    """
    print('Running get_token.')
    token = get_token()
    # This is hardcoded!!
    auth_header = {
        'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoibkJLTVQ0SVBQRnF3enFINVRKVkdlQSIsInN1YiI6IjllODY5ODA2LTZmNjgtNDhlNi1iNzhlLTk5ODI0MDEzNzAyNyIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjIxMzA1NTI4LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9KMUtJc2NwaGgiLCJjb2duaXRvOnVzZXJuYW1lIjoiOWU4Njk4MDYtNmY2OC00OGU2LWI3OGUtOTk4MjQwMTM3MDI3IiwiZXhwIjoxNjIxMzE5OTI4LCJpYXQiOjE2MjEzMDU1MjgsImVtYWlsIjoidXJkYWliYXljQGdtYWlsLmNvbSJ9.MitBhvBxRZ2o1aEFjP2Me96xUPgQfzMTJ7mz5ELtazSsTkdFv9NO7wAy8sTemM2fhpS0aQOBtszEV1mXNWGH1OOKo8THzICVSKagX3vmJ0vwl24dqAEYgvf4hDDASwb5PDheqO1ETV4HUJAyDCk4sb3HAw1qbOKz2IJ5pLi6bd9jnaXfAym3GEOrfVpz4IaQJ3QKyZAQji8yg32nDkTO8x-doE8EhDfZZqCFhjGW7-Z8CxrviZU8JJolFaj5Fy1--JRWnAH3inE3eyuSNzKCeNcZs6mIqck5cF9OSz_o-eJw3J6IE5_Q9rMdaKmD0uV-v02wQMhbefnb5oaI4_tYUw'
        }

    response = requests.get(BASE+str(endpoint)+'/'+str(value),
                            headers=auth_header,
                            verify=True,
                            timeout=None)

    return response.json()
    # print(jsonResponse)
    # print(jsonResponse["election_identifier"])
    # person_ids = jsonResponse["person_ids"]
