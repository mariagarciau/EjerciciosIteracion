"""Cuadrados perfectos y raíz cuadrada entera
Un número entero natural es un cuadrado perfecto si es el cuadrado de un número entero. Así, 0 = 02, 1 = 12, 4 = 22,16 = 42 son cuadrados perfectos.
1. Hacer un algoritmo que establezca la lista de los cuadrados perfectos inferiores a un límite dado. El algoritmo no debe hacer multiplicaciones.
La raíz cuadrada entera de un número entero n ≥ 0 es el único número enteror ≥ 0 definido por:
r2 ≤ n < (r + 1)2
2. Escribir el algoritmo de cálculo de la raíz cuadrada entera de un número entero."""
def cuadradosPerfectos(n1,n2):
  cuadrados=[]
  for i in range(n1,n2+1):
    n=1
    while n*n<=i:
      if n*n==i:
        cuadrados.append(i)
      n+=1
  return print(cuadrados)