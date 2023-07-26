import tensorflow as tf
from tensorflow.keras.layers import Dense
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# data_process
data = pd.read_csv('SnakeDataSet/dataset.csv')

data = data.values
Y = data[:, -1]
X = data[:,:-1]

Y = Y.reshape(-1, 1)
Y.shape

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=24)

# modeling

model = tf.keras.models.Sequential([
    Dense(16, input_dim=6, activation='relu'),
    Dense(24, activation='relu'),
    Dense(48, activation='relu'), 
    Dense(64, activation='relu'),
    Dense(8, activation='softmax') 
])

# model_compilation

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
loss=tf.losses.sparse_categorical_crossentropy,
metrics=['accuracy'])

train_output = model.fit(X_train, Y_train, epochs=50)

# evaluate
model.evaluate(X_test, Y_test)
model.save('MLPModel/Movement.h5')