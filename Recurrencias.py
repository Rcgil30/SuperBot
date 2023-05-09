import sympy as sp
import requests
import io

def RRLNHCCC(input):
  """ El input será de la forma f(n) = c1*f(n-1) + c2*f(n-2) ... + g(n) ; f(0) = s1, f(1) = s2 ... f(k) = sk """
  In = input.split(";")
  fn = In[0].strip()
  cond_in = In[1].strip().split(", ")
  condiciones = {}
  
  for cond in cond_in:
    aux = cond.split("=")
    condiciones[sp.parse_expr(aux[0])] = int(aux[1])

  relacion = sp.parse_expr(fn.split("=")[1])

  if '+' in fn:
    terminos = list(relacion.args)
  else:
    terminos = [relacion]
  
  f = sp.Function('f')
  n = sp.symbols('n')
  
  funcion = f(n)

  for termino in terminos:
    funcion -= termino
  
  return sp.rsolve(funcion, f(n), condiciones)

def RelacionesDeRecurrencia(input):
  try:
    fn =  RRLNHCCC(input)
    f = sp.latex('f(n) = ') + sp.latex(fn)
    response = requests.get('http://latex.codecogs.com/png.latex?\dpi{{1200}} {formula}'.format(formula=f))
    imagen = io.BytesIO(response.content)
    return imagen

  except:
    return 'Relación de recurrencia digitada de forma incorrecta'
  
