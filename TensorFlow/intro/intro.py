import tensorflow as tf

print("TensorFlow Version: ", tf.version.VERSION)

x = tf.constant(3)
print(x)
x = tf.constant([3, 5, 7])
print(x)

x = tf.constant([[3, 5, 7],
                [4, 6, 8]])
print(x)
y = x[:, 1]
print(y)
y = tf.reshape(x, [3,2])
print(y)

x = tf.constant([[[3, 5, 7],[4, 6, 8]],
                [[3, 5, 7],[4, 6, 8]]])
print(x)

# tf.Variable
x = tf.Variable(2.0, dtype=tf.float32, name='my_variable')
x.assign(45.8)
# x <- x + 4
x.assign_add(4)
# x <- x - 3
x.assign_sub(3)
print(x)

# w*x
w = tf.Variable([[1.], [2.]])
x = tf.constant([[3., 4.]])
print(tf.matmul(w, x))