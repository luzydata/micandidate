import os
import requests
#import pandas as pd

def get_contest_id(area_electoral):
    clave_electoral = pd.read_csv('/content/seccion_to_contest.csv')
    clave_electoral.drop(['ENTIDAD', 'NOMBRE ENTIDAD', 'DISTRITO', 'DISTRITO LOCAL', 'MUNICIPIO'],axis=1, inplace=True)
    clave_electoral.set_index("SECCION", inplace=True)
    contest_id = clave_electoral.loc[sec].values[0]


def api_query(contest_id, auth_header):

    # request the contest to the api
    BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'
    response = requests.get(BASE + f'contest/{contest_id}', headers=auth_header, verify=True,  timeout=None)
    contest = response.json()
    candidatos = []
    print(contest.items())
    for candidato in contest['person_ids']:
        response = requests.get(BASE + 'person/'+str(candidato), headers=auth_header, verify=True,  timeout=None)
        candidato = response.json()
        candidatos.append(candidato)

    return candidatos


if __name__ == '__main__':
    area_electoral = 10
    contest_id=get_contest_id(area_electoral)
    print(contest_id)
    # auth_header = {
    # 	'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiU0NhMEpaZ2VsVGVOcjZ6R1lNcG9OUSIsInN1YiI6IjllODY5ODA2LTZmNjgtNDhlNi1iNzhlLTk5ODI0MDEzNzAyNyIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV2ZW50X2lkIjoiZmIxZDBhYWQtYTA5NS00MDdiLTgzY2UtMjA4ODg5NDA1YThhIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MjE5NTE1ODksImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0yX0oxS0lzY3BoaCIsImNvZ25pdG86dXNlcm5hbWUiOiI5ZTg2OTgwNi02ZjY4LTQ4ZTYtYjc4ZS05OTgyNDAxMzcwMjciLCJleHAiOjE2MjE5NjU5ODksImlhdCI6MTYyMTk1MTU4OSwiZW1haWwiOiJ1cmRhaWJheWNAZ21haWwuY29tIn0.PxB2ZArxklByLKzMTHpI0Dj7DlbyleZRP1jfa1zsjKROFVe9bfeeH3YUN93Jq5_5YKPYJY5kLKqyR50lBl01yWAUfNx2ehApDIvPKsW10-T581SggohCXGrPcb2Mwjw--EtxeLOOaUiW3v6DdddZlvAjQ-c4OeaLQUYoPUlza7kstqE77kbLML3B_tnGiBOvN2ZxZcVLSxARkOOBBgBe8uF2Kjagt0QCPyIwMSDMu6o9a8d8ffYitWVPKRfmPPUVJH7wCQNDA2ulE_6X1ugcTaV0tZy7CwgZ0Ehh--DFrB4H2RddeE3KhQwrtSXoq9cnCkFfP6rCt-udcexhKwsgVA'
    # }
    # candidatos = api_query(contest_id, auth_header)
