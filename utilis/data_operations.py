import math
import numpy as np
import pandas as pd

def euclidean_distance(x1,x2):
    """Eucledian Distance between two points"""
      distance=math.sqrt((x1[0]-x2[0])*(x1[0]-x2[0])+(x1[1]-x2[1])*(x1[1]-x2[1])+(x1[2]-x2[2])*(x1[2]-x2[2]))
      return distance
x3 = [1,2,3]
x4 = [4,5,6]

# print(euclidean_distance(x3,x4))
