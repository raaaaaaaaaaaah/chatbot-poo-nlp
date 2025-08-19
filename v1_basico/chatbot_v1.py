
#Este chatbot demonstra dois modos de funcionamento:
#1. Baseado em regras simples (palavras-chave).
#2. Baseado em Machine Learning (Naive Bayes).




import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#CountVectorizer - Transforma frases em número (conta palavras)
#MultinomialNB - Classificar Naive Bayes 
# NLP + ML (scikit-learn)


Autor: Raquel Almeida



#Classe Abstrata

class EstrategiaResposta:
    def gerar_resposta(self, mensagem):
        raise NotImplementedError
    
#Estratégia baseada em regras
class RespostaRegras(EstrategiaResposta):
    def __init__(self):
        self.regras = {
            "oi":"Oi! Como você está?",
            "tchau": "Até logo! Foi bom conversar com você.",
            "ajuda":"Claro! Eu posso te ajudar com dúvidas simples."
        }

    def gerar_resposta(self, mensagem):
        for palavra, resposta in self.regras.items():
            if palavra in mensagem.lower():
                return resposta
            return "Desculpe, não entendi. Pode reformular?"
        
#Estratégia usando machine learning

# testando em ML, ele aprende com exemplos que vc da, então também consegue responder com palavras parecidas com a do treino

class RepostaML(EstrategiaResposta):
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.modelo = ModuleNotFoundError()
        self.intencoes = []
        self.respostas = []

# Ele aprende com exemplos de frases (intenção) e respostas 
# Exemplo : Frases como oi e olá > resposta = oi, como vai?

    def treinar(self, exemplos, respostas):
        self.intencoes = exemplos
        self.respostas = respostas
        X = self.vectorizer.transform(exemplos)
        y = list(range(len(respostas)))
        self.modelo.fit(X,y)
   

   #quando você manda uma mensagem - tranforma em número, o modelo prevê a intenção e escolhe a resposta certa
    def gerar_resposta(self, mensagem):
        X = self.vectorizer.transform([mensagem])
        pred = self.modelo.predict(X)[0]
        return self.respostas[pred]
    
#Classe principal chatbot

# A classe chatbot é o controlador principal, recebe uma estratégia (resposta regras ou respostas ML)
# sempre que alguém fala com ele, ele passa a mensagem para a estrategia escolhida e devolve a resposta

class Chatbot:
    def __init__(self, estrategia: EstrategiaResposta):
        self.estrategia = estrategia

    def responder(self, mensagem):
        return self.estrategia.gerar_resposta(mensagem)
    

    # ---------- test ---------

    #Teste com  regras 

    # teste com regras, ele entende o oi e ajuda se mandar, mas se vc mandar algo como xablau, ele informa que não entendeu


    print ("### Chat bot baseado em regras ####")
    bot_regras = Chatbot(RespostaRegras())
    print(bot_regras.responder("Oi"))
    print(bot_regras.responder("Preciso de ajuda"))
    print(bot_regras.responder("Xablau"))

    #Teste com machine learning

    

    print("\n### Chatbot com ML ###")
    exemplos = ["Oi", "Olá", "tchau", "adeus", "me ajuda", "preciso de suporte"]
    respostas = ["Oi! Como vai?", "Oi, Como vai?", "Até logo", "Até logo!",
                 "Claro, como posso te ajudar?", "Estou aqui para te ajudar!"]
    
    estrategia_ml = RespostaML()
    estrategia_ml.treinar(exemplos, respostas)

    bot_ml = Chatbot(estrategia_ml)
    print(bot_ml.responder("Oi"))
    print(bot_ml.responder("me ajuda por favor"))
    print(bot_ml.responder("Adeus"))
