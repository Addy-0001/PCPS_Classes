import tensorflow as tf

# scalar, vector, and matrix constants
scalar = tf.constant(5)
vector = tf.constant([1.0, 2, 3.0])
matrix = tf.constant([[1.0, 2.0], [3.0, 4.0]])

print("Scalar:", scalar)
print("Vector:", vector)
print("Matrix:", matrix)


#variables in tensorflow
# Creating a variable
var = tf.Variable([1.0, 2.0, 3.0])
print("Variable:", var)

# Updating the variable
var.assign([4.0, 5.0, 6.0])
print("Updated Variable:", var)


# Operations in TensorFlow
a = tf.constant(3.0)
b = tf.constant(4.0)

# Perform addition
c = tf.add(a, b)  # Or simply c = a + b
print("Addition Result:", c)


# Gradient and functions in TF
# Define a simple function
def f(x):
    return x**2

# Compute gradient at x = 3
x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = f(x)
    print(y)
gradient = tape.gradient(y, x)
print("Gradient of x^2 at x=3:", gradient)