from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']= 'my_secret_key'

##############################################################################
################## FORM ######################################################
##############################################################################

class Consulta(FlaskForm):
    consulta = StringField('Cual es la clave electoral', validators=[DataRequired()])
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

@app.route('/resutado')
def resutado():
    return render_template('resutado.html')

##############################################################################
################## CONSULTA API ##############################################
##############################################################################

if __name__ == '__main__':
    app.run(debug=True)
