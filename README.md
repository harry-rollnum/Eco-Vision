♻️ Eco Vision – Smart Waste Classifier with Azure & Streamlit
Eco Vision is a smart, AI-powered garbage classification system that helps users identify types of waste in real-time using images or camera input. Built with Azure Custom Vision, MongoDB, and Streamlit, this app not only predicts waste categories but also provides eco-friendly disposal tips, gathers user feedback, and maintains logs for continuous learning.

🚀 Features
✅ Classify garbage into 6 categories: Plastic, Paper, Glass, Metal, Cardboard, and Trash
📸 Supports image upload, camera capture, and image URLs
🔍 Uses Azure Custom Vision API for accurate predictions
💬 Shows interactive disposal tips based on the prediction
🗳️ Collects user feedback ("Correct"/"Incorrect") for model improvement
📊 Logs predictions, feedback, and usage data to MongoDB
📚 Has a Home Page explaining the importance of waste classification
🧠 Designed to be expandable — chatbot, dynamic tips, and more coming soon!

📦 Folder Structure
bash
Copy
Edit
eco-vision/
├── app.py                # Main Streamlit app
├── azure_api.py          # Handles prediction requests to Azure Custom Vision
├── database.py           # MongoDB logging and feedback utilities
├── utils.py              # Static disposal tips & helper functions
├── requirements.txt      # Required Python packages
└── README.md             # This file
🧠 How It Works
User Uploads Image / Captures from Camera / Pastes Image URL

Image is sent to Azure Custom Vision API

The model returns predictions (e.g., "Plastic: 94%")

The app shows:

Prediction result

Friendly disposal tips

A feedback form

All activity is logged into a MongoDB Atlas cluster

⚙️ Setup Instructions
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/yourusername/eco-vision.git
cd eco-vision
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set your secrets
Create a .env file or set these environment variables:

env
Copy
Edit
PREDICTION_KEY=1zbHNYawKdX2G8rnAMaKHBmoI7btqVQ7jv86RZfBMQwHAVuPBFNkJQQJ99BDACGhslBXJ3w3AAAIACOGwGPW
ENDPOINT=https://ecovisioncvprojectinstance-prediction.cognitiveservices.azure.com
PROJECT_ID=3ea00f4e-5165-4fb6-aae8-34c5e961e458
ITERATION_NAME=Eco_Vision
MONGODB_URI=mongodb+srv://<username>:<password>@eco-vision.mongodb.net/?retryWrites=true&w=majority&appName=eco-vision
4. Run the app
bash
Copy
Edit
streamlit run app.py
🔍 Example Prediction Flow
Input: 🖼️ An image of a plastic bottle

Output:

Predicted: Plastic (94%)

Disposal Tip: Rinse and place in a plastic recycling bin ♻️

Feedback Box: ✅ Correct | ❌ Incorrect

Logs: Stored in MongoDB with timestamp, result, and feedback

📊 MongoDB Structure
Prediction Log Document:
json
Copy
Edit
{
  "filename": "plastic_bottle.jpg",
  "result": [
    { "tagName": "Plastic", "probability": 0.94 }
  ],
  "timestamp": "2025-05-02T10:00:00Z"
}
Feedback Document:
json
Copy
Edit
{
  "filename": "plastic_bottle.jpg",
  "feedback": "Incorrect",
  "timestamp": "2025-05-02T10:05:00Z"
}
💡 Future Enhancements
🔄 Use user-submitted images (with incorrect predictions) for retraining

💬 Add a domain-limited chatbot for FAQs & eco-tips

📊 Dynamic dashboard for admin insights using Streamlit/Mongo

🌍 Multilingual support for eco-awareness expansion

🧠 Why Garbage Classification?
Proper waste classification:

Promotes recycling and reuse 🌱

Reduces landfill impact 🗑️

Ensures safe disposal of hazardous materials ⚠️

Supports cleaner ecosystems and sustainable living 🌎

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.
Ideas, issues, and stars ⭐ are appreciated!

📜 License
MIT License © 2025 Sai Kumar Garlapati

