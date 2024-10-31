import requests
import json
import time  # Import the time module for adding delays

# Your OpenAI API key
api_key = "sk-proj-3tbeeYESQeh8HwmZChf8T3BlbkFJbxrtEqjnQukuJqmc9Yg4"

# Define the API endpoint
url = "https://api.openai.com/v1/chat/completions"

# Headers for the request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# The request payload
data = {
    "model": "gpt-4o",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "You’re an advanced vision person specializing in automotive object recognition. You have deep knowledge of various car models, their specifications, and the ability to analyze images effectively. Your main goal is to accurately identify cars from images and provide detailed measurements. Please identify the car in the image and return the following specifications in a JSON format: car model name, length, width, and height. The measurements should be as accurate as possible and based on the recognized car model's standard specifications."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://raw.githubusercontent.com/MatthewJeffson/image_store/refs/heads/main/3.png"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}

# Send the request
response = requests.post(url, headers=headers, json=data)

# Parse the response
response_data = response.json()

# Step 1: Print the full response data
print("Full Response Data:")
print(json.dumps(response_data, indent=4))  # Pretty print the full response data
time.sleep(1)  # Wait for 1 second

# Step 2: Extract and print the assistant's message content
if response_data.get('choices'):
    assistant_message = response_data['choices'][0]['message']['content']
    
    print("\nAssistant Message Content:")
    print(assistant_message)
    time.sleep(1)  # Wait for 1 second
    
    # Step 3: Try to extract and print the JSON data from the message content
    try:
        json_data = assistant_message.split('```json\n')[1].split('\n```')[0]
        print("\nExtracted JSON Data:")
        print(json_data)  # Directly output the JSON data
    except IndexError:
        print("\nNo JSON data found in the response.")
else:
    print("\nNo choices were found in the response.")