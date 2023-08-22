import openai

def get_openai_suggestion(prompt: str) -> str:
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    response = openai.Completion.create(prompt=prompt, max_tokens=50)
    return response.choices[0].text.strip()
