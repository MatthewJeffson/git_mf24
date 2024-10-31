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
                    "text": "You are a highly skilled image processing expert with extensive experience in analyzing parking lot layouts. Your expertise lies in interpreting images that depict cars and parking areas, particularly those with specified markings like green lines for parking boundaries and rectangles for vehicles.\n\nYour task is to analyze the provided image and generate a JSON format output. This output should indicate which parking areas are available based on the intersection of the green lines and the rectangles representing cars. You need to ensure that your analysis is precise and only includes the necessary information related to parking availability.\n\nPlease keep in mind that the parking areas corresponding to the green lines are identified by unique identifiers, and they can be represented in a simple JSON structure. It’s crucial to output whether each area is available or occupied based on the intersection check.\n\nHere’s an example structure for the JSON output you should provide:\n```json\n{\n\"availableparkingspots\": [\n{\n\"spotid\": \"_\",\n\"is_available\": true/false\n},\n{\n\"spotid\": \"_\",\n\"is_available\": true/false\n}\n]\n}\n```\nMake sure to replace the placeholders appropriately based on your analysis of the image."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://raw.githubusercontent.com/MatthewJeffson/image_store/refs/heads/main/1.png"
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