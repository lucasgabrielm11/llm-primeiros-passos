from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()  # lê GEMINI_API_KEY do ambiente

resposta = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explique o que é uma API em 3 frases simples.",
)

print(resposta.text)