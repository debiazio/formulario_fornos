from django.shortcuts import render
from Form_Fornos.forms import Form_FornosFormulario

def index(request):
    form = Form_FornosFormulario()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = Form_FornosFormulario(request.POST)
        #valida o formulario antes de enviar para contexto
        if form.is_valid():
            contexto = {'form':form}
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('form inválido')
            #se não for válido envia novamente para a pagina de registro
            contexto = {'form':form}
            return render(request, 'index.html', contexto)