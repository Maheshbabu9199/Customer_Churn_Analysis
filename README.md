

# Customer Churn Prediction

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contact](#contact)

## Introduction
Customer churn prediction is an essential aspect of customer relationship management, helping businesses identify customers who are likely to leave. By using machine learning algorithms, specifically the RandomForest classifier, this project aims to predict customer churn with high accuracy. The project is implemented in Python 3.10 and utilizes the Streamlit framework to create an interactive web application for users to easily input data and view predictions. The modular code structure ensures the project is maintainable and scalable..

## Features
- Predict customer churn using a trained RandomForest model.
- Interactive web interface built with Streamlit.
- Modular code structure for ease of maintenance and scalability.
- Detailed visualizations and insights from the model predictions.

## Installation
Follow these steps to set up and run the project locally.

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Maheshbabu9199/Customer_Churn_Prediction.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd customer-churn-prediction
   ```

3. **Create a virtual environment:**
   ```sh
   python3.10 -m venv venv
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

5. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

6. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

## Usage
1. Open your web browser and go to `http://localhost:8501`.
2. Upload your customer data file in the required format.
3. Click on the "Predict" button to see the churn prediction results.
4. Explore the visualizations and insights provided by the app.

## Project Structure
The project is organized into the following modules:

```
customer-churn-prediction/
├── data/
│   └── dataset
├── src/
│   └── components/
│   └── utils/
│   └── entity_config/
│   └── config/
│   └── pipelines/
├── app.py
├── requirements.txt
└── setup.py
└── README.md

```

## Contact
Created by Maheshbabu Boggu - feel free to contact me!

---

Feel free to customize this template further to match your project's specifics and add any additional sections that might be necessary.
