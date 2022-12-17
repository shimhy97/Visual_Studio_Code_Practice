# LSTM example
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
# import Keras Model
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LSTM, Input

model = Sequential()
model.add(LSTM(5, input_shape=(10, 3)))

model.compile(loss='MSE',
              optimizer='SGD',
              metrics=['accuracy'])

x = np.array([[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [1.4, 1.5, 1.2],
    [1.9, 1.1, 1.2],
    [1.7, 1.4, 1.2],
    [1.5, 1.3, 1.2],
    [1.5, 1.3, 1.2],
    [0, 0.1, 0.2],
]])  # (None, 10, 3)

intermediate_layer_model = Model(inputs=model.input,
                                 outputs=model.output)
output = intermediate_layer_model.predict(x[:1])
print("Keras:", output)