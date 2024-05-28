# MatcHarmony: Aesthetic AI Matchmaking for Host Families and Exchange Students

![Welcome](https://github.com/robinsonronchi/match-family-student/blob/main/utils/welcome.webp)

## 📒 Descrição
Este projeto visa automatizar o processo de correspondência entre famílias anfitriãs e estudantes de intercâmbio com base em descrições detalhadas de estilos de vida, valores, hábitos e rotinas fornecidas nos formulários de inscrição. Utilizando IA generativa, o sistema analisa os perfis para identificar a melhor compatibilidade entre famílias e estudantes.

## 🤖 Tecnologias Utilizadas
- Google Generative AI (modelo Gemini 1.5-pro)
- PyPDF2 para extração de texto de arquivos PDF
- Biblioteca requests para manipulação de fluxos de arquivos

## 🧐 Processo de Criação
1. **Configuração da API**: Configuração inicial da API do Google Generative AI com as chaves de API necessárias.

```python
import os
import google.generativeai as genai
import PyPDF2

# Configuração da API do Google Generative AI
GOOGLE_API_KEY="Insiera sua API KEY AQUI"
genai.configure(api_key=GOOGLE_API_KEY)

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
```

2. **Extração de Texto**: Utilização do PyPDF2 para extrair o texto dos arquivos PDF contendo os perfis das famílias e dos estudantes.

```python
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
```

![MatHarmony Engine](https://github.com/robinsonronchi/match-family-student/blob/main/utils/matcharmony.webp)

3. **Análise e Correspondência**: Criação de uma sessão de chat com o modelo de IA para analisar os perfis e determinar a correspondência mais adequada entre famílias e estudantes.

```python
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
```

4. **Interatividade**: Implementação de um loop interativo para permitir a análise contínua e ajustes nas correspondências conforme necessário.

```python
prompt = input('Esperando prompt: ')

while prompt != "fim":
  response = chat_session.send_message(prompt)
  print("Resposta:", response.text, '\n\n')
  prompt = input('Esperando prompt: ')
```

## 🚀 Resultados
O sistema foi capaz de analisar detalhadamente os perfis das famílias e dos estudantes, identificando as melhores correspondências com base em descrições fornecidas. Cada família foi associada ao estudante mais compatível, garantindo uma experiência enriquecedora para ambos.

````bash
## Análise dos Perfis e Proposta de Acolhimento:

Vamos analisar cada família e cada estudante para determinar a melhor combinação para um intercâmbio enriquecedor e respeitoso para todos:

**Família 1:**

* **Residência:** Casa espaçosa no subúrbio. Positivo para estudantes que apreciam espaço e tranquilidade.
* **Animais:** Dois cachorros e um gato. Pode ser um problema para estudantes com alergias.
* **Alimentação:** Vegetariana. Ponto importante a ser considerado na escolha do estudante.
* **Religião:** Cristãos praticantes.  Cabe analisar se o estudante se sentiria confortável.
* **Hobbies:** Caminhadas, jardinagem, leitura.  Um estudante que aprecie atividades calmas se adaptaria bem.
* **Fumantes:** Não fumantes.
* **Orientação Sexual:** Heterossexuais.  Importante observar se o ambiente familiar é verdadeiramente inclusivo.
* **Atividades de Fim de Semana:**  Passeios no parque, churrascos em família, visitas a museus.  Um perfil tradicional.
* **Valores:** Tradicionais.
* **Rotina:** Tranquila, com horários definidos. Positivo para estudantes que preferem organização.
* **Outros:** Valorizam a educação e a leitura, participam de atividades comunitárias.

**Família 2:**

* **Residência:** Apartamento moderno no centro da cidade.  Pode agradar estudantes que preferem um estilo de vida mais urbano.
* **Animais:** Não tem.
* **Alimentação:** Onívora com preferência por alimentação saudável. Dieta flexível e abrangente.
* **Religião:** Agnósticos.
* **Hobbies:** Cinema, teatro, viagens. Um perfil cultural que pode combinar com estudantes de interesses similares.
* **Fumantes:** Não fumantes.
* **Orientação Sexual:** Diversa (casal LGBTQ+).   Um ambiente naturalmente inclusivo e diverso.
* **Atividades de Fim de Semana:** Saídas culturais, jantares em restaurantes, encontros com amigos. Um perfil socialmente ativo.
* **Valores:** Progressistas.
* **Rotina:** Agitada, com muitas atividades sociais e culturais.  Ideal para estudantes que apreciam movimento.
* **Outros:** Defensores dos direitos humanos e da diversidade, envolvidos em ONGs.

**Família 3:**

* **Residência:** Fazenda em uma área rural. Um ambiente completamente diferente, ideal para quem busca contato com a natureza.
* **Animais:** Vários animais de fazenda. Pode ser um atrativo ou um impedimento, dependendo do estudante.
* **Alimentação:** Onívora com muitos alimentos orgânicos e caseiros.
* **Religião:** Espiritualistas.
* **Hobbies:** Equitação, pesca, pintura.  Estudantes com hobbies similares se identificariam.
* **Fumantes:** Não fumantes.
* **Orientação Sexual:** Heterossexuais.  Assim como na Família 1, a abertura a diferentes realidades é crucial.
* **Atividades de Fim de Semana:** Trabalhos na fazenda, piqueniques, atividades ao ar livre.  Um estilo de vida mais tranquilo.
* **Valores:** Conservadores.
* **Rotina:** Flexível, com atividades variando.
* **Outros:** Vida sustentável, ensino em casa (homeschooling).

**Estudante 1:**

* **Habitação preferida:** Sem preferência.
* **Animais:** Aprecia animais, especialmente cachorros.
* **Alimentação:** Vegetariano.
* **Religião:** Ateu.
* **Hobbies:** Fotografia, escalada, leitura de ficção científica.
* **Fumante:** Não.
* **Orientação Sexual:** Heterossexual.
* **Atividades de Fim de Semana:** Passeios na natureza, clubes de leitura, workshops de fotografia.
* **Valores:** Progressistas.
* **Rotina:** Agitada com atividades extracurriculares.
* **Outros:** Valoriza a sustentabilidade e o meio ambiente, participa de movimentos estudantis.

**Estudante 2:**

* **Habitação preferida:** Apartamento.
* **Animais:** Alérgico a pelo de animais.
* **Alimentação:** Vegetariano.
* **Religião:** Católico.
* **Hobbies:** Dança e teatro.
* **Fumante:** Não.
* **Orientação Sexual:** Homossexual.
* **Atividades de Fim de Semana:** Eventos ao ar livre.
* **Valores:** Progressistas.
* **Rotina:** Agitada com atividades extracurriculares.
* **Outros:** Valoriza a sustentabilidade e o meio ambiente, participa de movimentos estudantis.
````

``` Bash
## Proposta de Acolhimento:

**Estudante 1  -> Família 3:** O Estudante 1, apesar de apreciar cachorros, encontraria na Família 3  uma experiência única em um ambiente rural,  com atividades ao ar livre que ele aprecia e alinhadas com seus 
valores de sustentabilidade. A Família 3, por sua vez,  poderia se beneficiar do contato com um estudante vegetariano e engajado em causas ambientais,  expandindo seus horizontes. O ponto de atenção seria garantir que o estudante se sinta confortável com os valores religiosos da família.

**Estudante 2 -> Família 2:** A Família 2 seria a mais adequada para o Estudante 2, pois ambos compartilham valores progressistas e um estilo de vida agitado com atividades culturais.  A localização em um apartamento moderno no 
centro da cidade e a ausência de animais de estimação são ideais para o estudante.   A abertura da família à diversidade, sendo um casal LGBTQ+,  criaria um ambiente acolhedor e respeitoso.

**Importante:** É fundamental que  haja um diálogo aberto e honesto entre as famílias e os estudantes antes da decisão final,  abordando  as expectativas,  os limites e as diferenças para garantir uma experiência positiva para todos.
```

``` Bash
Esperando prompt: Qual o total de estudantes e famílias analisadas?
Resposta: Temos **2 estudantes** e **3 famílias** sendo analisados para o intercâmbio! 😊 

Com essa informação, já podemos concluir que, infelizmente, uma família não irá receber nenhum dos estudantes. Por isso, a análise de compatibilidade entre os perfis será ainda mais importante para que possamos fazer o melhor "match" possível! 😉

Em que mais posso te ajudar? 😊

Esperando prompt: Quantas famílias possuem pets?
Resposta: Das 3 famílias analisadas, **2 possuem pets**:

* **Família 1:** Possui dois cachorros e um gato.
* **Família 3:** Vive em uma fazenda e tem vários animais, como cavalos, vacas e galinhas.

Somente a **Família 2** não possui animais de estimação. 🐶🐱🐔🐴

Essa informação é importante para levarmos em consideração as preferências e possíveis alergias dos estudantes na hora de decidir a família mais adequada para cada um! 😉

Continue me passando as informações que você achar relevantes! 😄 Quanto mais dados tivermos, melhor será a análise!
```

## 💭 Reflexão (Opcional)
Criar algo 'natty' com IA foi um desafio interessante. Foi essencial garantir que as descrições fossem compreendidas corretamente pela IA para que as correspondências fossem precisas e significativas. Este projeto demonstra o potencial da IA em resolver problemas complexos de correspondência e compatibilidade, destacando a importância da limpeza de dados e da configuração precisa dos modelos de IA.
