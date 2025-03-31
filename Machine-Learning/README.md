
# TensorFlow
- TensorFlow is an open-source, high-performance library for numerical computation thats uses directed graphs
- A tensor is an N-dimensional array of data. The simplest piece od data is called scalar. Scalar -> Vector -> Matrix ->  3D tensor -> 4D tensor . They behave like numpy n-dimensinal arrays except that:
    - tf.constant will produce tensors with constant values
    - tf.variable produces tensors with variable values or ones that can be modified. They typically hold model weights that need to be updated in a training loop.

    ![image](https://github.com/user-attachments/assets/01782333-76d0-46df-896a-c55db62d002a)

    ![image](https://github.com/user-attachments/assets/b8e29d89-4925-4815-8530-d0f7b524f7f3)


- TensorFlow graphs are portable between different devices. You can build a DAG in Python, store it in a saved model, restore it in C++ program for low latency predictions, you can use this same Python code and execute it both on CPUs, GPUs, and TPUs. This provides language and hardware portability. TensorFlow Lite provides on-device inference of ML models on mobile devices and is available for a variety of hardware.

- TensorFlow API Hierarchy

    ![image](https://github.com/user-attachments/assets/39ccb97d-bc0b-4744-bbbd-1fa0ee5ddf9b)

- TensorFlow has the ability to calculate the partial derivative of any function with respect to any variable.
    - The computation is recorded with GradientTapee

      ![image](https://github.com/user-attachments/assets/4708d71f-7e43-461b-9e44-70f234df4c37)
      ![image](https://github.com/user-attachments/assets/09063960-8ae3-4861-a022-69469cb7ba38)


    - the function is expressed with TensorFlow operations only.









