import joblib
from features.extract_features import extract_features

# Load trained model
model = joblib.load('emotion_model.pkl')

# Test on one audio file
file_path = 'audio_files/sample.wav'  # Replace with your test file
features = extract_features(file_path)

if features is not None:
    features = features.reshape(1, -1)
    prediction = model.predict(features)
    print("Predicted Emotion:", prediction[0])
else:
    print("Feature extraction failed.")