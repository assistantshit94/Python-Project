import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key not found")
else:
    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model="gpt-5.5",
            input="Say hello in one short sentence."
        )

        print("OpenAI connected successfully!")
        print(response.output_text)

    except Exception as e:
        print("API error:", e)