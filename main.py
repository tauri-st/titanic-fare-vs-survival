import csv
import numpy as np

with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data = list(data)
  data = np.array(data)
  
#create a numpy array with a slice for the survived column which is in index position zero and we want the data to be an integer. 
#The flatten function turns the array from two-dimensional to one which is easier to work with
survived = np.array(data[:,[0]], dtype=int).flatten()
fare = np.array

#empty lists to hold data from  the for loop
fare_survived = []
fare_not_survived = []

#ADD CODE: for loop and if/else statements

#ADD CODE: print lists
