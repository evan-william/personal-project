from spam_detector.data_handler import load_data
from spam_detector.model import SpamDetector

def run_demo(): # trains the model from the data/spam.csv and predict examples messages, SEE BELOW!
    print("--- Running Spam Detector Demo ---")

    # 1. loading the spam data sets
    data_path = 'data\spam.csv'
    print(f"\n[1] Loading data from '{data_path}'...")
    try:
        features, labels = load_data(data_path)
        print(f"    Data loaded successfully. Found {len(features)} messages.")
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"    Error: Could not load data. {e}")
        return

    # 2. initializes the models and trains it !
    print("\n[2] Training the Spam Detector model...")
    detector = SpamDetector()
    detector.train(features, labels)
    print("    Model training complete.")

    # 3. make predictions on new unseen before data !
    print("\n[3] Making predictions on new messages:")
    new_messages = [
        "Congratulations! You've won a $1,000 Walmart gift card. Go to http://example.com to claim now.",
        "Hey mom, I'm going to be late for dinner tonight. See you in a bit.",
        "URGENT: Your account has been suspended due to suspicious activity. Please click here to reactivate.",
        "Can you pick up some milk and bread on your way home?",
        "Final Reminder: Exclusive deal! Buy one get one free. Don't miss out on this prize."
    ]

    predictions = detector.predict(new_messages)

    for msg, pred in zip(new_messages, predictions):
        # visual difference between spam & ham
        marker = "🚨 SPAM" if pred == "spam" else "✅ HAM"
        print(f'\n  Message: "{msg}"')
        print(f'    -> Prediction: {marker}')

    print("\n--- Demo Finished ---")

if __name__ == '__main__':
    run_demo()

