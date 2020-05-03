import tensorflow as tf
from tensorflow import keras
from keras.models impoty Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import csv


# Clean Data
DATACSV = open('DATA.csv', 'r')

DATAReader = csv.reader(DATACSV)

dates = [None]

snohomishCases = [None]
LACases = [None]
NYCCases = [None]

snohomishTemp = [None]
LATemp = [None]
NYCTemp = [None]

startCollecting = False

for row in DATAReader:
    if row[0] == "2020-03-01":
        startCollecting = True
    elif row[0] == "2020-04-19":
        startCollecting = False

    if startCollecting == 1:
        dates.append(row[0])
        if row[1] == "Snohomish":
            snohomishCases.append(row[4])
            snohomishTemp.append(row[6])
        elif row[1] == "Los Angeles":
            LACases.append(row[4])
            LATemp.append(row[6])
        elif row[1] == "New York City":
            NYCCases.append(row[4])
            NYCTemp.append(row[6])

snohomishCases.remove(None)
snohomishTemp.remove(None)
LACases.remove(None)
LATemp.remove(None)
NYCCases.remove(None)
NYCTemp.remove(None)

popDensitySize = len(LACases) - 14

popDensityLA = []
popDensitySnohomish = []
popDensityNYC = []

for range(popDensitySize) 
    popDensityLA.append(7554)
    popDensityNYC.append(26403)
    popDensitySnohomish.append(2740)


# X-Axis 
   
#Input X1 - Avg Temperature 2 weeks before ; Input X2 - Population density

thetas = []

m = popDensitySize



//Neural Network model for linear regression

model = Sequential()
model.add(Dense(3, input_dim = 3, activation = 'linear')
model.add(Dense(3, activation = 'linear')
model.add(Dense(1, activation = 'sigmoid')

