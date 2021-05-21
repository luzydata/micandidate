from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from apiq import querry_for, get_dictionary


app = Flask(__name__)
app.config['SECRET_KEY']= 'my_secret_key'
df = get_dictionary()

##############################################################################
################## FORM ######################################################
##############################################################################

class Consulta(FlaskForm):
    consulta = StringField('Introduce tu área electoral: ', validators=[DataRequired()])
    submit = SubmitField('Informarse')


##############################################################################
################## ROUTES ####################################################
##############################################################################

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Consulta()
    if form.validate_on_submit():
        session['area_electoral'] = form.consulta.data
        return redirect(url_for('resutado'))
    return render_template('index.html', form=form)

##############################
###### CONSULTA API ##########
##############################
@app.route('/resutado')
def resutado():
    # TODO: mover diccionario

    search = session['area_electoral']
    to_query = df.loc[df.SECCION == int(search)]['Contest_id'].values[0]
    res = querry_for('contest', to_query)
    return render_template('resutado.html', output=res)


if __name__ == '__main__':
    app.run(debug=True)
