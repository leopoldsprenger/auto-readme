# OCR AI Method Comparison

## Project Overview

This project compares Optical Character Recognition (OCR) using a Genetic Algorithm-based AI and a Gradient Descent-based AI. Developed as a science project, it evaluates how these AI methods recognize handwritten digits from the MNIST dataset.

*   [Neural Network Architecture](#neural-network-architecture)
*   [Installation](#installation)
*   [Usage](#usage)
*   [License](#license)

## What it Does

This repository provides implementations of two distinct approaches to Optical Character Recognition (OCR) for handwritten digits:

*   **Gradient Descent:** A traditional neural network trained using backpropagation and stochastic gradient descent.
*   **Genetic Algorithm:** A neural network whose weights are evolved using a genetic algorithm, mimicking natural selection.

The project aims to compare the performance and characteristics of these two methods on the MNIST dataset.

## Demo

While a live demo isn't available, the repository contains example images showcasing the model's predictions:

*   **Gradient Descent Predictions:** `result_images/gradient_descent/gradient_descent_test_dataset_predictions.png`
*   **Accuracy Comparison:** `result_images/accuracy_comparison_gradient_descent_and_genetic_algorithm.png`

## Neural Network Architecture <a name="neural-network-architecture"></a>

Both the genetic algorithm and the gradient descent approaches use a similar feedforward neural network architecture.  The `NeuralNetwork` class (defined in both `genetic_algorithm.py` and `gradient_descent.py`, although potentially simplified in the former) defines the structure. Here's a breakdown:

1.  **Input Layer:** Accepts the flattened MNIST image (28x28 pixels = 784 input features).
2.  **Hidden Layers:** One or more fully connected (linear) layers. ReLU (Rectified Linear Unit) activation functions are applied after each hidden layer. The ReLU function introduces non-linearity, enabling the network to learn complex patterns.
3.  **Output Layer:** A fully connected layer with 10 outputs, corresponding to the 10 digit classes (0-9).
4.  **Forward Pass:** During prediction, the input data flows through the network. Each layer performs a matrix multiplication of the input with its weights, adds a bias, and applies the activation function (ReLU for hidden layers). The final output layer produces a vector of scores, one for each digit class.

The key difference between the two approaches lies in how the weights of these layers are *learned*:

*   **Gradient Descent:** Uses backpropagation and an optimizer (like Stochastic Gradient Descent - SGD) to iteratively adjust the weights to minimize a loss function (CrossEntropyLoss). The `train_model` function in `gradient_descent.py` handles this process.
*   **Genetic Algorithm:**  Treats the weights as genes in a population of neural networks. The algorithm evolves the population through selection, crossover (combining weights from parent networks), and mutation (randomly changing weights) to find networks with high accuracy.  The `genetic_algorithm` function in `genetic_algorithm.py` implements this.

## Installation <a name="installation"></a>

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/leopoldsprenger/ocr-ai-method-comparison.git
    cd ocr-ai-method-comparison
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install torch torchvision matplotlib
    ```

## Usage <a name="usage"></a>

### Running the Gradient Descent Model

1.  **Train the model (or use the pre-trained model):**

    The `gradient_descent.py` file contains functions to train the model and save the weights. It also loads and saves using functions from `data_manager.py`.

    ```bash
    python gradient_descent.py
    ```

    This will train the model from scratch.  You can use the pre-trained model located at `saved_models/gradient_descent.pt` by specifying a path to the load function:

    ```python
    # Example in gradient_descent.py
    from data_manager import load_model
    # Initialize your neural network model
    model = NeuralNetwork()  # Replace with your actual NeuralNetwork class
    load_model(model, 'saved_models/gradient_descent.pt')
    ```

2.  **Test the model:**

    The script also contains functions to evaluate the trained model on the test dataset and visualize predictions (as shown in `result_images/gradient_descent/gradient_descent_test_dataset_predictions.png`).  This is done automatically at the end of the `gradient_descent.py` script.

### Running the Genetic Algorithm Model

1.  **Run the genetic algorithm:**

    ```bash
    python genetic_algorithm.py
    ```

    This will evolve a population of neural networks using the genetic algorithm.  The best-performing model's weights can be saved (and are saved automatically to `saved_models/genetic_algorithm.pt`).

2.  **Evaluate the best model:**

    The `genetic_algorithm.py` script includes testing functionality to assess the performance of the evolved model and visualize its predictions.

### Data Management

The `data_manager.py` file provides functions for loading and saving PyTorch models (`.pt` files). It is used by both `gradient_descent.py` and `genetic_algorithm.py`.

*   `save_model`: Saves the model's weights to a specified file path.
    ```python
    from data_manager import save_model
    save_model(model, 'path/to/save/your/model.pt')
    ```

*   `load_model`: Loads the model's weights from a specified file path into an existing neural network object.
    ```python
    from data_manager import load_model
    model = NeuralNetwork() # Ensure model is properly initialized before loading
    load_model(model, 'path/to/saved/model.pt')
    ```

## Why it's Useful

This project offers several benefits:

*   **Educational:** Provides a hands-on comparison of two fundamentally different AI approaches (gradient descent vs. genetic algorithms) to the same problem.
*   **Practical:** Demonstrates how to implement and train neural networks for OCR using both techniques.
*   **Modular:** The code is organized into separate files for data management, gradient descent, and genetic algorithm, promoting reusability and maintainability.
*   **Extensible:** Can be extended to explore different network architectures, hyperparameters, and optimization strategies.

## License <a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
