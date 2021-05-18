# -*- coding: utf-8 -*-
"""mi_candidate_0.1_210514.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/luzydata/micandidate/blob/main/mi_candidate_0_1_210514.ipynb
"""

import requests
import pandas as pd

BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'

auth_header = {
	'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiTDBIWkpqUTN5VjNTU2hJRlBZdlhYZyIsInN1YiI6IjllODY5ODA2LTZmNjgtNDhlNi1iNzhlLTk5ODI0MDEzNzAyNyIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjIxMzIxOTM4LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9KMUtJc2NwaGgiLCJjb2duaXRvOnVzZXJuYW1lIjoiOWU4Njk4MDYtNmY2OC00OGU2LWI3OGUtOTk4MjQwMTM3MDI3IiwiZXhwIjoxNjIxMzM2MzM4LCJpYXQiOjE2MjEzMjE5MzgsImVtYWlsIjoidXJkYWliYXljQGdtYWlsLmNvbSJ9.HYHU7vgIhwxsIj-mxw8h1fbMzq39fipQMURVRlAAeCboyJptZMbgWPUmorzq41uqqLYZ68xbCnzrXY4PGg9RZPS5KPu0zy1T1IjVA7nPwUyZBo21yBXmyNg-bkUZJncfKVZ3mL0bHEndbULmb8Zlx5QMBwmhCEPRmAde0sOjPgDQFFuNkKzcm_IXH2-T2mrmuzO-5PCv6DNQjS3fDtxYq1Dy7-K7OEdhmVxHTl1QYKGi7Ho1JPb9LZ-9ePqWsYac7sCm_axYGR7D50xSk3DjMWCaQfisKycy6z4pMcF7bwW4NDKiPjfVXh1CQO9OJNPjezdLDOzNrHjsGI617Ttaag'
}

print('-----------------------------------------------------------------------')
print('Getting areas')
response = requests.get(BASE + 'area', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
# print('Getting an area')
# response = requests.get(BASE + 'area/123', headers=auth_header, verify=True,  timeout=None)
# print(response.json())
# print('-----------------------------------------------------------------------')
#