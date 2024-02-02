from django import forms
from .models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD
#UD7.5.b y UD7.5.c
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Column, Row
from django.core.exceptions import ValidationError

#UD7.3.a

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['codigo', 'nombre']
    #UD7.5.b y UD7.5.c
    def __init__(self, *args, **kwargs):
        super(UnidadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            #UD7.5.d
            Row(
                Column('codigo', css_class='col-2'),
                Column('nombre')
            ),
        )

class InstEvaluacionForm(forms.ModelForm):
    class Meta:
        model = InstEvaluacion
        fields = ['codigo', 'nombre', 'descripcion']
    #UD7.5.b y UD7.5.c
    def __init__(self, *args, **kwargs):
        super(InstEvaluacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            #UD7.5.d
            Row(
                Column('codigo', css_class='col-3'),
                Column('nombre')
            ),
            Row(
                Column('descripcion')
            )
        )

class PondRAForm(forms.ModelForm):
    class Meta:
        model = PondRA
        fields = ['resultado_aprendizaje', 'porcentaje']
    #UD7.3.b
    def clean_porcentaje(self):
        porcentaje = self.cleaned_data['porcentaje']
        if (porcentaje < 0 or porcentaje > 100):
            raise ValidationError("El porcentaje no puede ser mayor a 100 ni menor que 0")
        return porcentaje
    #UD7.5.b y UD7.5.c
    def __init__(self, *args, **kwargs):
        super(PondRAForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            #UD7.5.d
            Row(
                Column('resultado_aprendizaje', css_class='col-9'),
                Column('porcentaje')
            ),
        )

class PondCriterioForm(forms.ModelForm):
    class Meta:
        model = PondCriterio
        fields = ['criterio_evaluacion', 'porcentaje']
    #UD7.3.b
    def clean_porcentaje(self):
        porcentaje = self.cleaned_data['porcentaje']
        if (porcentaje < 0 or porcentaje > 100):
            raise ValidationError("El porcentaje no puede ser mayor a 100 ni menor que 0")
        return porcentaje
    #UD7.5.b y UD7.5.c
    def __init__(self, *args, **kwargs):
        super(PondCriterioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            #UD7.5.d
            Row(
                Column('criterio_evaluacion', css_class='col-9'),
                Column('porcentaje')
            )
        )

class PondCritUDForm(forms.ModelForm):
    class Meta:
        model = PondCritUD
        fields = ['criterio_evaluacion', 'unidad', 'porcentaje']
    #UD7.3.b
    def clean_porcentaje(self):
        porcentaje = self.cleaned_data['porcentaje']
        if (porcentaje < 0 or porcentaje > 100):
            raise ValidationError("El porcentaje no puede ser mayor a 100 ni menor que 0")
        return porcentaje
    #UD7.5.b y UD7.5.c
    def __init__(self, *args, **kwargs):
        super(PondCritUDForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        self.helper.layout = Layout(
            #UD7.5.d
            Row(
                Column('criterio_evaluacion'),
            ),
            Row(
                Column('unidad', css_class='col-9'),
                Column('porcentaje')
            )
        )