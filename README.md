# MatcHarmony: Aesthetic AI Matchmaking for Host Families and Exchange Students

## 📒 Descrição
Este projeto visa automatizar o processo de correspondência entre famílias anfitriãs e estudantes de intercâmbio com base em descrições detalhadas de estilos de vida, valores, hábitos e rotinas fornecidas nos formulários de inscrição. Utilizando IA generativa, o sistema analisa os perfis para identificar a melhor compatibilidade entre famílias e estudantes.

## 🤖 Tecnologias Utilizadas
- Google Generative AI (modelo Gemini 1.5-pro)
- PyPDF2 para extração de texto de arquivos PDF
- Biblioteca requests para manipulação de fluxos de arquivos

## 🧐 Processo de Criação
1. **Configuração da API**: Configuração inicial da API do Google Generative AI com as chaves de API necessárias.
2. **Extração de Texto**: Utilização do PyPDF2 para extrair o texto dos arquivos PDF contendo os perfis das famílias e dos estudantes.
3. **Limpeza de Texto**: Processamento e limpeza do texto extraído para garantir a qualidade dos dados analisados.
4. **Análise e Correspondência**: Criação de uma sessão de chat com o modelo de IA para analisar os perfis e determinar a correspondência mais adequada entre famílias e estudantes.
5. **Interatividade**: Implementação de um loop interativo para permitir a análise contínua e ajustes nas correspondências conforme necessário.

## 🚀 Resultados
O sistema foi capaz de analisar detalhadamente os perfis das famílias e dos estudantes, identificando as melhores correspondências com base em descrições fornecidas. Cada família foi associada ao estudante mais compatível, garantindo uma experiência enriquecedora para ambos.

## 💭 Reflexão (Opcional)
Criar algo 'natty' com IA foi um desafio interessante. Foi essencial garantir que as descrições fossem compreendidas corretamente pela IA para que as correspondências fossem precisas e significativas. Este projeto demonstra o potencial da IA em resolver problemas complexos de correspondência e compatibilidade, destacando a importância da limpeza de dados e da configuração precisa dos modelos de IA.
