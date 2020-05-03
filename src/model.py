import tensorflow as tf
from tensorflow import keras
from keras.models impoty Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import csv


# X-Axis 
#Input X1 - Avg Temperature 2 weeks before ; Input X2 - Population density 

popDensitySize = 49*3

popDensityLA = []
popDensitySnohomish = []
popDensityNYC = []

for range(popDensitySize) 
    popDensityLA.append(7554)
    popDensityNYC.append(26403)
    popDensitySnohomish.append(2740)

#Y - Axis



//Neural Network model for linear regression

model = Sequential()
model.add(Dense(3, input_dim = 2, activation = 'linear'))
model.add(Dense(3, activation = 'linear'))
model.add(Dense(1, activation = 'linear'))

model.compile(loss = 'mean squared error', optimizer = 'adam', metrics = 'accuracy')

model.fit(


