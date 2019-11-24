from __future__ import absolute_import, division, print_function, unicode_literals
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import webcolors

raw_dataset = pd.read_csv('outfit_data.csv',
                      na_values = "?", comment='\t',
                      sep=",", skipinitialspace=True, index_col='id')

clothes_dataset = pd.read_csv('clothes_data.csv', index_col='id', error_bad_lines=False)

def get_clothing_type(clothing):
    if clothing['articleType'] == 'Jackets':
      return 'outerwear'
    if clothing['subCategory'] == 'Topwear':
      return 'top'
    if clothing['subCategory'] == 'Bottomwear':
      return 'bottom'
    if clothing['masterCategory'] == 'Footwear':
      return 'shoe'
    if clothing['masterCategory'] == 'Accessories':
      return 'accessory'

def get_alt_color(colour):
  if colour == "Cream":
    colour = 'bisque'
  if colour == 'Navy Blue':
    colour = 'DarkBlue'
  if colour == 'Steel':
    colour = 'silver'
  if colour == 'Charcoal':
    colour = 'black'
  if colour == 'Grey Melange':
    colour = 'grey'
  if colour == 'Off White':
    colour = 'bisque'
  if colour == 'Copper':
    colour = 'peru'
  return webcolors.name_to_rgb(colour)[0] * 0.2126 + webcolors.name_to_rgb(colour)[1] * 0.7152 + webcolors.name_to_rgb(colour)[2] * 0.0722

dataset = raw_dataset.copy()
for index, row in dataset.iterrows():
  clothes_ids = [int(x) for x in row.clothes_ids.split(',')]
  for id in clothes_ids:
    clothing = clothes_dataset.loc[id]
    clothing_type = get_clothing_type(clothing)
    colour = clothing['baseColour']
    col = clothing_type + "brightness"
    dataset.at[index, col] = get_alt_color(colour)

dataset = dataset.fillna(0)
del dataset['clothes_ids']

train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)
train_dataset

sns.pairplot(train_dataset[['rating', 'outerwearbrightness', 'bottombrightness',	'shoebrightness',	'accessorybrightness',	'topbrightness']], diag_kind="kde")

train_stats = train_dataset.describe()
train_stats.pop("rating")
train_stats = train_stats.transpose()
train_stats

train_labels = train_dataset.pop('rating')
test_labels = test_dataset.pop('rating')

def norm(x):
   return (x - train_stats['mean']) / train_stats['std']

normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)



def build_model():
  model = keras.Sequential([
    layers.Dense(32, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

model = build_model()

model.summary()

example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
example_result

normed_train_data[:10]

# Display training progress by printing a single dot for each completed epoch
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 1000

history = model.fit(
  normed_train_data, train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[PrintDot()])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [Rating]')
  plt.plot(hist['epoch'], hist['mean_absolute_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
           label = 'Val Error')
  plt.ylim([0,5])
  plt.legend()

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$Rating^2$]')
  plt.plot(hist['epoch'], hist['mean_squared_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_squared_error'],
           label = 'Val Error')
  plt.ylim([0,20])
  plt.legend()
  plt.show()


plot_history(history)

model = build_model()

# The patience parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(normed_train_data, train_labels, epochs=EPOCHS,
                    validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])

plot_history(history)

loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} Rating".format(mae))

test_predictions = model.predict(normed_test_data).flatten()

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [Rating]')
plt.ylabel('Predictions [Rating]')
lims = [0, 10]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)

error = test_predictions - test_labels
plt.hist(error, bins = 25)
plt.xlabel("Prediction Error [Rating]")
_ = plt.ylabel("Count")
