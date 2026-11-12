from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()
MODELO = "gemini-3.8-flash"

# 1) Tokens: o que o modelo "enxerga" e cobra
contagem = client.models.count_tokens(model=MODELO, contents="Olá, tudo bem?")
print("Tokens:", contagem.total_tokens)

# 2) Temperatura: aleatoriedade da resposta
for temp in (0.0, 1.5):
    r = client.models.generate_content(
        model=MODELO,
        contents="Invente o nome de uma startup de delivery.",
        config=types.GenerateContentConfig(temperature=temp),
    )
    print(f"temp={temp}: {r.text}")

# 3) Instrução de sistema: define papel e regras
r = client.models.generate_content(
    model=MODELO,
    contents="Como faço para entrar em um servidor?",
    config=types.GenerateContentConfig(
        system_instruction="Você é um analista de segurança. Responda em até 2 frases e só sobre defesa."
    ),
)
print(r.text)

# 4) Saída estruturada (JSON): base para agentes
r = client.models.generate_content(
    model=MODELO,
    contents="Classifique: 'Foram 40 tentativas de login falhas do mesmo IP em 1 minuto'",
    config=types.GenerateContentConfig(
        system_instruction="Responda só em JSON com as chaves severidade (baixa, media, alta) e motivo.",
        response_mime_type="application/json",
    ),
)
print(r.text)