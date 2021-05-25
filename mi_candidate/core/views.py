# mi_candidate/core/views
from flask import render_template, url_for, redirect, request, Blueprint, session
from mi_candidate.core.forms import ConsultaForm
from mi_candidate.core import api_query


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
    contest_id = str(149)
    auth_header = {
            	'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiU0NhMEpaZ2VsVGVOcjZ6R1lNcG9OUSIsInN1YiI6IjllODY5ODA2LTZmNjgtNDhlNi1iNzhlLTk5ODI0MDEzNzAyNyIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV2ZW50X2lkIjoiZmIxZDBhYWQtYTA5NS00MDdiLTgzY2UtMjA4ODg5NDA1YThhIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MjE5NTE1ODksImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0yX0oxS0lzY3BoaCIsImNvZ25pdG86dXNlcm5hbWUiOiI5ZTg2OTgwNi02ZjY4LTQ4ZTYtYjc4ZS05OTgyNDAxMzcwMjciLCJleHAiOjE2MjE5NjU5ODksImlhdCI6MTYyMTk1MTU4OSwiZW1haWwiOiJ1cmRhaWJheWNAZ21haWwuY29tIn0.PxB2ZArxklByLKzMTHpI0Dj7DlbyleZRP1jfa1zsjKROFVe9bfeeH3YUN93Jq5_5YKPYJY5kLKqyR50lBl01yWAUfNx2ehApDIvPKsW10-T581SggohCXGrPcb2Mwjw--EtxeLOOaUiW3v6DdddZlvAjQ-c4OeaLQUYoPUlza7kstqE77kbLML3B_tnGiBOvN2ZxZcVLSxARkOOBBgBe8uF2Kjagt0QCPyIwMSDMu6o9a8d8ffYitWVPKRfmPPUVJH7wCQNDA2ulE_6X1ugcTaV0tZy7CwgZ0Ehh--DFrB4H2RddeE3KhQwrtSXoq9cnCkFfP6rCt-udcexhKwsgVA'
            }
    if form.validate_on_submit():
        session['estado'] = form.estado.data
        session['area_electoral'] = form.area_electoral.data
        session['api_response'] = api_query(
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
