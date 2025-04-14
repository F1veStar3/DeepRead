# DeepRead

DeepRead is a neural network for handwriting recognition built on NLP and OpenCV. Using PyTorch, the model analyses the letters drawn by the user on a virtual canvas and instantly predicts them.

## Installation and Setup

### Prerequisites
Ensure you have Python installed along with the following dependencies:

```sh
pip install -r requirements.txt
```

### Running the Application

1. Clone the repository or copy the project files.
2. Ensure the `DeepReadModel.pt` file is in the project directory.
3. Run the script:

```sh
python main.py
```

4. A drawing canvas will appear. Use the left mouse button to draw and the right mouse button to clear the canvas.
5. Adjust the brush size using the mouse wheel.
6. The predicted letter will be displayed in the console.
7. Press `q` to exit the application.

## Technology Stack

- **Python** - Main programming language.
- **OpenCV** - For handling the drawing canvas and user interactions.
- **PyTorch** - For deep learning model inference.
- **NumPy** - For numerical operations and image processing.

This project demonstrates real-time DeepRead using deep learning and computer vision techniques.

