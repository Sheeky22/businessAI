import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("API key not available!!!")
    exit()

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {api_key}",
  },
  data = json.dumps({
    "model": "cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
    "messages": [{
        "role": "system",
        "content": "You are a helpful programming tutor who explains concepts clearly."
    },
    {
        "role": "user", 
        "content": "Explain Python functions"
    },
    {
        "role": "assistant",
        "content": "A function is a reusable block of code..."
    },
    {
        "role": "user",
        "content": "Can you give me an example?"
    }],
    
    # CREATIVITY CONTROL
    "temperature": 0.7,        # 0.0 = very focused, 2.0 = very creative
    "top_p": 0.9,             # Nucleus sampling (0.1 = focused, 1.0 = diverse)
    "top_k": 50,              # Top-k sampling (limits vocabulary)
    
    # RESPONSE LENGTH
    "max_tokens": 150,        # Maximum tokens in response
    "min_tokens": 10,         # Minimum tokens in response
    
    # STOPPING CONDITIONS
    "stop": ["Human:", "\n"], # Stop generation at these strings
    
    # PENALTIES
    "frequency_penalty": 0.0,  # Penalize frequent words (-2.0 to 2.0)
    "presence_penalty": 0.0,   # Penalize repeated topics (-2.0 to 2.0)
    "repetition_penalty": 1.0, # Penalize repetition (1.0 = no penalty)
    
    # SAMPLING
    "seed": 42,               # For reproducible results
    "stream": False,          # True = streaming response, False = complete response
    
    # RESPONSE FORMAT
    "response_format": {
        "type": "json_object"  # Force JSON response
    }
})
)

if response.ok:
    print("id: ",response.json()['id'])
    print("Model & Provider: ",response.json()['model'],"by",response.json()['provider'])
    print(f"AI message: {response.json()['choices'][0]['message']['content']}")
    print(f"Prompt Tokens: {response.json()['usage']['prompt_tokens']}")
    print(f"Completion Tokens: {response.json()['usage']['completion_tokens']}")
    print(f"Total Tokens: {response.json()['usage']['total_tokens']}")
else:
    print(response.status_code)

# print("response: ",response)
# print("response.ok: ",response.ok)
# print("response.raise_for_status: ",response.raise_for_status)
# print("response.text: ",response.text)
# print("response.json(): ",response.json())


