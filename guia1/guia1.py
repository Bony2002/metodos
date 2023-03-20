import matplotlib.pyplot as plt
import numpy as np

## Para Implementar en clase

class Vector:
  def __init__(self, components:list):
      self.components=components
      self.dimensions=len(components)

      pass

  def __add__(self, other):
    if not isinstance(other, Vector):
      raise ValueError("Unsupported!!")
    elif self.dimension != other.dimension:
      raise ValueError("Vector must have the same dimensions to be summed")
    else:
      suma=list()
      i=0
      while(i <self.dimensions):
          suma.append(self.components[i]+other.components[i])
          i+=1
      return suma

  def __sub__(self,other):
    if not isinstance(other, Vector):
      raise ValueError("Unsupported!!")
    elif self.dimension != other.dimension:
      raise ValueError("Vector must have the same dimensions to be summed")
    else:
      resta=list()
      i=0
      while(i <self.dimensions):
          resta.append(self.components[i]-other.components[i])
          i+=1
      return resta

  def __mul__(self, value):
    if not isinstance(value, (int, float)):
      raise ValueError('Unsupported!!')
    else:
      mult=list()
      i=0
      while(i<self.dimensions):
          mult.append(self.components[i]*value)
          i+=1
      return mult

  def __rmul__(self, value):
    return self * value

  def __repr__(self):
    txt="Vector R" + str(self.dimensions) + "(" + self.components[0]
    i=1
    while(i<self.dimensions):
      txt+= "," + str(self.components[i])  
      i+=1
    txt+=")"
    return txt
  def escalar(self,other):
    if not isinstance(other, Vector):
      raise ValueError("Unsupported!!")
    elif self.dimension != other.dimension:
      raise ValueError("Vector must have the same dimensions to be escalated")
    else:
        total=0
        i=0
        while(i<self.dimensions):
            total+=self.components[i]*other.components[i]
            i+=1
        return total


class Matriz:
    def __init__(self,components:list):
        self.components=components
        self.filas=len(components)
        self.columnas=components[0].dimensions
        pass
    def __add__(self,other):
     if not isinstance(other, Matriz):
      raise ValueError("Unsupported!!")
     else:
        i=0
        res=Matriz()
        while(i<self.filas):
            res.components.append(self.components[i]+other.components[i])
            i+=1
        return res

    def __sub__(self,other):
     if not isinstance(other, Matriz):
      raise ValueError("Unsupported!!")
     else:
        i=0
        res=Matriz()
        while(i<self.filas):
            res.components.append(self.components[i]-other.components[i])
            i+=1
        return 
    def __mul__(self,value):
        i=0
        res=Matriz()
        while(i<self.filas):
            res.components.append(self.components[i]*value)
            i+=1
        return res
    def matrizporvector(self,vector):
     if not isinstance(vector, Vector):
      raise ValueError("Unsupported!!")
     else:
        res=Vector()
        i=0
        j=0
        while(i<self.filas):
            res.append(self.components[i].escalar(vector))
        return res
    def transpuesta(self):
        res=list()
        i=0
        j=0
        while(i<self.columnas):
            while(j<self.filas):
                aux=list()
                aux.append((self.components[j]).components[i])
                j+=1
            res.append(aux)    
            j=0
            i+=1
        return Matriz(res)
        
              
    def matrizxmatriz(self,other):
        res:list = list()   
        i=0
        j=0
        while(i<self.filas):
            while(j<self.columnas):
                aux:list = list()
                aux.append(self.components[j]*other.components[j])
                j+=1
            res.append(Vector(aux))
            j=0
            i+=1
        return Matriz(res)
    