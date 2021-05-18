from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from apiq import querry_for

app = Flask(__name__)
app.config['SECRET_KEY']= 'my_secret_key'

##############################################################################
################## FORM ######################################################
##############################################################################

class Consulta(FlaskForm):
    consulta = StringField('¿Qué area te gustaría consultar?', validators=[DataRequired()])
    submit = SubmitField('Informarse')


##############################################################################
################## ROUTES ####################################################
##############################################################################

@app.route('/', methods=['GET', 'POST'])
def index():
    print('Creando forma')
    form = Consulta()
    print('Validando forma')
    if form.validate_on_submit():
        session['consulta'] = form.consulta.data
        print('Valida')
        return redirect(url_for('resutado'))
    return render_template('index.html', form=form)

@app.route('/resutado')
def resutado():
    print('try output = querry_for()')
    try:
        output = querry_for()
    except:
        print('querry_for presented an error')
    finally:
        print(output)
        print('will pass to render_template')
    return render_template('resutado.html', output=output)

##############################################################################
################## CONSULTA API ##############################################
##############################################################################

if __name__ == '__main__':
    app.run(debug=True)
