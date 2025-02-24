
# Translator

# Instalar las librerías necesarias
# pip install translate

# Importar la librería necesaria
from translate import Translator  # Módulo para traducción automática

# Crear un objeto Translator para traducir del español al inglés
translator = Translator(from_lang='spanish', to_lang='english')

# Pedir al usuario que ingrese el texto a traducir
txt = input('¿Qué quieres traducir? ')

# Traducir el texto ingresado
res = translator.translate(txt)

# Imprimir el resultado traducido
print(res)

