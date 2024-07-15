import csv
import numpy as np
import matplotlib.pyplot as plt

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

#print lists
#print(fare_survived)
#print(fare_not_survived)

#print aggregated data for easier analysis
#print(f"The average fare of those who survived was: ${round(np.mean(fare_survived), 2)}")
#print(f"The average fare of those who did not survive was: ${round(np.mean(fare_not_survived), 2)}")

#print(f"The median fare of those who survived was: ${round(np.median(fare_survived), 2)}")
#print(f"The median fare of those who did not survive was: ${round(np.median(fare_not_survived), 2)}")

#The max fare is $240, and divide them by increments of 15
bins = range(0,240,15)