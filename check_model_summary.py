from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('./model/deepfake_video_model.h5')

# Print the model architecture
model.summary()
