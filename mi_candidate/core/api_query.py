# mi_candidate/core/api_query.py
import pandas as pd
import requests
import os


##############################################################################
################## API BASE ##################################################
##############################################################################
BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'


basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

def query_for(endpoint="area", value='0'):
    """
    querry_for makes a request to the specified API endpoint using the specified
    endpoint and value. Requires the uder token to create the auth_header.
    area
    contest_id
    person
    membership
    party
    """
    auth_header = {
        'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoibVZzX2pXLVh4TW5oczloTjhwanB2ZyIsInN1YiI6IjllODY5ODA2LTZmNjgtNDhlNi1iNzhlLTk5ODI0MDEzNzAyNyIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjIxOTM2MjI3LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9KMUtJc2NwaGgiLCJjb2duaXRvOnVzZXJuYW1lIjoiOWU4Njk4MDYtNmY2OC00OGU2LWI3OGUtOTk4MjQwMTM3MDI3IiwiZXhwIjoxNjIxOTUwNjI3LCJpYXQiOjE2MjE5MzYyMjcsImVtYWlsIjoidXJkYWliYXljQGdtYWlsLmNvbSJ9.U9tHIZ92--O72VCz3pSTpS8k_f_u-KTBwAMrJYXCfaoUEtBuB35soz0Zoq0CfF2XpitBQhfDZNU-XiCYKfkmc1iPZX1_jUZoWJ30oWm2N0Fjl-RBPaLDGD5cT8Yu4Sm4wDGCi-D8gsBOvbU6FFQDgoK3BdOG8Zin5c5Dm5P_J18Hb91MxBSUXynKZjB4QAfmEWwiEHZHzvhTbSpGkQFoWpxqAYiYVE8dmMlc5Tp8-7LhKSxsNPkIXNbhED9NnPd949tSQ0HQ6A3LsFRV_ZsAfxdqheCrNCTwzqaCmdAnpPuA0Z4JY10n1BW_ZYibFxFzQbEQaueq3em16a2fcpYh5Q'
        }

    response = requests.get(BASE+str(endpoint)+'/'+str(value),
                            headers=auth_header,
                            verify=True,
                            timeout=None)

    return response.json()

#
# def get_dictionary():
#     cwd = os.getcwd()
#     print('Current working dir', cwd)
#     move_to = input('moverse a cwd +')
#     os.chdir(cwd+move_to)
#     df = pd.read_csv('seccion_to_contest.csv')
#     print(df.head(2))
#     return df
if __name__ == '__main__':
    print(query_for(endpoint='contest_id', value=1))
