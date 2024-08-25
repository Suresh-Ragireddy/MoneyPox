

# Azure Pox: A Microsoft Azure Custom Vision Model for Monkeypox and Skin Lesion Prediction
##  Website link  [Monkeypox Prediction Web App](https://monkeypox.streamlit.app/).
https://monkeypox.streamlit.app/
## Overview

**Azure Pox** is a machine learning model developed using Microsoft Azure Custom Vision for the prediction of Monkeypox and other similar skin conditions. The model is trained on a comprehensive dataset, the **Mpox Skin Lesion Dataset Version 2.0 (MSLD v2.0)**, which includes over 9,500 images across six distinct classes: Monkeypox, Chickenpox, Measles, Cowpox, HFMD (Hand, Foot, and Mouth Disease), and Healthy skin.

## Project Features

- **Dataset**:
  - Trained on 9,500+ images sourced from the [Mpox Skin Lesion Dataset v2.0](https://www.kaggle.com/datasets/joydippaul/mpox-skin-lesion-dataset-version-20-msld-v20).
  - The dataset includes six classes: Mpox, Chickenpox, Measles, Cowpox, HFMD, and Healthy skin.
  
- **Model Performance**:
  - Achieved a **Precision** of 93.3%, **Recall** of 91.0%, and an **Average Precision (AP)** score of 97.6%.
  - These metrics demonstrate the model's high accuracy and reliability in classifying various skin conditions.

- **Web Interface**:
  - Developed and deployed using the **Streamlit** framework for real-time image prediction.
  - The web interface allows users to upload images directly and receive instant predictions, complete with detailed result metrics.
  - Sample images are provided within the interface to guide users on the types of images to upload for the most accurate results.
  - The web app is accessible at [Monkeypox Prediction Web App](https://monkeypox.streamlit.app/).

## How to Use

1. **Visit the Web App**: Navigate to [Monkeypox Prediction Web App](https://monkeypox.streamlit.app/).
2. **Select a Sample Image**: Browse through the provided sample images to understand the type of images suitable for prediction.
3. **Upload Your Image**: Use the "Upload Image" tab to upload your own image for prediction.
4. **View Results**: The model will predict the skin condition and display the results with performance metrics.

## Dataset

The **Mpox Skin Lesion Dataset v2.0 (MSLD v2.0)** used in this project can be accessed at the following link: [MSLD v2.0 Dataset on Kaggle](https://www.kaggle.com/datasets/joydippaul/mpox-skin-lesion-dataset-version-20-msld-v20).

## Project Files

This repository contains all the necessary files to replicate the project, including:
- Custom Vision training scripts.
- Model weights and performance logs.
- Streamlit app code.
- Deployment scripts.

## Web Interface Images

The following images showcase the web interface, guiding you through the process:
- **Homepage**: Displays the main features and options for image selection and upload.
  ![image](https://github.com/user-attachments/assets/4705918b-300f-411a-99fa-50c5638ef6e7)

  
- **Sample Image Selection**: Shows the provided sample images to help users select the correct type of image.
  ![image](https://github.com/user-attachments/assets/a0768684-2f06-4507-8c53-f2347553c36c)

  
- **Upload Image Interface**: The section where users can upload their own images for prediction.
  ![image](https://github.com/user-attachments/assets/a8ee2eaf-2dfb-447c-8773-083a5eb288d6)


- **Prediction Results**: Displays the predicted results along with performance metrics.
![image](https://github.com/user-attachments/assets/90e6268f-68e7-4784-b2fd-5d10ac4600cf)

#Sample Tests
- **Test case 1**:
 ![image](https://github.com/user-attachments/assets/3f310cfd-cb1a-4472-b739-25ba4e8554ed)

- **Test case 2**:
 ![image](https://github.com/user-attachments/assets/f76a83d7-1710-4722-8ade-cab57962e919)

- **Test case 3**:
 ![image](https://github.com/user-attachments/assets/9c499ada-0035-4c6a-98ce-64327bec8c9e)


## Conclusion

**Azure Pox** is a powerful tool leveraging Microsoft's Custom Vision to assist in the early and accurate detection of Monkeypox and similar skin conditions. By integrating a user-friendly web interface and training the model on a diverse dataset, this project aims to provide a reliable solution for medical professionals and individuals alike.

For any further inquiries or contributions, please feel free to open an issue or submit a pull request.

## Contributions
Contributions to this project are welcome. Feel free to fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License, which allows you to freely use, distribute, share, copy, and modify the content. Feel free to adapt the material for your own learning or to share with others. For more detailed information, see the [LICENSE](LICENSE) file.


## Contact
If you have any questions or feedback, feel free to reach out via email at sureshragireddy6@gmail.com.
