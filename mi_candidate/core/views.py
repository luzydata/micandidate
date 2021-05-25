# mi_candidate/core/views
from flask import render_template, url_for, redirect, request, Blueprint, session
from mi_candidate.core.forms import ConsultaForm
from mi_candidate.core import api_query, get_contest_id


core = Blueprint('core', __name__)

##############################################################################
################## ROUTES ####################################################
##############################################################################
##############################
###### HOME ##################
##############################

@core.route('/', methods=['GET', 'POST'])
def index():
    form = ConsultaForm()
    auth_header = {
            	'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiWnEySWlra0M2Umw2TThXUnJqQUFYUSIsInN1YiI6IjllODY5ODA2LTZmNjgtNDhlNi1iNzhlLTk5ODI0MDEzNzAyNyIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV2ZW50X2lkIjoiYjBlYjM3NjktYzZhZC00OWUyLTg3NWItMTBhMjg0YjkzOTY3IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MjE5NzA3NDUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0yX0oxS0lzY3BoaCIsImNvZ25pdG86dXNlcm5hbWUiOiI5ZTg2OTgwNi02ZjY4LTQ4ZTYtYjc4ZS05OTgyNDAxMzcwMjciLCJleHAiOjE2MjE5ODUxNDUsImlhdCI6MTYyMTk3MDc0NSwiZW1haWwiOiJ1cmRhaWJheWNAZ21haWwuY29tIn0.lXjPu2bCb31CQoOj5MZvm-sy-nB616NdKNChrZc4nE532IIfsAd-kcgisnbLG6DSaV26JHKZIcS4lahkkPZyuqySt6kkVTv4LVtsy8gV7Tk3_2U3qNcapukk3l9hixx610wGjTUbwXQ1kuwYyYzf0fUAUfJ7JMAjYJXgP4fvxe0ancf3g93mpV83-Z-Dtb4NgCOblTrCdhFIQi77JJycSZw93J9cTY7gPu5S4tFXskddzJ1rJWyNa4aaRaJ9GP-P9vlrLc8elorMRtyqWZ0QW3LtnOXgDLVILGkPEVQlSaZgJVyD1Mk7Q3Hmv8Wzh4G_E6VX9v8DpyPpxZrW2svUdw'
            }


    if form.validate_on_submit():
        session['estado'] = form.estado.data
        session['area_electoral'] = int(form.area_electoral.data)
        contest_id = get_contest_id(session['area_electoral'])
        session['candidatos'] = api_query(
                                        contest_id,
                                        auth_header,
                                        )

        return redirect(url_for('core.info'))
    return render_template(
                            'index.html',
                            form=form
                            )


##############################
###### RESULTS ###############
##############################
@core.route('/info')
def info():

    return render_template('info.html')
