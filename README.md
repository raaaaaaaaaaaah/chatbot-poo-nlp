# Chatbot em python (POO + NLP)

Este projeto demonstra como criar um chatbot em pyhton usando programação orienta a objetos (POO) e processamento de linguagem natural (NLP).

#São duas versões principais:

V1_basico : Chatbot simples com duas estratégias: Regras fixas e Machine Learning (Naive Bayes)

V2_memoria: Evolução do chatbot, adicionado memória de contexto e respostas diferentes (para o caso da mesma pergunta ser repetida)

# Estrutura do Projeto

├── v1_basico/
│ └── chatbot_v1.py # Versão inicial do chatbot (Regras + ML)
├── v2_memoria/
│ └── chatbot_v2.py # Versão evoluída com Memória de Contexto
└── README.md # Documentação do projeto

#Como rodar:

#1: Clonar o repositório

cd v1_basico
python chatbot_v1.py

# Nessa primeira versão o chat implementa duas estrategias de resposta, uma baseada em regras e uma em ML, exemplo:

**Baseado em Regras (Rule-based)**  
   O bot responde de acordo com palavras-chave (ex: "oi", "tchau", "ajuda").

**Baseado em Machine Learning (Naive Bayes)**  
   O bot é treinado com exemplos de frases e responde com base no aprendizado.

# Exemplo de saída 
# Chatbot baseado em Regras 
Oi! Como você está?
Claro! Eu posso te ajudar com dúvidas simples.
Desculpe, não entendi. Pode reformular?

# Chatbot baseado em Machine Learning 
Oi! Como vai?
Estou aqui para te ajudar!
Até logo!

# O chatbot_v2.py é uma evolução da versão anterior, agora com memória de contexto:

**O bot lembra as últimas interações.**
**Se não entende algo, pode se apoiar no histórico.**
**Se você repete a mesma pergunta, ele responde de forma diferente.**

# Como rodar:
cd v2_memoria
python chatbot_v2.py
Como rodar:
cd v2_memoria
python chatbot_v2.py

# Exemplo de saída:
# Chatbot com Memória (Regras) 
Oi! Como você está?
Você disse 'xablau' antes. Quer continuar nesse assunto?
Você disse 'xablau' antes. Quer continuar nesse assunto?

# Chatbot com Memória (ML) 
Oi! Como vai?
Você já me perguntou isso, mas eu repito: Oi! Como vai?
Até logo!

# Tecnologias utilizadas

Python Python 3.11.5
scikit-learn → para Machine Learning (Naive Bayes)
CountVectorizer → para transformar texto em números

# Objetivo:

Praticar Orientação a Objetos em Python.
Entender a diferença entre chatbots baseados em regras e Machine Learning.
Explorar a ideia de memória de contexto em assistentes virtuais.

# Próximos Passos:

Criar uma interface web simples (Flask ou Streamlit).
Melhorar a memória para lembrar conversas longas.
Integrar com uma API externa (ex: clima, piadas, etc.).





