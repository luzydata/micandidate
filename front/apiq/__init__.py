import pandas as pd
import requests
import os


##############################################################################
################## API BASE ##################################################
##############################################################################
BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'
def move(directory=''):
    current_dir = os.getcwd()
    if directory != '':
        os.chdir(current_dir + directory)
    else:
        move_to = input('Where to move?')
        os.chdir(current_dir + move_to)

def get_local_data():
    move('/apiq/')
    token=''
    with open("token.txt") as fp:
        token = fp.readlines()[0].strip()
    print(token)
    df = pd.read_csv('seccion_to_contest.csv')
    move('/../')
    return token, df

def query_for(token, endpoint="contest", value='1'):
    # print('Running get_token.')
    auth_header = {'Authorization': str(token)}
    response = requests.get(BASE+str(endpoint)+'/'+str(value),
                            headers=auth_header,
                            verify=True,
                            timeout=None)
    # TODO: {'message': 'The incoming token has expired'}
    # TODO: handle status codes
    print(response.status_code)
    if response.status_code != 200:
        print('no ok response =//')
    else:
        return response.json()

def get_persons(token, contest):
    persons = contest['person_ids']
    my_out = []
    for person in persons:
        my_out.append(query_for(token, 'person', person))
    return my_out

if __name__ == '__main__':
    token, df = get_local_data()
    x = query_for(token, "contest", 1)
    print(get_persons(token, x))
