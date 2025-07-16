requests: This is a popular Python library for making HTTP requests (like GET, POST) to web servers.
json: This library helps you work with JSON data, which is a common format for sending and receiving data on the web.

Common HTTP Status Codes (for reference):
200: Success! Everything worked
400: Bad Request (something wrong with your request)
401: Unauthorized (API key issue)
404: Not Found (wrong URL)
500: Server Error (problem on their end)

requests.get(), requests.post(), requests.put(), requests.delete()
response.json(), response.text, response.status_code
response.raise_for_status(), response.ok

json.dumps() - Python → JSON string
json.loads() - JSON string → Python
json.dump() - Python → JSON file
json.load() - JSON file → Python

response:  <Response [200]>
response.ok:  True
response.raise_for_status:  <bound method Response.raise_for_status of <Response [200]>>
response.text:  







{"id":"gen-1752314742-4dEgBjBERTRXlSwzYkUa","provider":"Venice","model":"meta-llama/llama-3.2-3b-instruct:free","object":"chat.completion","created":1752314742,"choices":[{"logprobs":null,"finish_reason":"stop","native_finish_reason":"stop","index":0,"message":{"role":"assistant","content":"Salty chest rapes\nBrotherly love's subtle sting\nBrotherly device","refusal":null,"reasoning":null}}],"usage":{"prompt_tokens":346,"completion_tokens":18,"total_tokens":364}}
response.json():  {'id': 'gen-1752314742-4dEgBjBERTRXlSwzYkUa', 'provider': 'Venice', 'model': 'meta-llama/llama-3.2-3b-instruct:free', 'object': 'chat.completion', 'created': 1752314742, 'choices': [{'logprobs': None, 'finish_reason': 'stop', 'native_finish_reason': 'stop', 'index': 0, 'message': {'role': 'assistant', 'content': "Salty chest rapes\nBrotherly love's subtle sting\nBrotherly device", 'refusal': None, 'reasoning': None}}], 'usage': {'prompt_tokens': 346, 'completion_tokens': 18, 'total_tokens': 364}}



## **🎯 Parameter Effects Explained:**

### **Temperature (0.0 - 2.0):**
- **0.0**: Robot-like, predictable responses
- **0.7**: Balanced creativity (DEFAULT)
- **1.5**: Very creative, sometimes weird
- **2.0**: Maximum chaos! 🤪

### **Top_p (0.1 - 1.0):**
- **0.1**: Only considers most likely words
- **0.9**: Considers 90% of probable words
- **1.0**: All words are possible

### **Max_tokens:**
- Controls response length
- **50**: Short answers
- **500**: Medium essays
- **2000**: Long detailed responses

---

## **💡 Pro Tips:**

### **For Different Use Cases:**
- **Chatbot**: `temperature=0.7, max_tokens=150`
- **Code Generation**: `temperature=0.2, max_tokens=500`
- **Creative Writing**: `temperature=1.0, max_tokens=300`
- **Data Analysis**: `temperature=0.1, max_tokens=100`

### **Memory Management:**
- Keep `messages` array reasonable size
- Long conversations = more tokens = higher cost
- Consider truncating old messages

