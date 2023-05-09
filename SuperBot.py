# Archivo .py que contiene el API
from config import * 

# Importamos TeleBot, librería que nos ayuda a configurar nuestro bot 
import telebot 

#----------------------------------------

# CONFIGURACIÓN DEL BOT

#---------------------------------------


# Asignamos el API a una variable llamada bot

bot=telebot.TeleBot(TELEGRAM_TOKEN) 

# Mensaje de bienvenida y menú.

intro ="""  Bienvenido, mi nombre es SuperBot🤖. \n \n¿En que te puedo servir?😎 
 \nTengo distintas funciones 🔧 como: \n1.Mostrar un gráfico de todas las estrellas🌟 
 \n2.Mostrar un gráfico de todas las estrellas🌟 y una constelación🌌 en particular. 
 \n3.Mostrar todas las estrellas🌟 y constelaciones🌌🌌
 \n4.Hallar la solución de una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.
 \n5.Hola esto es un saludo especial para Thomas Camacho (escribe /thomas y envialo)
\n \nPara escoger una opción, ingrese el comando"""


ayuda = """  Hola!!!🤖🤖
Para escoger alguna opción ingresa alguno de los comandos 🔧: 
\n 1.Mostrar un gráfico de todas las estrellas🌟 
\n comando: /Estrellas
\n2.Mostrar un gráfico de todas las estrellas🌟 y una constelación🌌 en particular. 
\n comando: /EyC
\n3.Mostrar todas las estrellas🌟 y constelaciones🌌🌌
\n comando: /Todo
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
def helppp(message):

    # Lo que el bot nos va a responder cuando ingrese 

    bot.reply_to(message, ayuda)

# Si escoge la opción de Mostrar un gráfico de todas las estrellas y una constelación

@bot.message_handler(commands=["EyC"])
def helppp(message):

    # Lo que el bot nos va a responder cuando ingrese 
    bot.reply_to(message, "escogiste la 2")


# Si escoge la opción de Mostrar un gráfico de todas las estrellas🌟

@bot.message_handler(commands=["Estrellas"])
def helppp(message):

    # Lo que el bot nos va a responder cuando ingrese 
    bot.reply_to(message, "escogiste la 1")

# Si escoge Mostrar todas las estrellas🌟 y constelaciones🌌🌌

@bot.message_handler(commands=["Todo"])
def helppp(message):

    # Lo que el bot nos va a responder cuando ingrese 
    bot.reply_to(message, "escogiste la 3")

# Si escoge solucionar una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.

@bot.message_handler(commands=["Recurrencia"])
def helppp(message):

    # Lo que el bot nos va a responder cuando ingrese 
    bot.reply_to(message, "escogiste la 4")

# Esta parte del código valida las entradas que el usuario digite y que el Bot no reconozca.

@bot.message_handler(content_types=["text"])
def validacion(message):

    # Lo que el bot nos va a responder

    rep = """ Mi inteligencia no permite leer lo que estas escribiendo 😔, asi que te lo repito: \nTengo distintas funciones🔧 como: 
    \n 1.Mostrar un gráfico de todas las estrellas🌟 
    \n2.Mostrar un gráfico de todas las estrellas🌟 y una constelación🌌 en particular. 
    \n3.Mostrar todas las estrellas🌟 y constelaciones🌌🌌
    \n4.Hallar la solución de una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.
    \n \nPara escoger una opción, ingrese el número""" 
    
    bot.send_message(message.chat.id, rep)


# Esta función ayuda a que nuestro bot guarde la información del usuario (bucle infinito).

if __name__ == '__main__':
    print('Iniciando bot')
    bot.infinity_polling()
    print("fin")