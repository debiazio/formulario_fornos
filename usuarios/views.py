from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages



def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        usuario= auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'Login de {nome} efetuado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login!')
            return redirect('login')
      
    return render(request, 'usuarios/login.html', {'form': form})




def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
           
            #coloca os valores em variáveis
            nome=form["nome_cadastro"].value()
            #email=form["email"].value()
            senha=form["senha_cadastro_1"].value()

            #valida se já tem nome de usuário criado no banco
            if User.objects.filter(username=nome).exists():
                messages.error(request, f"Usuário {nome} já existente")
                return redirect('cadastro')

            #grava/cria o usuario no banco
            usuario = User.objects.create_user(
                username=nome,
                #email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f"Cadastro de {nome} efetuado com sucesso!")
            return redirect('login')





    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)

    messages.success(request, "Usuário deslogado com sucesso!")
    return redirect('login')

