import streamlit as st
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from PIL import Image
import os
import config  # Import the config file

# Initialize Azure Custom Vision client using the variables from config.py
credentials = ApiKeyCredentials(in_headers={"Prediction-key": config.PREDICTION_KEY})
predictor = CustomVisionPredictionClient(config.ENDPOINT, credentials)

# Streamlit app title
st.title("Monkeypox Prediction")

# Add a message about the predictions
st.markdown("""
**This model can predict the following conditions:**

- Monkeypox
- Chickenpox
- Measles
- Cowpox
- Hand, Foot and Mouth Disease (HFMD)
- Healthy

Select a sample image or upload your own to see if it matches any of these conditions. The prediction results will be displayed based on the selected or uploaded image.
""")
# Define the tabs
tab1, tab2 = st.tabs(["Sample Images", "Upload Image"])

# Tab 1: Sample Images
with tab1:
    with st.sidebar:
        st.header("Select a Sample Image")

        # List all images in the sample_images folder
        sample_images_folder = "sample_images"
        sample_images = os.listdir(sample_images_folder)

        # Display images in a grid layout
        cols = st.columns(2)  # Adjust based on how many images to show per row
        selected_image = st.session_state.get('selected_image', None)  # Retrieve selected image from session state

        for i, image_file in enumerate(sample_images):
            image_path = os.path.join(sample_images_folder, image_file)
            img = Image.open(image_path)

            with cols[i % 2]:  # Adjust to match the columns defined above
                # Label for selecting image
                if st.button(f"Image {i + 1}", key=f"label_{i}"):
                    st.session_state.selected_image = image_file  # Store the selected image in session state
                    st.session_state.selected_image_path = image_path  # Also store the image path
                    # No need for st.experimental_rerun() here; Streamlit will re-render on state change

                # Display images as thumbnails
                st.image(img, caption=f"Image {i + 1}", use_column_width=True)

    # Main area for displaying selected image and results
    st.header("Selected Image and Analysis")
    if 'selected_image' in st.session_state:
        selected_image_path = st.session_state.selected_image_path
        with open(selected_image_path, "rb") as image_file:
            image_contents = image_file.read()

        # Display selected image in a large size
        st.image(Image.open(selected_image_path), caption="Selected Image", use_column_width=True)

        # Predict using the selected image
        st.write("Running prediction...")
        results = predictor.classify_image(config.PROJECT_ID, config.PUBLISH_ITERATION_NAME, image_contents)

        # Display prediction results
        st.write("Results:")
        for prediction in results.predictions:
            st.write(f"{prediction.tag_name}: {prediction.probability * 100:.2f}%")

# Tab 2: Upload Image
with tab2:
    st.header("Upload Your Own Image")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        # Get the image contents as a byte array
        image_contents = uploaded_file.getvalue()

        # Predict using the uploaded image
        st.write("Running prediction...")
        results = predictor.classify_image(config.PROJECT_ID, config.PUBLISH_ITERATION_NAME, image_contents)

        # Display prediction results
        st.write("Results:")
        for prediction in results.predictions:
            st.write(f"{prediction.tag_name}: {prediction.probability * 100:.2f}%")
