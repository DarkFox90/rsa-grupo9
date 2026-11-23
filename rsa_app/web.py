from rsa_app.cifrado import encriptar, desencriptar


def con_comillas(texto):
    if len(texto) == 1:
        return '"' + texto + '" (1 carácter)'
    return '"' + texto + '" (' + str(len(texto)) + " caracteres)"


def ejecutar_encriptar(mensaje, texto_p, texto_q, texto_e):
    try:
        resultado = encriptar(mensaje, texto_p, texto_q, texto_e)
    except ValueError as error:
        return {"error": str(error), "resumen": "", "cifrado": "", "filas": []}

    if resultado["relleno"]:
        linea_relleno = 'Mensaje con relleno: "' + resultado["texto_con_relleno"] + '" (se agregó un espacio de relleno)'
    else:
        linea_relleno = "Relleno: No"

    lineas = [
        "Mensaje M: " + con_comillas(resultado["mensaje"]),
        "Longitud L: " + str(resultado["longitud"]),
        linea_relleno,
        "p = " + texto_p + "     q = " + texto_q + "     e = " + texto_e,
        "n = " + str(resultado["n"]) + "     φ = " + str(resultado["phi"]) + "     MCD(e, φ) = " + str(resultado["mcd"]),
        "Llave pública (e, n): (" + str(resultado["e"]) + ", " + str(resultado["n"]) + ")"
    ]
    return {"error": "", "resumen": "\n".join(lineas), "cifrado": resultado["cifrado"], "filas": resultado["filas"]}


def ejecutar_desencriptar(texto_c, texto_l, texto_p, texto_q, texto_e):
    try:
        resultado = desencriptar(texto_c, texto_l, texto_p, texto_q, texto_e)
    except ValueError as error:
        return {"error": str(error), "resumen": "", "filas": []}

    if resultado["relleno"]:
        linea_relleno = 'Mensaje con relleno: "' + resultado["texto_recuperado"] + '" (se quitó el espacio de relleno)'
    else:
        linea_relleno = "Relleno: No"

    lineas = [
        "Mensaje recuperado: " + con_comillas(resultado["mensaje"]),
        "Longitud L: " + str(resultado["longitud"]),
        linea_relleno,
        "p = " + texto_p + "     q = " + texto_q + "     e = " + texto_e,
        "n = " + str(resultado["n"]) + "     φ = " + str(resultado["phi"]) + "     d = " + str(resultado["d"]),
        "Llave privada (d, n): (" + str(resultado["d"]) + ", " + str(resultado["n"]) + ")"
    ]
    return {"error": "", "resumen": "\n".join(lineas), "filas": resultado["filas"]}
