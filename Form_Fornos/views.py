from django.shortcuts import render, redirect
from Form_Fornos.forms import Form_FornosFormulario
import pyodbc
from Form_Fornos.models import InsertedData
from django.contrib import messages




def index(request):
    #se usuário não estiver autenticado será redirecionado para o login
    if not request.user.is_authenticated:
        messages.error(request, "Para acessar essa página é necessário realizar login!")
        return redirect('login')  
    
    
    form = Form_FornosFormulario()
    contexto = {'form':form}
    return render(request, 'formulario/index.html', contexto)

#conecta com o banco
def saverecords(request):
    conn = pyodbc.connect(
        "Driver={Sql Server};"
        "Server=**********;"
        "DataBase=*******;"
        "uid=******;"
        "pwd=**********"
    )
    if request.method == 'POST':
        form = Form_FornosFormulario(request.POST)

        
        #valida o formulario antes de enviar para contexto
        if request.POST.get("NUM_PANELA") and request.POST.get("FORNO_FUSAO"):
            insertsvalues = InsertedData()
            insertsvalues.NUM_PANELA = request.POST.get("NUM_PANELA")
            insertsvalues.FORNO_FUSAO = request.POST.get("FORNO_FUSAO")
            insertsvalues.HORA = request.POST.get("HORA")
            insertsvalues.COMP_QUIMICA = request.POST.get("COMP_QUIMICA")
            insertsvalues.TEMP_VAZ_ESPECIFICADO = request.POST.get("TEMP_VAZ_ESPECIFICADO")
            insertsvalues.LIGA = request.POST.get("LIGA")
            insertsvalues.REL_MAQUINAS = request.POST.get("REL_MAQUINAS")
            insertsvalues.DENSIDADE_ESP = request.POST.get("DENSIDADE_ESP")
            insertsvalues.TEMPERATURA = request.POST.get("TEMPERATURA")
            insertsvalues.FORNO_TORRE = request.POST.get("FORNO_TORRE")
            insertsvalues.N_P_TORRE = request.POST.get("N_P_TORRE")
            insertsvalues.MKR = request.POST.get("MKR")
            
            cursor = conn.cursor()
            cursor.execute(
            "insert into CST_ACOMPANHAMENTO_FORNOS (NUM_PANELA, FORNO_FUSAO, HORA, COMP_QUIMICA, TEMP_VAZ_ESPECIFICADO, LIGA, REL_MAQUINAS, DENSIDADE_ESP, TEMPERATURA, FORNO_TORRE, N_P_TORRE, MKR) values('"
            + insertsvalues.NUM_PANELA
            + "','"
            + insertsvalues.FORNO_FUSAO
            + "','"
            + insertsvalues.HORA
            + "','"
            + insertsvalues.COMP_QUIMICA
            + "','"
            + insertsvalues.TEMP_VAZ_ESPECIFICADO
            + "','"
            + insertsvalues.LIGA
            + "','"
            + insertsvalues.REL_MAQUINAS
            + "','"
            + insertsvalues.DENSIDADE_ESP
            + "','"
            + insertsvalues.TEMPERATURA
            + "','"
            + insertsvalues.FORNO_TORRE
            + "','"
            + insertsvalues.N_P_TORRE
            + "','"
            + insertsvalues.MKR
            + "')"
            )
            cursor.commit()



            contexto = {'form':form}
            return render(request, 'formulario/minha_consulta.html', contexto)
        else:
            print('form inválido')
            #se não for válido envia novamente para a pagina de registro
            contexto = {'form':form}
            return render(request, 'formulario/index.html', contexto)
        
        
