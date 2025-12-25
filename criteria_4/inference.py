import requests
import json

# Define the URL of the /predict endpoint
PREDICT_URL = "http://127.0.0.1:8000/predict"

# Define the input data for inference
input_data = {
    "input": [25, 0, 28.5, 0, 0, 0, 1, 0]  # Example input features
}

def make_inference():
    try:
        # Send a POST request to the /predict endpoint
        response = requests.post(
            PREDICT_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(input_data)
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Inference successful!")
            print("Response:", response.json())
        else:
            print(f"Inference failed with status code {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print("An error occurred during inference:", str(e))

if __name__ == "__main__":
    # Run the inference
    make_inference()