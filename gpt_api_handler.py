import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")


"""
Allows for conversation with the gpt api.

Args:
    system: Context for the gpt
    user: User's promt

Returns:
    String: gpt's answer
"""
def chat_with_gpt(context, prompt):
    # print("chatting with gpt")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
             messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt},
             ]
            # ],
            # temperature=0.7,  # Adjust creativity level
            # max_tokens=150,  # Adjust response length
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"An error occurred: {e}"