# Criptografía RSA (versión web)

Proyecto del curso MM2015 Matemática Discreta 1, Universidad del Valle de Guatemala.

Autores: Carlos Pozuelos Mendizabal (25104) y Andrés Castro Morales (25039).

Esta es la versión web del proyecto, para usarlo desde el navegador sin instalar nada. La página corre el mismo código de Python que la versión de escritorio, dentro del navegador, con Pyodide (Python 3.14). La primera vez tarda unos segundos en cargar.

## Archivos

- `index.html`: la página, con las pestañas Encriptar y Desencriptar.
- `rsa_app/logica.py`, `rsa_app/codificacion.py`, `rsa_app/validacion.py` y `rsa_app/cifrado.py`: los mismos archivos de la versión de escritorio, sin cambios.
- `rsa_app/web.py`: arma el resumen que muestra la página, igual que las pestañas de la versión de escritorio.

Los tres algoritmos matemáticos están en `rsa_app/logica.py`:

- MCD: `mcd_euclides(a, b)`, con el algoritmo de Euclides.
- Inverso modular: `inverso_modular(a, m)`, que usa `bezout_matricial(a, b)`.
- Exponenciación modular: `exponenciacion_modular(b, e, n)`, con su función interna `mpower`.

## Ejemplo

Encriptar M = "RSA" con p = 367, q = 373 y e = 17 da C = 026054 123875 y L = 3. Al desencriptar C con L = 3 y los mismos p, q y e se obtiene d = 8009 y el mensaje "RSA".
