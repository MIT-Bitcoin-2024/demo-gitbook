import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to translate content
def translate_content(content, target_language="Spanish"):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate the following content to {target_language}: {content}",
        max_tokens=1000
    )
    translated_content = response.choices[0].text.strip()
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
