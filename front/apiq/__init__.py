import pandas as pd
import requests


##############################################################################
################## API BASE ##################################################
##############################################################################
BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'

def get_token():
    token=''
<<<<<<< HEAD
    # print('--Getting token.')
=======
    print('--Getting token from file.')
>>>>>>> 408e3fb8dacbb15c03f720519f52c2303d47912b
    with open("token.txt") as fp:
        token = fp.readlines()[0].strip()
    # print(token)
    return token


def querry_for(endpoint="area", value='0'):
    """
    area
    contest_id
    person
    membership
    party
    """
    # print('Running get_token.')
    auth_header = {'Authorization': str(get_token())}
    response = requests.get(BASE+str(endpoint)+'/'+str(value),
                            headers=auth_header,
                            verify=True,
                            timeout=None)
    # TODO: {'message': 'The incoming token has expired'}
    print(response.status_code)
    return response.json()
