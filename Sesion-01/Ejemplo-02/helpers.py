def test_variables(globs):
    """ Prueba para Reto 01: lista de variables"""
    
    vars_1 = [
        "var_1",
        "variable_nueva_2",
        "Variable_nueva_3",
        "var_3_1",
        "varNueva4",
        "var_nuevaNumero",
        "var_num",
        "VarNum",
        "soyUnaVariable",
        "soyVariableDelAño"
    ]
    vars_2 = [
        "var_1",
        "variable_nueva_2",
        "Variable_nueva_3",
        "var_3_1",
        "varNueva4",
        "",
        "var_num",
        "",
        "soyUnaVariable",
        ""
    ]
    v = sum([v in globs for v in vars_1])
    if v == 0:
        print("""
        ERROR: Debes ejecutar primero la celda donde están
        definidas las variables!
        """)
        return
        
    sv = sum([(v in globs) != bool(vars_2[i]) for i, v in enumerate(vars_1)])
    if sv > 0:
        print(f"""
        ERROR: Hay {sv} variables erroneamente definidas,
        comenta o descomenta alguna e intenta de nuevo!
        """)
    else:
        print(f"""
        FELICIDADES!: Todas las variables definidas son correctas
        """)
    for v in vars_1:
        if v in globs:
            del globs[v]

def test_asignacion_variables(globals):
    """ Prueba para Reto-01: Asignación de variables """
    var_python = ['In', 'Out', 'get_ipython', 'exit', 'quit', 'helpers',
                  'test_variables', 'test_asignacion_variables']
    vars_1 = [
        "var_1",
        "variable_nueva_2",
        "Variable_nueva_3",
        "var_3_1",
        "varNueva4",
        "var_nuevaNumero",
        "var_num",
        "VarNum",
        "soyUnaVariable",
        "soyVariableDelAño"
    ]
    num_variables = 5  # Variables esperadas
    
    nvar = "variable_locochona"
    nval = 12345
    if nvar in globals and globals[nvar] == nval:
        num_variables -= 1
        del globals[nvar]
    else:
        print(f"Error: {nvar}")
    nvar = "var_decimal"
    nval = 14.567
    if nvar in globals and globals[nvar] == nval:
        num_variables -= 1
        del globals[nvar]
    else:
        print(f"Error: {nvar}")
    noms = [g for g in globals if not g.startswith("_") and
            g not in var_python and g not in vars_1]
    def es_variable_5_palabras(v):
        import re
        if re.search("^[a-z]+(_[a-z]+){3}_[a-z]+", v):
            return True
        if re.search("^[a-z][a-z]+([A-Z][a-z]+){4}", v):
            return True
        return False
    noms_5 = [n for n in noms if es_variable_5_palabras(n)]
    if noms_5:
        num_variables -= 1
        del globals[noms_5[0]]
        noms.remove(noms_5[0])
    else:
        print("Error: variable de 5 palabras")
    def es_variable_palabras_numeros(v):
        import re
        if re.search("^[a-z]+(_[a-z]+)+(_[0-9]+)+$", v):
            return True
        if re.search("^[a-z]+(?:[A-Z][a-z]+)+[0-9]+(?:_[0-9]+)+$", v):
            return True
        return False
    noms_palnums = [n for n in noms if es_variable_palabras_numeros(n)]
    if noms_palnums:
        num_variables -= 1
        del globals[noms_palnums[0]]
        noms.remove(noms_palnums[0])
    else:
        print("Error: variable de palabras y números")
    if noms:
        num_variables -= 1
        for nom in noms:
            del globals[nom]
        noms = []
    else:
        print("Error: variables a discreción")
        
    if num_variables > 0:
        print(f"""
        ERROR: Hay {num_variables} variables erroneamente definidas,
        revisa el nombre y el valor de cada variable, no olvides ejecutar
        la celda de las variables e intenta de nuevo!
        """)
    else:
        print(f"""
        FELICIDADES!: Todas las variables definidas son correctas
        """)
