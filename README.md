# **Forecasting Exam Scores Based on Study Hours**

## **Project Description**
This project aims to predict students' exam scores based on the number of hours they study, using a linear regression model. The goal is to help students understand the relationship between their study time and expected exam performance, allowing them to make informed decisions about how much time they need to study to achieve their desired scores.

## **Business Problem**
The business problem addressed by this project is the ability to predict student exam scores based on the number of study hours they commit. By understanding how study hours correlate with performance, students can adjust their study habits to maximize their academic results.

The project can provide:
- Expected exam scores for a given number of study hours.
- Insights into the minimum study hours needed for passing or achieving a high score.
- Guidance on how students can manage their time more effectively to meet their academic goals.

## **Data**
The data used in this project comes from a CSV file called `student_info.csv`. It contains information about students' study hours and their corresponding exam scores. The dataset is cleaned and processed to ensure that missing values are handled and the features are prepared for use in machine learning.

## **Libraries Used**
- **numpy**: For numerical operations
- **pandas**: For data manipulation and analysis
- **matplotlib**: For data visualization
- **scikit-learn**: For machine learning algorithms
- **joblib**: For saving and loading the model

## **Steps Involved**
1. **Data Cleaning**: Handle missing values and prepare the dataset for machine learning.
2. **Exploration and Visualization**: Visualize the relationship between study hours and exam scores using scatter plots.
3. **Model Training**: Use linear regression to create a model that predicts exam scores based on study hours.
4. **Evaluation**: Evaluate the model's performance using metrics such as accuracy, mean squared error (MSE), and mean absolute error (MAE).
5. **Prediction**: Deploy the model using Streamlit, where users can input study hours and get predicted exam scores.

## **How to Run the Application**

### Prerequisites:
Ensure that the following Python packages are installed:
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `streamlit`
- `joblib`

You can install the required packages using pip:
```bash
pip install numpy pandas matplotlib scikit-learn streamlit joblib
```

### Steps:
1. Clone the repository or download the project files.
2. Make sure that the `student_info.csv` file is in the same directory.
3. Run the Streamlit app by executing the following command in your terminal:
```bash
streamlit run app.py
```

4. Once the app is running, enter the number of study hours to predict the exam score.

## **Model Evaluation**
- **Accuracy**: The model achieves a certain accuracy score based on the test dataset.
- **Mean Squared Error (MSE)**: Measures the average of the squared differences between predicted and actual values.
- **Mean Absolute Error (MAE)**: Measures the average of the absolute differences between predicted and actual values.

## **Files in the Project**
- `student_info.csv`: The dataset containing student study hours and exam scores.
- `Forecasting_Exam_Scores_Based_on_Study_Hours.pkl`: The saved machine learning model.
- `app.py`: The Streamlit app file for deploying the model as a web application.
- `README.md`: This file.

## **About the Developer**
**Anubhav Kumar Tiwary**  
This project was developed by Anubhav Kumar Tiwary. If you have any questions or suggestions, feel free to reach out.
