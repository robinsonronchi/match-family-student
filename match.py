# NOTE: Your prompt contains media inputs that are not directly supported by the
# Gemini Files API. Preprocessing will be required for these inputs. Specific
# information is provided below.

"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai
import PyPDF2

# Configuração da API do Google Generative AI
GOOGLE_API_KEY="Insira sua API KEY aqui"
genai.configure(api_key=GOOGLE_API_KEY)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

# Função para extrair texto das páginas do PDF
def extract_text_from_pdf(file_stream) -> list[str]:
    parts = []
    pdf_reader = PyPDF2.PdfReader(file_stream)
    pages = [pdf_reader.pages[i].extract_text() for i in range(len(pdf_reader.pages))]
    for index, page in enumerate(pages):
        parts.append(page)
    return parts

def load_profiles():
    # Verifica se os diretórios existem
    if not os.path.exists(FAMILIES_DIR):
        raise FileNotFoundError(f"O diretório {FAMILIES_DIR} não existe.")
    if not os.path.exists(STUDENTS_DIR):
        raise FileNotFoundError(f"O diretório {STUDENTS_DIR} não existe.")
    
    # Carrega os perfis de famílias
    for filename in os.listdir(FAMILIES_DIR):
        if filename.endswith(".pdf"):
            filepath = os.path.join(FAMILIES_DIR, filename)
            text = extract_text_from_pdf(filepath)
            families.append(text)

    # Carrega os perfis de estudantes
    for filename in os.listdir(STUDENTS_DIR):
        if filename.endswith(".pdf"):
            filepath = os.path.join(STUDENTS_DIR, filename)
            text = extract_text_from_pdf(filepath)
            students.append(text)

# Constantes
FAMILIES_DIR = r"C:\Users\tatia\Code\match-family-student\profiles\families"
STUDENTS_DIR = r"C:\Users\tatia\Code\match-family-student\profiles\students"

families = []
students = []

# Chama a função para carregar os perfis
load_profiles()

history = []

for family in families:
    history.append({"role": "user", "parts": f'"{family}"'})

for student in students:
    history.append({"role": "user", "parts": f'"{student}"'})

chat_session = model.start_chat(history=history)

response = chat_session.send_message("Faça a análise aprofundada dos perfis das famílias e dos estudantes.\
    Baseado nas descrições dos perfis, identifique qual família é a mais adequada para receber cada estudante.\
    Indique qual família é a mais compatível com cada estudante e explique em detalhes o porquê.\
    Uma família pode receber apenas um estudante.")
print(response.text)

prompt = input('Esperando prompt: ')

while prompt != "fim":
  response = chat_session.send_message(prompt)
  print("Resposta:", response.text, '\n\n')
  prompt = input('Esperando prompt: ')
