# LLM: Primeiros Passos

Projeto de estudo com os fundamentos de LLMs usando Python e a API do Gemini (Google AI Studio).

## O que o projeto mostra

- Primeira chamada a um LLM via API com o SDK `google-genai`
- Contagem de tokens
- Efeito da temperatura nas respostas
- Instrução de sistema para definir papel e regras
- Saída estruturada em JSON

## Estrutura

```
llm-primeiros-passos/
├── 01_primeira_chamada.py
├── 02_fundamentos.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como rodar

Requisitos: Python 3.9+ e uma chave de API gratuita do [Google AI Studio](https://aistudio.google.com).

```bash
git clone https://github.com/lucasgabrielm11/llm-primeiros-passos.git
cd llm-primeiros-passos

python -m venv .venv
source .venv/Scripts/activate      # Git Bash
# .venv\Scripts\Activate.ps1       # PowerShell

pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz com a sua chave:

```
GEMINI_API_KEY=sua-chave-aqui
```

Execute:

```bash
python 01_primeira_chamada.py
python 02_fundamentos.py
```

O `.env` está no `.gitignore` e não deve ser enviado ao GitHub.

## Aprendizados

- Nomes de modelos mudam com frequência. O `gemini-2.5-flash` deixou de estar disponível para contas novas e precisei trocar o nome do modelo.
- A API pode retornar erros temporários (como o 503, por alta demanda), então em projetos reais é preciso tratar falhas.
- Chaves de API ficam fora do repositório, e o `.gitignore` deve existir antes do `.env`.

## Próximos passos

- [x] Assistente RAG sobre documentos
- [x] Agente de triagem de logs

---