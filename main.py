import csv
import numpy as np

with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data = list(data)
  data = np.array(data)
  #print(headers)
  
#create a numpy array with a slice for the survived column which is in index position zero and we want the data to be an integer. 
#The flatten function turns the array from two-dimensional to one which is easier to work with
survived = np.array(data[:,[0]], dtype=int).flatten()
fare = np.array(data[:,[7]], dtype=float).flatten()

#empty lists to hold data from  the for loop
fare_survived = []
fare_not_survived = []

#for loop and if/else statements
#The length function inside range tells the loop when to begin and end the loops
for index in range(0, len(fare)):
  if survived[index] == 1:
    fare_survived.append(fare[index])
  else:
    fare_not_survived.append(fare[index])

#ADD CODE: print lists
