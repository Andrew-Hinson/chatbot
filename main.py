import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = ""
    if "GEMENI_API_KEY" in os.environ:
        api_key = os.environ.get("GEMENI_API_KEY")
        print("gemeni key retrieved")
    else:
        raise Exception("Gemeni API Key not found")

    client = genai.Client(api_key=api_key)
    content = client.models.generate_content(model="gemini-2.5-flash", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    print(content.text)


if __name__ == "__main__":
    main()
