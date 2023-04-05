from django import forms
from tempus_dominus.widgets import TimePicker
from datetime import datetime
from Form_Fornos.choices import *
from Form_Fornos.validation import *

class Form_FornosFormulario(forms.Form):
    NUM_PANELA = forms.IntegerField(label='NP (Número da panela)')
    FORNO_FUSAO = forms.CharField(label='Forno Fusão', max_length=50)
    hora = forms.TimeField(label='Hora', widget=TimePicker())
    data_registro = forms.DateField(label='Data do acompanhamento', disabled=True, initial=datetime.today)
    compos_quimica = forms.ChoiceField(label='Composição Química', choices=tipos_comp_quimica)
    liga = forms.ChoiceField(label='Liga(AL)', choices=tipos_de_liga)


    
    def clean(self):
        """clean valida os campos"""
        FORNO_FUSAO = self.cleaned_data.get('FORNO_FUSAO')
        #NUM_PANELA = self.cleaned_data.get('NUM_PANELA')
        lista_de_erros = {}
        campo_tem_algum_numero(FORNO_FUSAO, 'FORNO_FUSAO', lista_de_erros)
        #campo_tem_algum_numero(NUM_PANELA, 'NUM_PANELA', lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data