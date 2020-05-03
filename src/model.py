import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import csv

# Import data
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
        if row[0] not in dates:
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

dates.remove(None)
snohomishCases.remove(None)
snohomishTemp.remove(None)
LACases.remove(None)
LATemp.remove(None)
NYCCases.remove(None)
NYCTemp.remove(None)

dates = np.array(dates)
snohomishCases = list(map(int, snohomishCases))
snohomishTemp = list(map(int, snohomishTemp))
LACases = list(map(int, LACases))
LATemp = list(map(int, LATemp))
NYCCases = list(map(int, NYCCases))
NYCTemp = list(map(int, NYCTemp))


diffSCases = [None] * (len(dates) - 1)
diffSTemps = [None] * (len(dates) - 1)
diffLCases = [None] * (len(dates) - 1)
diffLTemps = [None] * (len(dates) - 1)
diffNCases = [None] * (len(dates) - 1)
diffNTemps = [None] * (len(dates) - 1)

def diff(X, Y, A, B):
    for i in range(len(X)):
        X[i] = A[i + 1] - A[i]
        Y[i] = B[i + 1] - B[i]
    return (X, Y)

#calculate temperature differences and new cases per day
(diffSCases, diffSTemps) = diff(diffSCases, diffSTemps, snohomishCases, snohomishTemp)
(diffLCases, diffLTemps) = diff(diffLCases, diffLTemps, LACases, LATemp)
(diffNCases, diffNTemps) = diff(diffNCases, diffNTemps, NYCCases, NYCTemp)

outputFile = open('outputFile.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
for i in range(len(diffSCases)):
    outputWriter.writerow(["Snohomish", diffSCases[i], diffSTemps[i]])
    outputWriter.writerow(["Los Angeles", diffLCases[i], diffLTemps[i]])
    outputWriter.writerow(["New York City", diffNCases[i], diffNTemps[i]])

# X-Axis 
#Input X1 - Avg Temperature 2 weeks before ; Input X2 - Population density 

popDensitySize = 48*3

popDensityLA = []
popDensitySnohomish = []
popDensityNYC = []

for i in range(popDensitySize): 
    popDensityLA.append(7554)
    popDensityNYC.append(26403)
    popDensitySnohomish.append(2740)

#Y - Axis

X = [None]
X.append(diffSTemps)
X.append(diffLTemps)
X.append(diffNTemps)
X.remove(None)

Y = [None]
Y.append(diffSCases)
Y.append(diffLCases)
Y.append(diffNCases)
Y.remove(None)

popDense = [None]
popDense.append(popDensitySnohomish)
popDense.append(popDensityLA)
popDense.append(popDensityNYC)
popDense.remove(None)

#Neural Network model for linear regression


model = tf.keras.Sequential([   tf.keras.layers.Flatten(),
                                tf.keras.layers.Dense(3, input_dim = 2, activation = 'linear'),
                                tf.keras.layers.Dense(3, activation = 'linear'),
                                tf.keras.layers.Dense(1, activation = 'linear')
                            ])

model.compile(loss = 'mean_squared_error', optimizer = 'adam')

model.fit(X, Y, epochs=1000, batch_size=10)
