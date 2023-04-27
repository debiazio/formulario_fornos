# Cria as categorias para selecionar no campo Composição Química
tupla_tipos_comp_quimica = {
    (1, 'Ok'),
    (2, 'Não OK')
}
#ordena do menor para o maior
tipos_comp_quimica = sorted(tupla_tipos_comp_quimica, key=lambda x:x[0])

# Cria as categorias para selecionar no campo Liga(AL)
tupla_tipos_de_liga = {
    (1, '2'),
    (2, '3'),
    (3, '4')
}
#ordena do menor para o maior
tipos_de_liga = sorted(tupla_tipos_de_liga, key=lambda x:x[0])

tupla_forno = {
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, 'Sklenar')
}
#ordena do menor para o maior
tipos_forno  = sorted(tupla_forno, key=lambda x:x[0])

rel_maquinas = {
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20),
    (21, 21),
    (22, 22),
    (23, 23)
}
#ordena do menor para o maior
relacao_das_maquinas = sorted(rel_maquinas, key=lambda x: x[0])