import os
from openai import AzureOpenAI

# Initialize the Azure OpenAI Client
client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key = os.getenv("AZURE_OPENAI_KEY"),  
    api_version = "2024-02-15-preview"
)

def get_efik_stem_response(user_query):
    # Load the system prompt from the local file
    with open('src/system_prompt.txt', 'r', encoding='utf-8') as f:
        system_instructions = f.read()

    response = client.chat.completions.create(
        model="gpt-4o", # Targeted model for Imagine Cup 2026
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content

# Example Usage
# print(get_efik_stem_response("Explain Gravity in Efik"))
