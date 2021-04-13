# Introduction to TensorFlow (TF)
## Agenda
- Understand the key components of TF 2.0
- Use the tf.data library to manipulate data and large datasets
- Create ML models in TF 2.0
- Use the Keras Sequential and Functional API to create ML models
- Train, deploy, and productionalize ML models at scale with Cloud AI Platform

## TensorFlow (TF)
- TF is an open-source, high-performance library for numerical computation that uses directed graphs.
- A tensor is an N-dimensional array of data
- `TensorFlow Lite` provides on-device inference of ML models on mobile and is available for variety of hardware
```
TF runs on hardware -> Core TF C++ (quite low level) -> Core TF Python (give full control) -> Components when building custom NN models -> High-level APIs for distributed training
```
- `tf.constant` produces constant tensors
- `tf.Variable` produces tensors that can be modified
- GradientTape records operations for Automatic Differentiation
- TF can compute the derivative of a function with respect to any parameter
