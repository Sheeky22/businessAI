import requests
import json
# import os
# from dotenv import load_dotenv

# load_dotenv()

def marketcopy_generator(product_name,usp,target,brand,api_key):

    # api_key=os.getenv("OPENROUTER_API_KEY")

    # if not api_key:
    #     return ("Error: API key not available!!!")
    #     exit()
    

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}"
        },
        data=json.dumps({
            "model":"deepseek/deepseek-r1:free",
            "messages":[{
                "role":"system",
                "content":'''You are a professional marketing copy writer. Write a marketing an effective marketing copy that clearly 
                communicates the value and the benefit of the product to it's target audience. Let the copy be short and crisp. 
                Remove all meta-comments or internal notes about the copy. '''
            },
            {
                "role":"user",
                "content":f"Product is {product_name}, target audience = {target}, usp is {usp}, brand name is {brand}"
        }]

        })
    )

    if response.ok:
        return (f"{response.json()['choices'][0]['message']['content']}")
    else:
        return(f"Error: {response.status_code}")


