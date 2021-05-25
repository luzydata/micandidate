# mi_candidate/core/views
from flask import render_template, url_for, redirect, request, Blueprint, session
from mi_candidate.core.forms import ConsultaForm
from mi_candidate.core.api_query import query_for


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
    if form.validate_on_submit():
        session['consulta'] = form.consulta.data
        session['api_response'] = query_for(endpoint='contest_id', value= session['consulta'])

        return redirect(url_for('core.info'))
    return render_template('index.html', form=form)


##############################
###### RESULTS ###############
##############################
@core.route('/info')
def info():
    # df = get_dictionary()
    # search = session['area_electoral']
    # to_query = df.loc[df.SECCION == int(search)]['Contest_id'].values[0]
    # res = querry_for('contest', to_query)
    return render_template('info.html')
