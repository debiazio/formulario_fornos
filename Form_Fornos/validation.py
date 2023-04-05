    
def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """valida se há caracters numéricos nos campos"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números nesse campo'