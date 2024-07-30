import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to translate content using ChatGPT
def translate_content(content, target_language="Spanish"):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Translate the following content to {target_language}: {content}"}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000
    )
    
    translated_content = response.choices[0].message['content'].strip()
    return translated_content

# List of files to translate
files_to_translate = [
    "README.md",
    "SUMMARY.md",
    "code_of_conduct.md",
    "contributing.md",
    "first-time-onboarding.md",
    "license.md",
    "lightning-bounties-team.md",
    "socials.md"
    # Add more files as needed
]

for file_name in files_to_translate:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    
    translated_content = translate_content(content, "Spanish")
    
    translated_file_name = f"translated_{file_name}"
    with open(translated_file_name, "w", encoding="utf-8") as translated_file:
        translated_file.write(translated_content)
