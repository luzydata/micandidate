# mi_candidate/core/forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError


##############################
###### USER QUERY ############
##############################
class ConsultaForm(FlaskForm):
    consulta = StringField('Introduce tu área electoral: ', validators=[DataRequired()])
    submit = SubmitField('Informarse')
