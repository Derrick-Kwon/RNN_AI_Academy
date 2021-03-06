# Day_12_03_functional.py
import tensorflow.keras as keras
import numpy as np


# 퀴즈
# data를 x, y로 분할하세요
# x, y로 학습하는 모델을 만들고 결과를 예측하세요
def and_sequential():
    # AND
    data = [[0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1]]
    data = np.int32(data)

    x = data[:, :-1]
    y = data[:, -1:]
    # print(x.shape, y.shape)       # (4, 2) (4, 1)

    model = keras.Sequential()
    model.add(keras.layers.InputLayer(input_shape=[2]))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    model.summary()

    model.compile(optimizer=keras.optimizers.SGD(0.01),
                  loss=keras.losses.binary_crossentropy,
                  metrics='acc')

    model.fit(x, y, epochs=10, verbose=2)
    print(model.evaluate(x, y, verbose=0))


def and_functional():
    data = [[0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1]]
    data = np.int32(data)

    x = data[:, :-1]
    y = data[:, -1:]

    input = keras.layers.Input(shape=[2])
    # dense = keras.layers.Dense(1, activation='sigmoid')

    # output = dense.__call__(input)
    # output = dense(input)
    output = keras.layers.Dense(1, activation='sigmoid')(input)

    model = keras.Model(input, output)
    model.summary()

    model.compile(optimizer=keras.optimizers.SGD(0.01),
                  loss=keras.losses.binary_crossentropy,
                  metrics='acc')

    model.fit(x, y, epochs=10, verbose=2)
    print(model.evaluate(x, y, verbose=0))


# and_sequential()
and_functional()


