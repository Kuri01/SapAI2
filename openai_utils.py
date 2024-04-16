from openai import OpenAI

client = OpenAI()

def extract_information(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Extract key entities and relationships from the following text: " + text
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content
    

def generate_test_cases(description):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Generate test cases based on the following process description: " + description
            }
        ],
        max_tokens=800
    )
    return response.choices[0].message.content


def extract_process_names(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Identify all process names mentioned in the following text: " + text
            }
        ],
        max_tokens=100
    )
    return response.choices[0].message.content.split(', ')
