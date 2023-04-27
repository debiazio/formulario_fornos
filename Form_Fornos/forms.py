from django import forms
from tempus_dominus.widgets import TimePicker
from datetime import datetime
from Form_Fornos.choices import *
from Form_Fornos.validation import *
#teste


#acaba teste
#cria os campos na página
class Form_FornosFormulario(forms.Form):
    NUM_PANELA = forms.IntegerField(label='NP (Número da panela)')
    HORA = forms.DateTimeField(label='Hora',widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}), initial=datetime.today)
    FORNO_FUSAO = forms.ChoiceField(label='Forno fusão', choices=tipos_forno, initial=1)
    #HORA = forms.TimeField(label='Hora', widget=TimePicker())    
    COMP_QUIMICA = forms.ChoiceField(label='Composição Química', choices=tipos_comp_quimica)
    TEMP_VAZ_ESPECIFICADO = forms.IntegerField(label='Temperatura vazamento especificado:')
    LIGA = forms.ChoiceField(label='Liga(AL)', choices=tipos_de_liga)
    #USUARIO = forms.CharField(label='Operador', disabled=True, initial=User.username)
    REL_MAQUINAS = forms.ChoiceField(label='Relação Máquinas', choices=relacao_das_maquinas)
    DENSIDADE_ESP = forms.IntegerField(label='Densidade Especificado: (conf. plano de controle)')
    TEMPERATURA = forms.IntegerField(label='Temp. | Após FDU | Min. 650ºC')
    FORNO_TORRE = forms.ChoiceField(label='Forno Torre', choices=tipos_forno, initial=1)
    N_P_TORRE = forms.IntegerField(label='NP (Número da panela)')
    MKR = forms.CharField(label='MKR')


    
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