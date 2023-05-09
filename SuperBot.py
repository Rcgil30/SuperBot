# Archivo .py que contiene el API
from config import * 

# Importamos TeleBot, librería que nos ayuda a configurar nuestro bot 
import telebot 

from Estrellas import ObtenerImagen
from Recurrencias import RelacionesDeRecurrencia

#----------------------------------------

# CONFIGURACIÓN DEL BOT

#---------------------------------------


# Asignamos el API a una variable llamada bot

bot=telebot.TeleBot(TELEGRAM_TOKEN) 

# Mensaje de bienvenida y menú.

intro ="""  Bienvenido, mi nombre es SuperBot🤖. \n \n¿En que te puedo servir?😎 
 \nTengo distintas funciones 🔧 como: \n/estrellas: Mostrar un gráfico de todas las estrellas🌟 
 \n/constelacion: Mostrar un gráfico de todas las estrellas🌟 y una constelación🌌 en particular. 
 \n/constelaciones: Mostrar todas las estrellas🌟 y constelaciones🌌🌌
 \n/recurrencia Hallar la solución de una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.
\n \nPara escoger una opción, ingrese el número"""



# Usamos decoradores, estas reciben parámetros de otras funciones y retorna distintos resultados (Reusar código)
# Los comandos a utilizar son /start, /help, /ayuda. Creamos la función

@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):

    # Lo que el bot nos va a responder

    bot.reply_to(message, intro)

# Esta parte del código valida las entradas que el usuario digite y que el Bot no reconozca.

@bot.message_handler(content_types=["text"])
def validacion(message):

    # Lo que el bot nos va a responder

    rep = """ Mi inteligencia no permite leer lo que estas escribiendo 😔, asi que te lo repito: \nTengo distintas funciones🔧 como: 
    \n/estrellas: Mostrar un gráfico de todas las estrellas🌟 
    \n/constelacion: Mostrar un gráfico de todas las estrellas🌟 y una constelación🌌 en particular. 
    \n/constelaciones: Mostrar todas las estrellas🌟 y constelaciones🌌🌌
    \n/recurrencia: Hallar la solución de una Relación de Recurrencia Lineal, No homogénea, con coeficientes constantes.
    \n \nPara escoger una opción, ingrese el comando""" 

    # Si llega a colocar una de las opciones.

    if message.text.startswith("/estrellas"):
        bot.send_photo(message.chat.id, photo=ObtenerImagen(False, ''))

    elif message.text.startswith("/constelacion"):
        bot.send_message(message.chat.id, "Escogiste punto 2")

    elif message.text.startswith("/constelaciones"):
        bot.send_message(message.chat.id, "Escogiste punto 3")

    elif message.text.startswith("/recurrencia"):
        puntoCuatro(message)

    else:
        bot.send_message(message.chat.id, rep)

# Aqui se encuentra todo lo de la opción 4

def puntoCuatro(message):
    f = RelacionesDeRecurrencia('f(n) = f(n-1) + 2*f(n - 2) ; f(0) = 1, f(1) = 1')
    if type(f) != str:
        bot.send_photo(message.chat.id, photo=f)
    else:
        bot.send_message(message.chat.id, f)

# Esta función ayuda a que nuestro bot guarde la información del us\nuario (bucle infinito).

if __name__ == '__main__':
    print('Iniciando bot')
    bot.infinity_polling()
    print("fin")