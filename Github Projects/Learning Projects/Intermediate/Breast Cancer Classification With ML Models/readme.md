# 📊 Breast Cancer Classification with Scikit-Learn

## 📜 Description

**Breast Cancer Classification** is a machine learning project built with **scikit-learn** that demonstrates binary classification techniques using the Wisconsin Breast Cancer dataset.

The goal is to practice and improve understanding of:
- 🔬 Data preprocessing (train-test split, feature scaling)
- 🤖 Training multiple ML models
- 📈 Comparing performance using confusion matrices, classification reports, and accuracy metrics

This project uses the **Breast Cancer Wisconsin dataset** (built into scikit-learn) to classify tumors as **benign** or **malignant**.

> **Note**: This project is for educational purposes and machine learning practice only.

---

## ⚙️ Requirements

- **Python 3.9+**
- **Required Libraries**:
  - `numpy`
  - `pandas` 
  - `matplotlib`
  - `scikit-learn`

### Installation

Install all required dependencies with:

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## 📂 Dataset

No external dataset required — scikit-learn provides the breast cancer dataset. The script automatically:
- Loads the Wisconsin Breast Cancer dataset
- Splits the dataset into training (80%) and testing (20%) sets
- Standardizes features using `StandardScaler`

---

## 🛠️ How It Works

1. **Data Loading**: Loads the breast cancer dataset from scikit-learn
2. **Data Splitting**: Divides data into training (80%) and testing (20%) sets
3. **Feature Scaling**: Applies `StandardScaler` for feature normalization
4. **Model Training**: Trains six different classification models:
   - 🧑‍🤝‍🧑 K-Nearest Neighbors (KNN)
   - 📈 Logistic Regression
   - 🌳 Decision Tree
   - 🌀 Support Vector Classifier (SVC)
   - 🌲 Random Forest
   - 🎲 Gaussian Naive Bayes

5. **Model Evaluation**: Evaluates each model using:
   - Confusion Matrix
   - Classification Report (precision, recall, F1-score)
   - Accuracy Score

6. **Visualization**: Creates a bar chart comparing all model accuracies

---

## ▶️ How To Run

1. Save the script as `breast_cancer_classification.py`
2. Run in terminal:

```bash
python breast_cancer_classification.py
```

The script will:
- Print confusion matrices and classification reports for each model
- Display accuracy scores
- Show a comparative bar chart of all models

---

## 📊 Example Output

```
=== Logistic Regression ===
Confusion Matrix:
[[71  2]
 [ 2 39]]

Classification Report:
              precision    recall  f1-score   support

           0       0.97      0.97      0.97        73
           1       0.95      0.95      0.95        41

    accuracy                           0.96       114
   macro avg       0.96      0.96      0.96       114
weighted avg       0.96      0.96      0.96       114

Accuracy: 0.9649
```

📌 The final bar chart visualization shows which model performs best on this dataset.

---

## 👨‍💻 Developer  
Created by Evan William (2025)  
Version: 1.0
