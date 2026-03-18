import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = ""
    if "GEMENI_API_KEY" in os.environ:
        api_key = os.environ.get("GEMENI_API_KEY")
        print("gemeni key retrieved")
    else:
        raise Exception("Gemeni API Key not found")

    print("Hello from chatbot!")


if __name__ == "__main__":
    main()
