🎙️ Speech Emotion Recognition (SER) 

\- This project is a complete end-to-end Speech Emotion Recognition system that classifies    human emotions from audio recordings using machine learning. The system includes:

&nbsp;   1. A trained deep learning model to recognize emotions from audio

&nbsp;   2. A Flask-based web application with endpoints for uploading audio and receiving predictions

&nbsp;   3. A frontend interface to interact with the system



📂 Project Structure

├── app.py           

├── model.h5               

├── templates/

│   ├── index.html

│   ├── demo.html

│   ├── about.html

│   └── technical.html

├── uploads/                

└── README.md               



🧠 Model Details

\- Input: .wav audio file (up to 4 seconds)

\- Feature Extraction: 40 MFCCs with fixed length (173 frames)

\- Model Type: Hybrid Model CNN+BiLSTM

\- Output Classes:

&nbsp;   1. Angry

&nbsp;   2. Calm

&nbsp;   3. Disgust

&nbsp;   4. Fearful

&nbsp;   5. Happy

&nbsp;   6. Neutral

&nbsp;   7. Sad

&nbsp;   8. Surprised



🌐 Web Application Features

\- Upload an audio file and get emotion prediction

\- Confidence score for the predicted emotion

\- Beautifully designed frontend pages:

&nbsp;   1. Home

&nbsp;   2. Technical Details

&nbsp;   3. Demo

&nbsp;   4. About



🎧 How it Works

\- User uploads a .wav audio file through the web interface.

\- Flask (app.py):

&nbsp;   1. Saves and preprocesses the audio (MFCC feature extraction)

&nbsp;   2. Loads the trained model and makes predictions

&nbsp;   3. Returns emotion and confidence

&nbsp;   4. Results are displayed on the frontend.



📊 Model Training

\- The model was trained using MFCC features extracted from labeled datasets (e.g., RAVDESS, CREMA-D). Training includes:

\- Balancing dataset 

\- Data augmentation

\- Normalization

\- Stratified splits

\- Early stopping and tuning



🎯Accuracy

Test Accuracy: 94.48%



Classification Report:

&nbsp;             precision    recall  f1-score   support



&nbsp;      angry       0.96      0.99      0.97        77

&nbsp;       calm       1.00      0.97      0.99        77

&nbsp;    disgust       0.94      0.87      0.91        77

&nbsp;    fearful       0.87      0.90      0.88        77

&nbsp;      happy       0.97      0.96      0.97        77

&nbsp;    neutral       0.89      0.96      0.93        77

&nbsp;        sad       0.93      0.96      0.94        77

&nbsp;  surprised       1.00      0.95      0.97        77



&nbsp;   accuracy                           0.94       616

&nbsp;  macro avg       0.95      0.94      0.94       616

weighted avg       0.95      0.94      0.94       616

