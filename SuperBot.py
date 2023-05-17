# Archivo .py que contiene el API
from config import * 

# Importamos TeleBot, librería que nos ayuda a configurar nuestro bot 
import telebot 

from Recurrencias import RelacionesDeRecurrencia



#----------------------------------------

# CONFIGURACIÓN DEL BOT

#---------------------------------------


# Asignamos el API a una variable llamada bot

bot=telebot.TeleBot(TELEGRAM_TOKEN) 

# Mensaje de bienvenida y menú.

intro ="""  Bienvenido, mi nombre es SuperBot🤖. \n \n¿En que te puedo servir?😎 
 \nTengo distintas funciones 🔧 como: \n/Estrellas: Mostrar un gráfico de todas las estrellas🌟 
 \n/EyC: Mostrar un gráfico de todas las estrellas🌟 y una constelación🌌 en particular. 
 \n/Constelaciones: Mostrar todas las estrellas🌟 y constelaciones🌌🌌
 \n/Recurrencia Hallar la solución de una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.
\n \nPara escoger una opción, ingrese el número"""


ayuda = """  Hola!!!🤖🤖
Para escoger alguna opción ingresa alguno de los comandos 🔧: 
\n 1.Mostrar un gráfico de todas las estrellas🌟 
\n comando: /Estrellas
\n2.Mostrar un gráfico de todas las estrellas🌟 y una constelación🌌 en particular. 
\n comando: /EyC
\n3.Mostrar todas las estrellas🌟 y constelaciones🌌🌌
\n comando: /Constelaciones
\n4.Hallar la solución de una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.
\n comando: /Recurrencia
\n \nPara escoger una opción, ingrese el comando"""
# Usamos decoradores, estas reciben parámetros de otras funciones y retorna distintos resultados (Reusar código)
# Los comandos a utilizar son /start, /help, /ayuda. Creamos la función

@bot.message_handler(commands=["start", "inicio"])
def cmd_start(message):

    # Lo que el bot nos va a responder cuando ingrese /start

    bot.reply_to(message, intro)

# Cuando ingrese el comando /ayuda o /help
@bot.message_handler(commands=["help", "ayuda"])
def help(message):
    # Lo que el bot nos va a responder cuando ingrese 
    bot.reply_to(message, ayuda)

# Si escoge la opción de Mostrar un gráfico de todas las estrellas y una constelación

@bot.message_handler(commands=['EyC'])
def EyC(message):
    def Constelacion(message):
        if message.text == '/start':
            bot.send_message(message.chat.id, 'Redirigiendote al menú de inicio...')
            bot.send_message(message.chat.id, intro)
            return
        try:
            imagen = ImagenABit(message.text[1:])
            
            bot.send_photo(message.chat.id, imagen)
        except:
            bot.send_message(message.chat.id, 'La constelación que intentas ingresar no la puedo leer 😔 \nPor favor inténtalo de nuevo o escoge /start para volver al menú')
            bot.register_next_step_handler(message, Constelacion)
    
    texto = """Tu acabas de escoger la opción EyC 🌠🌠
    \n➡️ Mostrar todas las estrellas y una constelación en particular.
    \nAhora te vamos a pedir que escojas la constelación que quieras😄:
- /Boyero
- /Casiopea
- /Cazo
- /Cygnet
- /Geminis
- /Hydra
- /OsaMayor
- /OsaMenor

Presiona el comando de la que desees ☄"""

    bot.send_message(message.chat.id, texto)
    bot.register_next_step_handler(message, Constelacion)


# Si escoge la opción de Mostrar un gráfico de todas las estrellas🌟

@bot.message_handler(commands=["Estrellas"])
def Estrellas(message):
    imagen = ImagenABit('Estrellas')
    bot.send_photo(message.chat.id, imagen)

# Si escoge Mostrar todas las estrellas🌟 y constelaciones🌌🌌

@bot.message_handler(commands=["Constelaciones"])
def Constelaciones(message):
    imagen = ImagenABit('Constelaciones')
    bot.send_photo(message.chat.id, imagen)

# Si escoge solucionar una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.

@bot.message_handler(commands=["Recurrencia"])
def Recurrencia(message):
    def ObtenerRecurrencia(m):
        recurrencia = m.text
        if recurrencia == '/start':
            bot.send_message(message.chat.id, 'Redirigiendote al menú de inicio...')
            bot.send_message(message.chat.id, intro)
            return
        try:
            fn = RelacionesDeRecurrencia(recurrencia)
            bot.send_photo(message.chat.id, fn)                
        except: 
            bot.send_message(message.chat.id, 'La relación de recurrencia que intentas ingresar no la puedo leer 😔 \nPor favor inténtalo de nuevo o escoge /start para volver al menú')
            bot.register_next_step_handler(m, ObtenerRecurrencia)

    rec = """Tu acabas de escoger la opción de relaciones de recurrencia 😁\nPor favor ingresa una función de la forma:
f(n) = c_1*f(n-1) + c_2*f(n-2) + ... + g(n) ; f(0) = v_1, f(1) = v_2, ..."""
    bot.send_message(message.chat.id, rec)
    bot.register_next_step_handler(message, ObtenerRecurrencia)

# Esta parte del código valida las entradas que el usuario digite y que el Bot no reconozca.

@bot.message_handler(content_types=["text"])
def validacion(message):

    # Lo que el bot nos va a responder

    rep = """ Mi inteligencia no permite leer lo que estas escribiendo 😔, asi que te lo repito: \nTengo distintas funciones🔧 como: 
    \n/Estrellas: Mostrar un gráfico de todas las estrellas🌟 
    \n/EyC: Mostrar un gráfico de todas las estrellas🌟 y una constelación🌌 en particular. 
    \n/Constelaciones: Mostrar todas las estrellas🌟 y constelaciones🌌🌌
    \n/Recurrencia: Hallar la solución de una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.
    \n \nPara escoger una opción, ingrese el comando""" 
    
    bot.send_message(message.chat.id, rep)

def ImagenABit(name):
  with open(f'Constellations\{name}.png', 'rb') as imagen:
    return imagen.read()

# Esta función ayuda a que nuestro bot guarde la información del us\nuario (bucle infinito).

if __name__ == '__main__':
    print('Iniciando bot')
    bot.infinity_polling()
    print("fin")