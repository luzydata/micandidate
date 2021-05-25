# mi_candidate/core/api_query.py
import pandas as pd
import requests
import os


##############################################################################
################## API BASE ##################################################
##############################################################################
BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'
TOKEN = ''
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
    # token = get_token()
    # TODO: get_token WTF!!!!
    # This is hardcoded!!
    auth_header = {
        'Authorization': str(TOKEN)
        }

    response = requests.get(BASE+str(endpoint)+'/'+str(value),
                            headers=auth_header,
                            verify=True,
                            timeout=None)

    return response.json()


def get_dictionary():
    cwd = os.getcwd()
    print('Current working dir', cwd)
    move_to = input('moverse a cwd +')
    os.chdir(cwd+move_to)
    df = pd.read_csv('seccion_to_contest.csv')
    print(df.head(2))
    return df
