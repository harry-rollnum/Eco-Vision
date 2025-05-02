import requests

PREDICTION_KEY = "1zbHNYawKdX2G8rnAMaKHBmoI7btqVQ7jv86RZfBMQwHAVuPBFNkJQQJ99BDACGhslBXJ3w3AAAIACOGwGPW"
HEADERS_URL = {
    "Prediction-Key": PREDICTION_KEY,
    "Content-Type": "application/json"
}
HEADERS_FILE = {
    "Prediction-Key": PREDICTION_KEY,
    "Content-Type": "application/octet-stream"
}

URL_ENDPOINT = "https://ecovisioncvprojectinstance-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/3ea00f4e-5165-4fb6-aae8-34c5e961e458/classify/iterations/Eco_Vision/url"
FILE_ENDPOINT = "https://ecovisioncvprojectinstance-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/3ea00f4e-5165-4fb6-aae8-34c5e961e458/classify/iterations/Eco_Vision/image"

def predict_image_url(image_url):
    response = requests.post(URL_ENDPOINT, headers=HEADERS_URL, json={"Url": image_url})
    return response.json()

def predict_image_file(image_bytes):
    response = requests.post(FILE_ENDPOINT, headers=HEADERS_FILE, data=image_bytes)
    return response.json()
