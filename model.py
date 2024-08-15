# Building an AI model using TensorFlow

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Create a simple neural network
model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),  # Input layer with 128 units
    Dense(64, activation='relu'),  # Hidden layer
    Dense(10, activation='softmax')  # Output layer with 10 units for classification
])
model.summary()


#Compiling the model
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])


#Training The model
# Dummy training data
import numpy as np
X_train = np.random.rand(1000, 784)  # 1000 samples, 784 features
y_train = np.random.randint(0, 10, 1000)  # 1000 labels for 10 classes

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)



#Model Evaluation
# Dummy test data
X_test = np.random.rand(200, 784)  # 200 samples
y_test = np.random.randint(0, 10, 200)  # 200 labels

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')


# Making Predictions
# Make predictions on test data
predictions = model.predict(X_test)
print("Predictions:\n", predictions)


# Creating a dataset
# Create a dataset from NumPy arrays
dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))

# Shuffle and batch the dataset
dataset = dataset.shuffle(buffer_size=1000).batch(32)

# Iterate through the dataset
for X_batch, y_batch in dataset:
    print("Batch shape:", X_batch.shape, y_batch.shape)
