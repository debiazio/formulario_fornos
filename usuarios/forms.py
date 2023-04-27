#import da biblioteca de formulario do Django
from django import forms

#Classe para inserção dos campos para efetuar o login
class LoginForms(forms.Form):
    #campo de inserção de usuário 
    nome_login=forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )

    )
    #campo de inserção de senha
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

#Classe para criação dos compos de cadastro
class CadastroForms(forms.Form):
    #cria o campo para inserir o nome de usuário
    nome_cadastro=forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao.silva"
            }
        )
    )
    #campo email - removido pois no caso dos Fornos, acredito que não será útil, validar com José 
    """     
        email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@seuemail.com"
            }
        )
    ) """
    #campo da senha
    senha_cadastro_1=forms.CharField(
                label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    #campo para repetir a senha
    senha_cadastro_2=forms.CharField(
                label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    #valida se o nome do cadastro tem alguma espaço em branco.
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é permitido inserir espaços no campo de nome de usuário!")
            else:
                return nome

    #valida se as senhas coincidem, caso não aparece mensagem de erro abaixo dos campos      
    def clean_senha_cadastro_2(self):
        senha_cadastro_1 = self.cleaned_data.get('senha_cadastro_1')
        senha_cadastro_2 = self.cleaned_data.get('senha_cadastro_2')

        if senha_cadastro_1 and senha_cadastro_2:
            if senha_cadastro_1 != senha_cadastro_2:
                raise forms.ValidationError('As senhas não são iguais!')
            else:
                return senha_cadastro_2