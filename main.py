import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = ""
    if "GEMENI_API_KEY" in os.environ:
        api_key = os.environ.get("GEMENI_API_KEY")
        print("gemeni key retrieved")
    else:
        raise Exception("Gemeni API Key not found")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(model="gemini-2.5-flash", contents= messages)

    if response.usage_metadata is not None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        raise Exception("Cannot read usage metadata")
    print(response.text)


if __name__ == "__main__":
    main()
