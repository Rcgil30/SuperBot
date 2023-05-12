import matplotlib.pyplot as plt

# Nombres de las estrellas que podemos graficar
estrellas = ('Boyero', 'Casiopea', 'Cazo', 'Cygnet', 'Geminis', 'Hydra', 'OsaMayor', 'OsaMenor')
rutas = {}
# Creamos un diccionario donde las llaves son las estrellas y los datos son las rutas de acceso a sus archivos
for estrella in estrellas:
    rutas[estrella] = f'Constellations\{estrella}.txt'

# lista con las coordenadas en x de las estrellas
x = []
# lista con las coordenadas en y
y = []
# Guardamos las estrellas con nombre y sus posiciones en x y y
NamedStarsX = {}
NamedStarsY = {}

with open("Constellations\stars.txt", "r") as stars:
  for star in stars:
    # Separamos todos los campos para guardar x y y
    aux = star.split(" ")
    x.append(float(aux[0]))
    y.append(float(aux[1]))
    # Esto se ejecuta si la estrella tiene nombre
    if len(aux) > 6:
      name = ""
      nameInfo = aux[6:]
      for word in nameInfo:
        name += word + " "
      # Quitamos el \n que queda al final
      name = name[:-1]
      # Verificamos si tiene varios nombres
      if ";" in name:
        # Separamos los nombres y los añadimos individualmente con las mismas coordenadas
        multinames = name.split(";")
        for names in multinames:
          NamedStarsX[names.strip()] = float(aux[0])
          NamedStarsY[names.strip()] = float(aux[1])
      # Si solo tiene un nombre se escoge y se añade al diccionario de las estrellas con nombre
      else:
        NamedStarsX[name[:-1]] = float(aux[0])
        NamedStarsY[name[:-1]] = float(aux[1])


def GraficarConstelacion(txtPath):
  # Abrimos el archivo de la constelación correspondiente
  with open(txtPath) as constelacion:
    for line in constelacion:
      connection = line.split(",")
      # Le quitamos el \n del final
      connection[1] = connection[1][:-1]
      Estrella1 = connection[0]
      Estrella2 = connection[1]
      # Hallamos las coordenadas de las estrellas usando los diccionarios de estrellas con nombre
      x1 = NamedStarsX[Estrella1]
      x2 = NamedStarsX[Estrella2]
      y1 = NamedStarsY[Estrella1]
      y2 = NamedStarsY[Estrella2]
      # Dibujamos la línea entre las estrellas
      plt.plot((x1, x2), (y1, y2), color="white")
      # Incrementamos el tamaño de las estrellas de la constelación para que sean más notorios
      plt.scatter((x1, x2), (y1, y2), color='white', s=10)

def ObtenerImagen(Todas: bool, Constelacion: str):
  plt.rcParams['figure.figsize'] = [10, 10]
  # Ponemos el fondo y los ejes en negro para que se resalte la imagen
  with plt.rc_context({'axes.edgecolor':'black', 'xtick.color':'black', 'ytick.color':'black', 'figure.facecolor':'black'}):
    ax = plt.axes()
    ax.set_facecolor('black')
    # Graficamos todas las estrellas
    plt.scatter(x, y, s=1, color='white')
    name = ''
    # Si son todas las constelaciones
    if Todas:
        name = 'Constelaciones'
        # Graficamos cada constelacion de las rutas que tenemos guardadas
        for ruta in rutas:
            GraficarConstelacion(rutas[ruta])
    # Si tenemos alguna constelacion
    elif Constelacion != '':
        name = Constelacion
        GraficarConstelacion(rutas[Constelacion])
    # En caso de que no haya que graficar constelaciones
    else:
        name = 'Estrellas'

    # Guardamos la imagen creada en la carpeta de constelaciones
    plt.savefig(f'Constellations\{name}.png')
  

if __name__ == '__main__':
   # Creamos las imágenes necesarias que el bot va a devolver
   ObtenerImagen(True, '')
   ObtenerImagen(False, '')
   for estrella in estrellas:
      ObtenerImagen(False, estrella)