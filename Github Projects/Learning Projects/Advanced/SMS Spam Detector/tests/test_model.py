import pytest
import pandas as pd
import numpy as np
from spam_detector.model import SpamDetector
from spam_detector.data_handler import load_data

@pytest.fixture(scope="module") # the file contains the test suite for the spam detector model.
def sample_data():
    # small & consisten df for testing
    data = {
        'label': ['ham', 'spam', 'ham', 'spam'],
        'message': [
            "Hey, what's up?",
            "Claim your free prize now!",
            "Let's meet tomorrow.",
            "URGENT: call this number for your reward"
        ]
    }
    return pd.DataFrame(data)

@pytest.fixture(scope="module")
def trained_model(sample_data):
    # provides spamdetector model instance that is traiend
    model = SpamDetector()
    X_train, y_train = sample_data['message'], sample_data['label']
    model.train(X_train, y_train)
    return model

# --- Test Cases ---
def test_model_initialization():
    # test 1. check if spam detector initializes correctly, to ensure constructor and pipeline setup work as excpected (basic sanity check)
    model = SpamDetector()
    assert model.model is not None, "Model pipeline should be initialized."
    assert 'vectorizer' in model.model.named_steps, "Vectorizer step should exist."
    assert 'classifier' in model.model.named_steps, "Classifier step should exist."

def test_model_training(trained_model):
    # test 2. check if model is trained and internal state is up to date!, cause a trained model should have fitted attributes
    # this to confirm fit() as succesful and the model learn ATLEAST SOMETHING FROM THE DATA
    # after training, the vectorizer should have built a vocabulary.
    vocab = trained_model.model.named_steps['vectorizer'].vocabulary_
    assert len(vocab) > 0, "Vectorizer should have a vocabulary after training."
    
    # naive bayes classifired should hav class counts!
    class_counts = trained_model.model.named_steps['classifier'].class_count_
    assert len(class_counts) == 2, "Classifier should be trained on two classes (ham, spam)."
    assert class_counts[0] > 0 and class_counts[1] > 0

def test_ham_prediction(trained_model):
    # test 3. ensure a clearly non spam msg to be classified as 'ham', this to ensure a funcitonality for one of the primary classes
    ham_message = ["Hi, are you available for a meeting tomorrow?"]
    prediction = trained_model.predict(ham_message)
    assert prediction[0] == 'ham', "A normal message should be classified as 'ham'."

def test_spam_prediction(trained_model):
    # test 4. unlike above, this ensure a clearly SPAMMY msg to be classified as 'spam'
    spam_message = ["Free prize! claim your reward now!"]
    prediction = trained_model.predict(spam_message)
    assert prediction[0] == 'spam', "An obvious spam message should be classified as 'spam'."

def test_prediction_output_type_and_shape(trained_model):
    # test 5. check the data type and shape of the prediction output, so that model output is consisdent, the dwnstream systems
    # depends on the output being a predictable type and size
    messages = ["test message 1", "test message 2", "another test"]
    predictions = trained_model.predict(messages)
    assert isinstance(predictions, np.ndarray), "Prediction output should be a numpy array."
    assert predictions.shape == (3,), "Prediction array shape should match number of inputs."

def test_predict_proba_output(trained_model):
    # test 6. checks the ouput of probability prediciton methods, cuz probabilities is often more used for more nuancced decision,
    # they MUST BE VALID, in example (sum to 1 and have correct shape)
    message = ["call for free prize"]
    probabilities = trained_model.predict_proba(message)
    
    assert isinstance(probabilities, np.ndarray), "Probabilities should be a numpy array."
    assert probabilities.shape == (1, 2), "Shape should be (n_samples, n_classes)."
    assert np.isclose(np.sum(probabilities[0]), 1.0), "Probabilities for a prediction should sum to 1."

def test_data_loader(tmp_path):
    # test 7. checks the data_handler's load_data func, ensuring it correctly reads and handle the csv well
    # `tmp_path` is a special pytest fixture that provides a temporary directory.
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test_data.csv"
    p.write_text("label,message\nham,hello world\nspam,buy now")
    
    features, labels = load_data(p)
    
    assert len(features) == 2
    assert len(labels) == 2
    assert features[0] == "hello world"
    assert labels[1] == "spam"
    
def test_data_loader_file_not_found():
    # test 8. ensure the data loader raise a correct error if file is misisng
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file.csv")

def test_data_loader_bad_columns(tmp_path):
    # test 9. ensure the data loader raise error if a csv is malformed, wrong format will ruin the model
    p = tmp_path / "bad_data.csv"
    p.write_text("header1,header2\nval1,val2")
    
    with pytest.raises(ValueError, match="must contain 'label' and 'message'"):
        load_data(p)

