import os
import requests
import pandas as pd

def get_contest_id(area_electoral):
    basedir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(basedir, 'seccion_to_contest.csv')
    clave_electoral = pd.read_csv(file)
    clave_electoral.drop(['ENTIDAD', 'NOMBRE ENTIDAD', 'DISTRITO', 'DISTRITO LOCAL', 'MUNICIPIO'],axis=1, inplace=True)
    clave_electoral.set_index("SECCION", inplace=True)
    contest_id = clave_electoral.loc[area_electoral].values[0]
    return contest_id




def api_query(contest_id, auth_header):

    # request the contest to the api
    BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'
    response = requests.get(BASE + f'contest/{contest_id}', headers=auth_header, verify=True,  timeout=None)
    if response.status_code == 200:
        contest = response.json()
        candidatos = []
        for candidato in contest['person_ids']:
            response = requests.get(BASE + 'person/'+str(candidato), headers=auth_header, verify=True,  timeout=None)
            candidato = response.json()
            candidatos.append(candidato)
            return candidatos
    else:
        return 1


if __name__ == '__main__':
    area_electoral = 10
    contest_id=get_contest_id(area_electoral)
    print(contest_id)
    auth_header = {
    	'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiWnEySWlra0M2Umw2TThXUnJqQUFYUSIsInN1YiI6IjllODY5ODA2LTZmNjgtNDhlNi1iNzhlLTk5ODI0MDEzNzAyNyIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV2ZW50X2lkIjoiYjBlYjM3NjktYzZhZC00OWUyLTg3NWItMTBhMjg0YjkzOTY3IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MjE5NzA3NDUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0yX0oxS0lzY3BoaCIsImNvZ25pdG86dXNlcm5hbWUiOiI5ZTg2OTgwNi02ZjY4LTQ4ZTYtYjc4ZS05OTgyNDAxMzcwMjciLCJleHAiOjE2MjE5ODUxNDUsImlhdCI6MTYyMTk3MDc0NSwiZW1haWwiOiJ1cmRhaWJheWNAZ21haWwuY29tIn0.lXjPu2bCb31CQoOj5MZvm-sy-nB616NdKNChrZc4nE532IIfsAd-kcgisnbLG6DSaV26JHKZIcS4lahkkPZyuqySt6kkVTv4LVtsy8gV7Tk3_2U3qNcapukk3l9hixx610wGjTUbwXQ1kuwYyYzf0fUAUfJ7JMAjYJXgP4fvxe0ancf3g93mpV83-Z-Dtb4NgCOblTrCdhFIQi77JJycSZw93J9cTY7gPu5S4tFXskddzJ1rJWyNa4aaRaJ9GP-P9vlrLc8elorMRtyqWZ0QW3LtnOXgDLVILGkPEVQlSaZgJVyD1Mk7Q3Hmv8Wzh4G_E6VX9v8DpyPpxZrW2svUdw'
    }
    candidatos = api_query(contest_id, auth_header)
    print(candidatos)
