'''
A. Генератор точек в круге

One approach to solve this problem could be to compare the distribution of
the points generated by each algorithm to the distribution of the given
sets of points.
One way to compare the distributions is to calculate the average distance
between all points in the set of points and the origin (0,0) for both algorithms.
'''
from math import sqrt
import random
import math
from itertools import chain

def generate1():  
    a = random.uniform(0, 1)  
    b = random.uniform(0, 1)  
    return (a * math.cos(2 * math.pi * b), a * math.sin(2 * math.pi * b))
def generate2():  
    while True:  
        x = random.uniform(-1, 1)  
        y = random.uniform(-1, 1)  
        if x ** 2 + y ** 2 > 1:  
            continue  
        return (x, y)

l = [] #list the will containts 100 set of (1000 pairs x,y)
for i in range(100):        #100 sublist 
  l_i = []
  for iii in range(1000):   #1000values for each set
    if i < 63:              #63 set with the first generator
      (a,b) = generate1()   
    else:
      (a,b) = generate2()
    l_i.append(a)
    l_i.append(b)
  l_i = [str(i) for i in l_i]
  l.append(' '.join(l_i))    #each sublist contains a string x,y separated by' '
     

f = open('input_v.txt', 'w')   #create file
for index in l:
  f.write(index + '\n')      #put in sublist string in file , one string one lines
     

#function that takes in a set of points and returns the average distance
#between all points and the origin     
def avg_distance(points):
    total_distance = 0
    for i in range(0, len(points), 2):
        x = points[i]
        y = points[i+1]
        total_distance += sqrt(x*x + y*y)
    return total_distance / (len(points) / 2)

#function calculate the average distance of the points generated by each algorithm and
#then compare that to the average distance of the given sets of points.
#The algorithm whose average distance is closest to the given set of points is likely to
#have generated that set of points.

def main(points):
    points = [float(i) for i in points.split()]
    avg_dist_1 = avg_distance(list(chain(*[generate1() for _ in range(1000)])))
    avg_dist_2 = avg_distance(list(chain(*[generate2() for _ in range(1000)])))
    avg_dist_points = avg_distance(points)
    if abs(avg_dist_1 - avg_dist_points) < abs(avg_dist_2 - avg_dist_points):
         return(1)
    else:
         return(2)

#call the main function on each set of points to get the generated algorithm for
#that set of points.

with open('input.txt') as f:
    input_points = f.readlines()

input_points = [x.strip() for x in input_points]


for i in range(100):
    print(main(input_points[i]))


