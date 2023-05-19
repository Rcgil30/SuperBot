import sympy as sp
import requests
import io

def RRLNHCCC(input):
  """ El input será de la forma f(n) = c1*f(n-1) + c2*f(n-2) ... + g(n) ; f(0) = s1, f(1) = s2 ... f(k) = sk """
  # Separamos la parte de la función y las condciones iniciales
  In = input.split(";")
  # Guardamos f(n) y las condiciones iniciales
  fn = In[0].strip()
  cond_in = In[1].strip().split(", ")
  condiciones = {}
  
  # Guardamos cada condición inicial en un diccionario de la forma {f(0): 1, f(1) = 3, ...}
  # Siendo f(0) una expresión simbólica
  for cond in cond_in:
    aux = cond.split("=")
    condiciones[sp.parse_expr(aux[0])] = int(aux[1])

  # Guardamos la parte derecha de la igualdad 
  relacion = sp.parse_expr(fn.split("=")[1])

  # Guardamos los términos de la relación individualmente
  if '+' in fn:
    terminos = list(relacion.args)
  else:
    terminos = [relacion]
  
  f = sp.Function('f')
  n = sp.symbols('n')
  
  funcion = f(n)

  # Lo que se hace en este paso es lo siguiente:
  # Supongamos que f(n) = f(n-1) + f(n-2)
  # Entonces vamos a tener en la variable funcion f(n) - f(n-1) - f(n-2)
  for termino in terminos:
    funcion -= termino
  
  # Igualamos esta función a 0 y le damos las condiciones iniciales para hallar la 
  # función no recurrente
  return sp.rsolve(funcion, f(n), condiciones)

def RelacionesDeRecurrencia(input):
  # Hallamos la relación de recurrencia
  print(input)
  fn =  RRLNHCCC(input)
  # Convertimos el resultado a LaTeX
  f = sp.latex('f(n) = ') + sp.latex(fn)
  # Enviamos esta fórmula de LaTeX a codecogs para tenerlo en formato de imagen
  response = requests.get('http://latex.codecogs.com/png.latex?\dpi{{1200}} {formula}'.format(formula=f))
  print('b')
  # Devolvemos la imagen cono bytes para que el bot lo lea
  return io.BytesIO(response.content)
  
