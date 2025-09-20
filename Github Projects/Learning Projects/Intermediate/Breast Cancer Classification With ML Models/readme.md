# Breast Cancer Classification

A machine learning project comparing different classification algorithms on the Wisconsin Breast Cancer dataset to practice binary classification techniques.

## What This Project Does

This is a straightforward classification exercise using the built-in breast cancer dataset from scikit-learn. I wanted to get hands-on experience with different ML algorithms and see how they perform on the same medical dataset.

The goal was to practice the full pipeline: data preprocessing, model training, and evaluation. It compares six different algorithms to see which ones work best for distinguishing between benign and malignant tumors.

## Learning Goals

- Practice data preprocessing and feature scaling
- Train multiple classification models
- Compare model performance using proper metrics
- Understand confusion matrices and classification reports
- Get familiar with scikit-learn's workflow

## Requirements

- Python 3.9+
- Standard ML libraries:
  - `numpy`
  - `pandas` 
  - `matplotlib`
  - `scikit-learn`

Install with:
```bash
pip install numpy pandas matplotlib scikit-learn
```

## Dataset

Uses the Wisconsin Breast Cancer dataset that comes with scikit-learn. It has 569 samples with 30 features each, measuring things like cell size, texture, and shape. The target is binary: benign (0) or malignant (1).

No need to download anything - the script loads it automatically.

## How It Works

Pretty standard ML pipeline:

1. Load the breast cancer dataset
2. Split into training (80%) and testing (20%) sets
3. Scale features using StandardScaler
4. Train six different models:
   - K-Nearest Neighbors
   - Logistic Regression
   - Decision Tree
   - Support Vector Classifier
   - Random Forest
   - Gaussian Naive Bayes
5. Evaluate each model with confusion matrices and classification reports
6. Compare accuracies in a bar chart

## Running the Code

Save the script and run:
```bash
python breast_cancer_classification.py
```

It will print detailed results for each model and show a comparison chart at the end.

## Sample Output

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

Accuracy: 0.9649
```

The confusion matrix shows true negatives, false positives, false negatives, and true positives. The classification report breaks down precision, recall, and F1-score for each class.

## What I Learned

- Different algorithms perform surprisingly similarly on this dataset
- Feature scaling makes a big difference for some models (like SVC and KNN)
- Random Forest and Logistic Regression tend to perform well out of the box
- Medical datasets often have good class separation, leading to high accuracy scores

## Limitations

This is a pretty clean, well-known dataset, so results are probably better than you'd see with messier real-world data. Also, I'm just using default hyperparameters - tuning them would likely improve performance.

The comparison is fairly basic too - just accuracy scores. A more thorough analysis would look at precision/recall tradeoffs, especially for medical applications where false negatives are costly.

## Possible Improvements

- Try hyperparameter tuning
- Feature importance analysis

## Author

**Evan William**  
Version 1.0 (2025)

Built this to practice classification algorithms and get comfortable with scikit-learn. Medical datasets are interesting to work with because the stakes feel more real.

The breast cancer dataset is a classic in ML education - good for learning the basics before moving on to messier, more complex problems.

---

*Educational project only for my own test*
