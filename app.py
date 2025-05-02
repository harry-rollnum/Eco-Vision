# Save this as app.py
import streamlit as st
import requests
from utils.azure_api import predict_image_url, predict_image_file
from utils.database import save_feedback, save_log, get_logs
from PIL import Image
import io

st.set_page_config(page_title="EcoVision", layout="centered")

st.title("🌍 EcoVision - Smart Garbage Classifier")

menu = st.sidebar.radio("Navigate", ["🏠 Home", "📷 Upload/Camera"])

if menu == "🏠 Home":
    st.header("Why Garbage Classification?")
    st.markdown("""
    Garbage classification is vital for:
    - ♻️ Efficient recycling
    - 🌱 Reducing environmental impact
    - 🧠 Training smarter AI to manage waste
    """)
    st.info("This app uses a trained AI model on Azure to classify garbage into different types and provides smart tips on how to dispose of them correctly.")

elif menu == "📷 Upload/Camera":
    st.subheader("Detect Garbage from Image")

    input_type = st.radio("Choose input type:", ["Upload Image", "Image URL", "Camera Capture"])
    image = None
    image_info = {}

    if input_type == "Upload Image":
        uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            image = uploaded_file.read()
            image_info["type"] = "upload"
            image_info["name"] = uploaded_file.name

    elif input_type == "Image URL":
        image_url = st.text_input("Paste image URL:")
        if image_url and st.button("Predict"):
            with st.spinner("Analyzing..."):
                result = predict_image_url(image_url)
            image_info["type"] = "url"
            image_info["url"] = image_url
            predictions = result.get("predictions", [])
            save_log(image_info, predictions)
            if predictions:
                best = predictions[0]
                st.success(f"Predicted: **{best['tagName']}** ({best['probability']*100:.2f}%)")
                st.markdown("**💡 Tip:** " + {
                    "plastic": "Rinse before recycling and avoid mixed materials.",
                    "metal": "Crush cans to save space and recycle.",
                    "organic": "Great for composting! Avoid mixing with plastics.",
                    "paper": "Keep dry and clean. No oil stains!",
                    "glass": "Handle with care. Reuse when possible.",
                    "e-waste": "Drop at certified centers, never in regular bins."
                }.get(best['tagName'].lower(), "Dispose responsibly!"))
                feedback = st.radio("Is this correct?", ["Yes", "No"])
                if feedback == "No":
                    correct_label = st.text_input("What should be the correct label?")
                    if st.button("Submit Feedback"):
                        save_feedback(image_info, feedback, correct_label)
                        st.success("Thanks for your feedback!")
                elif feedback == "Yes":
                    if st.button("Submit Feedback"):
                        save_feedback(image_info, feedback)
                        st.success("Thanks for your feedback!")

    elif input_type == "Camera Capture":
        captured = st.camera_input("Take a picture")
        if captured:
            image = captured.getvalue()
            image_info["type"] = "camera"
            image_info["name"] = "camera_capture.jpg"

    if image and input_type != "Image URL":
        if st.button("Predict"):
            with st.spinner("Sending to AI model..."):
                result = predict_image_file(image)
            predictions = result.get("predictions", [])
            save_log(image_info, predictions)
            if predictions:
                best = predictions[0]
                st.success(f"Predicted: **{best['tagName']}** ({best['probability']*100:.2f}%)")
                st.markdown("**💡 Tip:** " + {
                    "plastic": "Rinse before recycling and avoid mixed materials.",
                    "metal": "Crush cans to save space and recycle.",
                    "organic": "Great for composting! Avoid mixing with plastics.",
                    "paper": "Keep dry and clean. No oil stains!",
                    "glass": "Handle with care. Reuse when possible.",
                    "e-waste": "Drop at certified centers, never in regular bins."
                }.get(best['tagName'].lower(), "Dispose responsibly!"))
                feedback = st.radio("Is this correct?", ["Yes", "No"])
                if feedback == "No":
                    correct_label = st.text_input("What should be the correct label?")
                    if st.button("Submit Feedback"):
                        save_feedback(image_info, feedback, correct_label)
                        st.success("Thanks for your feedback!")
                elif feedback == "Yes":
                    if st.button("Submit Feedback"):
                        save_feedback(image_info, feedback)
                        st.success("Thanks for your feedback!")