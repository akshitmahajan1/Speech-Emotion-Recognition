import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from features.extract_features import extract_features

DATA_PATH = 'audio_files'
X, y = [], []

for file in os.listdir(DATA_PATH):
    if file.endswith('.wav'):
        label = file.split('-')[2]  # Adjust this depending on your dataset
        features = extract_features(os.path.join(DATA_PATH, file))
        if features is not None:
            X.append(features)
            y.append(label)

X_train, X_test, y_train, y_test = train_test_split(np.array(X), y, test_size=0.2, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

joblib.dump(clf, 'emotion_model.pkl')
print("Model trained and saved as emotion_model.pkl")