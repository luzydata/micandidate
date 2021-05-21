import pandas as pd
import requests


##############################################################################
################## API BASE ##################################################
##############################################################################
BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'

def get_token():
    token=''
    print('--Getting token from file.')
    with open("token.txt") as fp:
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
    # token = get_token()
    # TODO: get_token WTF!!!!
    # This is hardcoded!!
    auth_header = {
        'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiY2lXaWNkendVcWl2WE5iVGg0WXNaQSIsInN1YiI6IjllODY5ODA2LTZmNjgtNDhlNi1iNzhlLTk5ODI0MDEzNzAyNyIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV2ZW50X2lkIjoiNzUyNGU5OWEtMjhjYS00NmRlLWI2Y2EtZWNmYzQ5M2E5OTU5IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MjE1NTY0MjcsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0yX0oxS0lzY3BoaCIsImNvZ25pdG86dXNlcm5hbWUiOiI5ZTg2OTgwNi02ZjY4LTQ4ZTYtYjc4ZS05OTgyNDAxMzcwMjciLCJleHAiOjE2MjE1NzA4MjcsImlhdCI6MTYyMTU1NjQyNywiZW1haWwiOiJ1cmRhaWJheWNAZ21haWwuY29tIn0.Bj5lMhjb0VOdMVsuvr1XWmLtjy7bkOVh69vjyb33FfpxBxZm95krv4kGsDv_ZqY6pVAIUHrwmPhAa_uClNhJA6GCOIyliTROnk9dikxUjm2QpxDYJchD5YFu6SNqGIDo-pNlEJSRCTrJhStJObgjmuTKQSr-Gms0j3kYf5Nk7cNDQ90UwMYheFhTJceZlYiQrWws-3WpZeRBil_-_KVYVxASolziz0-fzr7h9UjNPxGWoplB-Drp1Qeod5fsHOBXny4eKGxcPCgxA-5rSXws7BVQZcqLSbt-z9stGwVImPBNcRhvJlltQmYxwI_giyBlTNvyN5CBAT0-lp7e8qW7rg'
        }

    response = requests.get(BASE+str(endpoint)+'/'+str(value),
                            headers=auth_header,
                            verify=True,
                            timeout=None)

    return response.json()
    # print(jsonResponse)
    # print(jsonResponse["election_identifier"])
    # person_ids = jsonResponse["person_ids"]
