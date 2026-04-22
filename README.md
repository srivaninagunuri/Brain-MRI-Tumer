# 🧠 Brain Tumor Classification using MobileNetV2

## 📌 Project Overview
This project focuses on classifying brain MRI images into four categories using a deep learning model (MobileNetV2):

- Glioma Tumor  
- Meningioma Tumor  
- Pituitary Tumor  
- No Tumor  

The model is trained using transfer learning with MobileNetV2 to achieve efficient and accurate medical image classification.

---

## 🏗️ Model Architecture
- Base Model: MobileNetV2 (Pretrained on ImageNet)
- Approach: Transfer Learning
- Framework: TensorFlow / Keras
- Input Image Size: (224 x 224 x 3)
- Activation: Softmax (Multi-class classification)

---

## 📊 Dataset
The dataset consists of labeled brain MRI images categorized into four classes:
- Glioma Tumor
- Meningioma Tumor
- Pituitary Tumor
- No Tumor

Preprocessing steps:
- Image resizing
- Normalization
- Data augmentation (rotation, flipping, zooming)

---

## ⚙️ Training Details
- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Metrics: Accuracy
- Epochs: (based on training configuration)
- Batch Size: (your value)

---

## 📈 Model Performance

### Confusion Matrix (MobileNetV2)

Below is the confusion matrix showing model performance across all classes:

![Confusion Matrix](efbe28a3-f3c3-4723-87f9-3cfed1b37863.png)

### 🔍 Observations:
- Good performance on **No Tumor** and **Pituitary Tumor**
- Some misclassification between **Glioma** and **Meningioma**
- Model can be further improved using fine-tuning or advanced augmentation

---

## 📦 Installation

```bash
git clone https://github.com/your-username/brain-tumor-classification.git
cd brain-tumor-classification
pip install -r requirements.txt
