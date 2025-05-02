# ♻️ Eco Vision – Smart Waste Classifier with Azure & Streamlit

**Eco Vision** is a smart, AI-powered garbage classification system that helps users identify types of waste in real-time using images or camera input. Built with **Azure Custom Vision**, **MongoDB**, and **Streamlit**, this app not only predicts waste categories but also provides eco-friendly disposal tips, gathers user feedback, and maintains logs for continuous learning.

---

## 🚀 Features

- ✅ Classifies garbage into 6 categories: **Plastic**, **Paper**, **Glass**, **Metal**, **Cardboard**, and **Trash**
- 📸 Supports **image upload**, **camera capture**, and **image URL input**
- 🔍 Uses **Azure Custom Vision API** for accurate predictions
- 💬 Displays interactive **disposal tips** based on the prediction
- 🗳️ Collects **user feedback** ("Correct"/"Incorrect") to improve the model
- 📊 Logs predictions, feedback, and usage data into **MongoDB**
- 📚 Includes a **Home Page** explaining the importance of waste classification
- 🧠 Designed to be expandable — chatbot, dynamic tips, and more coming soon!

---

## 📦 Folder Structure

```
eco-vision/
├── app.py             # Main Streamlit app
├── azure_api.py       # Handles Azure Custom Vision prediction requests
├── database.py        # MongoDB logging and feedback utilities
├── utils.py           # Static disposal tips & helper functions
├── requirements.txt   # Required Python packages
└── README.md          # Project documentation
```

---

## 🧠 How It Works

1. User uploads an image, captures it from the camera, or pastes an image URL.
2. Image is sent to the **Azure Custom Vision API**.
3. The model returns predictions (e.g., `"Plastic: 94%"`).
4. The app displays:
   - The prediction result
   - Friendly disposal tips
   - A feedback form
5. All activity is logged in **MongoDB Atlas**.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/eco-vision.git
cd eco-vision
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your environment variables

Create a `.env` file in the root directory with the following content (replace placeholders with actual values):

```
PREDICTION_KEY=your_azure_prediction_key
ENDPOINT=your_azure_endpoint_url
PROJECT_ID=your_project_id
ITERATION_NAME=Eco_Vision
MONGODB_URI=mongodb+srv://<username>:<password>@eco-vision.mongodb.net/?retryWrites=true&w=majority&appName=eco-vision
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🔍 Example Prediction Flow

**Input**: 🖼️ Image of a plastic bottle  
**Output**:

- **Predicted**: Plastic (94%)
- **Disposal Tip**: Rinse and place in a plastic recycling bin ♻️
- **Feedback Box**: ✅ Correct | ❌ Incorrect
- **Logs**: Stored in MongoDB with timestamp, result, and feedback

---

## 📊 MongoDB Document Structure

### Prediction Log

```json
{
  "filename": "plastic_bottle.jpg",
  "result": [
    { "tagName": "Plastic", "probability": 0.94 }
  ],
  "timestamp": "2025-05-02T10:00:00Z"
}
```

### Feedback Log

```json
{
  "filename": "plastic_bottle.jpg",
  "feedback": "Incorrect",
  "timestamp": "2025-05-02T10:05:00Z"
}
```

---

## 💡 Future Enhancements

- 🔄 Retrain model with user-submitted images marked as incorrect
- 💬 Add a chatbot for FAQs & eco-tips
- 📊 Dynamic admin dashboard using Streamlit and MongoDB
- 🌍 Multilingual support for wider eco-awareness

---

## 🧠 Why Garbage Classification?

- Promotes **recycling** and **reuse** 🌱
- Reduces **landfill impact** 🗑️
- Ensures safe disposal of **hazardous materials** ⚠️
- Supports a **cleaner ecosystem** and **sustainable living** 🌎

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.  
Ideas, issues, and ⭐ stars are appreciated!

---

## 📜 License

MIT License © 2025 Sai Kumar Garlapati
