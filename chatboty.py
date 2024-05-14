import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Set up OpenAI API key
openai.api_key = os.environ["API_KEY"]

def ask_gpt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.5,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response['choices'][0]['message']['content'].strip()

def generate_image_url(prompt: str) -> str:
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def main():
    print("Welcome to the Developer's Bot-The Dev's Assistant(chat and image generation ). Type 'quit' to exit.")
    user_input = ""

    while user_input.lower() != "quit":
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        # Check if the user wants to generate an image
        if user_input.lower() == "generate image":
            image_prompt = input("Enter a prompt for image generation: ")
            image_url = generate_image_url(image_prompt)
            print(f"Generated Image URL: {image_url}")
        else:
            # Generate chat response
            response = ask_gpt(user_input)
            print("Developer's Bot:", response , "\n")

if __name__ == "__main__":
    main()
