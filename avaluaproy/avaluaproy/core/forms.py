from django import forms
from .models import Modulo, ResAprendizaje, CritEvaluacion
#UD7.5.b y UD7.5.c
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Column, Row

#UD7.3.a

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['codigo', 'nombre']
    #UD7.5.b y UD7.5.c
    def __init__(self, *args, **kwargs):
        super(ModuloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            #UD7.5.d
            Row(
                Column('codigo' , css_class='col-3'),
                Column('nombre')
            )
        )
        



class ResAprendizajeForm(forms.ModelForm):
    class Meta:
        model = ResAprendizaje
        fields = ['modulo', 'codigo', 'descripcion']
    #UD7.5.b y UD7.5.c
    def __init__(self, *args, **kwargs):
        super(ResAprendizajeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            #UD7.5.d
            Row(
                Column('modulo', css_class='col-3'),
                Column('codigo'),
            ),
            Row(
                Column('descripcion')
            )
        )


class CritEvaluacionForm(forms.ModelForm):
    class Meta:
        model = CritEvaluacion
        fields = ['resultado_aprendizaje', 'codigo', 'descripcion', 'minimo']
    #UD7.5.b y UD7.5.c
    def __init__(self, *args, **kwargs):
        super(CritEvaluacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            #UD7.5.d
            Row(
                Column('resultado_aprendizaje')                
            ),
            Row(
                Column('codigo'),
                Column('minimo', css_class='col-3')
            ),
            Row(
                Column('descripcion')                
            ),
        )