# Build Machine Learning Solutions with Tensorflow

## Installation Guide for TensorFlow 2.0
- TensorFlow (TF): the latest stable release with CPU and GPY support Ubuntu and Windows
- tf-nightly: preview build (unstable)
- Note: TensorFlow 2 packages require a pip version later than 19.0

### Linux OS/MacOS
- Install TF
    - `pip3 install --user --upgrade tensorflow`
- Run the code to verify TF installation
    - `python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([10, 10])))"`
