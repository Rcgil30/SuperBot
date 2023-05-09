import matplotlib.pyplot as plt

# Nombres de las estrellas que podemos graficar
estrellas = ('Boyero', 'Casiopea', 'Cazo', 'Cygnet', 'Geminis', 'Hydra', 'OsaMayor', 'OsaMenor')
rutas = {}
# Creamos un diccionario donde las llaves son las estrellas y los datos son las rutas de acceso a sus archivos
for estrella in estrellas:
    rutas[estrella] = f'Constellations\{estrella}.txt'

x = []
y = []
NamedStarsX = {}
NamedStarsY = {}

with open("Constellations\stars.txt", "r") as stars:
  for star in stars:
    aux = star.split(" ")
    x.append(float(aux[0]))
    y.append(float(aux[1]))
    if len(aux) > 6:
      name = ""
      nameInfo = aux[6:]
      for word in nameInfo:
        name += word + " "
      name = name[:-1]
      if ";" in name:
        multinames = name.split(";")
        for names in multinames:
          NamedStarsX[names.strip()] = float(aux[0])
          NamedStarsY[names.strip()] = float(aux[1])
      else:
        NamedStarsX[name[:-1]] = float(aux[0])
        NamedStarsY[name[:-1]] = float(aux[1])


def GraficarConstelacion(txtPath):
  with open(txtPath) as constelacion:
    for line in constelacion:
      connection = line.split(",")
      connection[1] = connection[1][:-1]
      Estrella1 = connection[0]
      Estrella2 = connection[1]
      x1 = NamedStarsX[Estrella1]
      x2 = NamedStarsX[Estrella2]
      y1 = NamedStarsY[Estrella1]
      y2 = NamedStarsY[Estrella2]
      plt.plot((x1, x2), (y1, y2), color="white")
      plt.scatter((x1, x2), (y1, y2), color='white', s=10)

def ObtenerImagen(Todas: bool, Constelacion: str):
  plt.rcParams['figure.figsize'] = [10, 10]
  with plt.rc_context({'axes.edgecolor':'black', 'xtick.color':'black', 'ytick.color':'black', 'figure.facecolor':'black'}):
    ax = plt.axes()
    ax.set_facecolor('black')
    plt.scatter(x, y, s=1, color='white')
    if Todas:
        for ruta in rutas:
            GraficarConstelacion(rutas[ruta])
    elif Constelacion != '':
        GraficarConstelacion(rutas[Constelacion])
    plt.savefig('Constellations\output.png')
  with open('Constellations\output.png', 'rb') as image:
    return image.read()

