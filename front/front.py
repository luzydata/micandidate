from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from apiq import get_local_data, query_for, get_persons

app = Flask(__name__)
app.config['SECRET_KEY']= 'my_secret_key'

##############################################################################
################## FORM ######################################################
##############################################################################

class Consulta(FlaskForm):
    consulta = StringField('¿Qué CONTEST te gustaría consultar? ', validators=[DataRequired()])
    submit = SubmitField('Informarse')


##############################################################################
################## ROUTES ####################################################
##############################################################################

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Consulta()
    if form.validate_on_submit():
        session['consulta'] = form.consulta.data
        return redirect(url_for('resutado'))
    return render_template('index.html', form=form)

##############################
###### CONSULTA API ##########
##############################
@app.route('/resultado')
def resutado():
    token, df = get_local_data()
    contest = query_for(token, "contest", session['consulta'])
    persons = get_persons(token, contest)
    

    output = []
    output = [contest, persons]
    return render_template('resultado.html', output=output)


if __name__ == '__main__':
    app.run(debug=True)
