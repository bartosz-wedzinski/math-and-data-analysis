import tensorflow as tf
from tensorflow.keras import layers, models, datasets
import matplotlib.pyplot as plt
import numpy as np

# 1. Pobranie danych CIFAR-10
print("Pobieranie i przygotowanie danych...")
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# 2. Funkcja budująca model
def build_model(use_bn=False, use_dropout=False):
    model = models.Sequential()
    
    # Warstwy splotowe (Feature extraction)
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    if use_bn: model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D((2, 2)))
    
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    if use_bn: model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D((2, 2)))
    
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    if use_bn: model.add(layers.BatchNormalization())
    
    # Warstwy klasyfikujące (Classification)
    model.add(layers.Flatten())
    if use_dropout: model.add(layers.Dropout(0.5))
    model.add(layers.Dense(64, activation='relu'))
    if use_bn: model.add(layers.BatchNormalization())
    model.add(layers.Dense(10))

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    return model

# 3. Trening 3 wariantów
EPOCHS = 8

print("\n--- Model 1: BAZOWY ---")
model_base = build_model()
hist_base = model_base.fit(train_images, train_labels, epochs=EPOCHS, validation_data=(test_images, test_labels), verbose=2)

print("\n--- Model 2: BATCH NORMALIZATION ---")
model_bn = build_model(use_bn=True)
hist_bn = model_bn.fit(train_images, train_labels, epochs=EPOCHS, validation_data=(test_images, test_labels), verbose=2)

print("\n--- Model 3: DROPOUT ---")
model_drop = build_model(use_dropout=True)
hist_drop = model_drop.fit(train_images, train_labels, epochs=EPOCHS, validation_data=(test_images, test_labels), verbose=2)

# 4. Rysowanie wykresów
plt.figure(figsize=(14, 6))

# Wykres dokładności
plt.subplot(1, 2, 1)
plt.plot(hist_base.history['val_accuracy'], label='Bazowy', linestyle='--')
plt.plot(hist_bn.history['val_accuracy'], label='Batch Norm', linewidth=2)
plt.plot(hist_drop.history['val_accuracy'], label='Dropout', linewidth=2)
plt.title('Dokładność na zbiorze testowym')
plt.xlabel('Epoka')
plt.ylabel('Dokładność (Accuracy)')
plt.legend()
plt.grid(True)

# Wykres straty
plt.subplot(1, 2, 2)
plt.plot(hist_base.history['val_loss'], label='Bazowy', linestyle='--')
plt.plot(hist_bn.history['val_loss'], label='Batch Norm')
plt.plot(hist_drop.history['val_loss'], label='Dropout')
plt.title('Strata (Błąd) na zbiorze testowym')
plt.xlabel('Epoka')
plt.ylabel('Strata (Loss)')
plt.legend()
plt.grid(True)

plt.show()