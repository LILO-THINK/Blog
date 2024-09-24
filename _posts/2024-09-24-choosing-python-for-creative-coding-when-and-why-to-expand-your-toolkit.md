---
layout: post
title: Choosing Python for Creative Coding - When and Why to Expand Your Toolkit
id: 2024-09-24-choosing-python-for-creative-coding-when-and-why-to-expand-your-toolkit.md
categories:
  - creative process
  - digital tools
image: https://live.staticflickr.com/65535/54019232579_8751b63ec2_o.png
share: "true"
comments: "true"
filename: Blog/_posts/2024-09-24-choosing-python-for-creative-coding-when-and-why-to-expand-your-toolkit.md
tags:
  - python
  - tutorial
date: 2024-09-24
author: lina
---
Creative coding is a vibrant field where art meets programming, allowing creators to produce expressive and interactive digital works. While JavaScript has long been a go-to language for me in this space, especially for web-based projects, Python emerges as a powerful alternative worth considering. **When should you choose Python for your creative coding projects?**

In this post, we'll delve into scenarios where Python can enrich your creative coding endeavors. We'll explore how expanding your toolkit with Python — and specifically with Py5 — can open up new possibilities. Additionally, we'll guide you through setting up Py5 in a macOS environment using Visual Studio Code and Jupyter Notebook, highlighting how Py5's syntax, reminiscent of Processing, can streamline your creative process.

## Why Choose Python for Creative Coding?

**1. Simplicity and Readability**

- **Python** is renowned for its clean and straightforward syntax, making it easier to read and write code.
- This simplicity accelerates the learning curve for beginners and enhances productivity for experienced coders.

**2. Rich Scientific and Mathematical Libraries**

- Python boasts extensive libraries like **NumPy**, **SciPy**, and **Pandas**, which are invaluable for computational art involving complex mathematics or data manipulation.
- These tools enable artists to incorporate advanced algorithms and data-driven visuals into their work.

**3. Integration with Machine Learning and AI**

- With libraries such as **TensorFlow** and **PyTorch**, Python excels in machine learning and artificial intelligence.
- This integration allows for the creation of generative art and interactive installations powered by AI.

**4. Versatile Development Environments**

- Python supports environments like **Jupyter Notebook**, facilitating an interactive coding experience.
- These environments are ideal for experimentation and iterative development, crucial aspects of creative coding.

**5. Processing Capabilities with Py5**

- **Py5** brings the power of the Processing graphics library to Python, combining ease of use with advanced features.
- This synergy allows artists to leverage Processing's simplicity while enjoying Python's robustness.

---
<img src="https://live.staticflickr.com/65535/54019232579_8751b63ec2_o.png" width="100%" alt="Screenshot 2024-09-24 at 19.44.10"/>

## Setting Up Py5 with Visual Studio Code and Jupyter Notebook on macOS

To harness the power of Py5 for your creative projects, follow this step-by-step guide to set up your development environment on macOS.

### Prerequisites

- **Python 3.10 or higher** installed on your system.
- **Visual Studio Code (VS Code)** installed.
- **Homebrew** (optional but recommended for managing installations).

### Step 1: Install Java Development Kit (JDK)

Py5 requires Java to function correctly.

1. **Install JDK 17 or higher**:
- Download and install from the [Oracle JDK Downloads](https://www.oracle.com/java/technologies/javase-jdk17-downloads.html) page.
- Alternatively, use Homebrew:
```bash
   brew install openjdk@17
```

2. **Configure JAVA_HOME Environment Variable**:
- Add the following line to your `~/.bash_profile` or `~/.zshrc` file:
```bash
export JAVA_HOME=$(/usr/libexec/java_home)
```

- Reload your terminal configuration:
```bash
source ~/.zshrc
```

### Step 2: Install Py5

Install Py5 using `pip`:
```bash
pip install py5
```

### Step 3: Install Visual Studio Code Extensions

Open VS Code and install the following extensions:

- **Python**: Provides rich support for Python.
- **Jupyter**: Enables Jupyter Notebook functionality within VS Code.

### Step 4: Set Up Jupyter Notebook in VS Code

1. **Create a New Jupyter Notebook**:
- Open the Command Palette (`Shift + Command + P`) and select **Jupyter: Create New Blank Notebook**.
2. **Configure the Notebook for Py5**:
- Before importing Py5, ensure the macOS event loop is activated by running:
```python
%gui osx
```

### Step 5: Write Your First Py5 Sketch

In a new cell, import Py5 and define your sketch functions:
```python
import py5

def setup():
    py5.size(400, 400, py5.P2D)
    py5.background(255)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 50)

def mouse_clicked():
    py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))

py5.run_sketch(block=False)
```

**Note**: The `block=False` parameter allows the sketch to run asynchronously within the notebook.

Sometimes, to kill the Java window, you can use this inside your Notebook:
```python
py5.exit_sketch()
```

### Step 6: Run the Sketch

- Execute the cells in order.
- A canvas should appear within your Jupyter Notebook, displaying the interactive sketch.

---

## The Familiar Syntax of Py5 and Processing

Py5 is designed to closely mirror the syntax of **Processing**, a flexible software sketchbook and language for learning how to code within the context of the visual arts.

**Benefits of Py5's Syntax Similarity**:

- **Ease of Transition**: Artists familiar with Processing can effortlessly switch to Py5 without a steep learning curve.
- **Community and Resources**: Leveraging Processing's vast community and resources becomes straightforward.
- **Educational Value**: The consistent syntax aids in teaching programming concepts within creative coding, making it accessible for educational purposes.

**Purpose in Creative Coding**:

- The syntax promotes a **minimalist and expressive coding style**, allowing artists to focus on creativity rather than technical complexities.
- Functions like `setup()`, `draw()`, and event handlers like `mouse_clicked()` provide a structured yet flexible framework for interactive art.

---
## Conclusion

Use Python if you prefer working locally, value a simple and readable syntax, or if you intend to integrate your work with data science tools, machine learning, or mathematical environments. Python is great for generative art projects requiring heavy computation or AI integration. It's always good to expand your creative coding toolkit to include Python and Py5.

If you're interested in expanding your creative coding skills with Python, I highly recommend Alexandre Villares course on Domestika:

**[Designing with Python: Programming for a Visual Context](https://www.domestika.org/en/courses/4307-designing-with-python-programming-for-a-visual-context/course)**

In this course, you'll learn how to create visual projects using Python, exploring techniques that combine programming and design to produce interactive and artistic works. It's a great opportunity to deepen your knowledge and discover new creative possibilities.