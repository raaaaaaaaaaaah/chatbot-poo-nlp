"""
Chatbot em Python (Versão 2 - Com Memória de Contexto)
-------------------------------------------------------
Evolução do chatbot da versão 1:
- Mantém as estratégias baseadas em Regras e ML.
- Adiciona memória de contexto (lembra últimas interações).
- Pode dar respostas diferentes quando a pergunta se repete.

Autor: Raquel Almeida
"""

import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class EstrategiaResposta:
    """
    Classe abstrata para definir o contrato das estratégias de resposta.
    """
    def gerar_resposta(self, mensagem, memoria):
        raise NotImplementedError


class Memoria:
    """
    Classe que armazena as últimas interações (usuário e bot).
    """
    def __init__(self, tamanho=5):
        self.historico = []
        self.tamanho = tamanho

    def adicionar(self, usuario, bot):
        self.historico.append((usuario, bot))
        if len(self.historico) > self.tamanho:
            self.historico.pop(0)

    def ultimas_interacoes(self):
        return self.historico


class RespostaRegras(EstrategiaResposta):
    """
    Estratégia baseada em regras fixas, agora com memória de contexto.
    """
    def __init__(self):
        self.regras = {
            "oi": "Oi! Como você está?",
            "tchau": "Até logo! Foi bom conversar com você.",
            "ajuda": "Claro! Eu posso te ajudar com dúvidas simples."
        }

    def gerar_resposta(self, mensagem, memoria):
        msg = mensagem.lower()
        for palavra, resposta in self.regras.items():
            if palavra in msg:
                return resposta

        # Usa memória se não entendeu
        if memoria.ultimas_interacoes():
            ultima_pergunta, _ = memoria.ultimas_interacoes()[-1]
            return f"Você disse '{ultima_pergunta}' antes. Quer continuar nesse assunto?"

        return "Desculpe, não entendi. Pode reformular?"


class RespostaML(EstrategiaResposta):
    """
    Estratégia baseada em Machine Learning (Naive Bayes),
    agora adaptada para usar memória.
    """
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.modelo = MultinomialNB()
        self.respostas = []

    def treinar(self, exemplos, respostas):
        self.respostas = respostas
        X = self.vectorizer.fit_transform(exemplos)
        y = list(range(len(respostas)))
        self.modelo.fit(X, y)

    def gerar_resposta(self, mensagem, memoria):
        X = self.vectorizer.transform([mensagem])
        pred = self.modelo.predict(X)[0]
        resposta = self.respostas[pred]

        # Se repetiu a mesma pergunta, muda a resposta
        if memoria.ultimas_interacoes():
            ultima_pergunta, _ = memoria.ultimas_interacoes()[-1]
            if ultima_pergunta.lower() == mensagem.lower():
                resposta = "Você já me perguntou isso, mas eu repito: " + resposta

        return resposta


class Chatbot:
    """
    Classe principal do Chatbot com memória de contexto.
    """
    def __init__(self, estrategia: EstrategiaResposta):
        self.estrategia = estrategia
        self.memoria = Memoria()

    def responder(self, mensagem):
        resposta = self.estrategia.gerar_resposta(mensagem, self.memoria)
        self.memoria.adicionar(mensagem, resposta)
        return resposta


# ---------------------- Testando ---------------------- #
if __name__ == "__main__":
    print("### Chatbot com Memória (Regras) ###")
    bot_regras = Chatbot(RespostaRegras())
    print(bot_regras.responder("oi"))
    print(bot_regras.responder("xablau"))   # não entende
    print(bot_regras.responder("repete"))   # usa memória

    print("\n### Chatbot com Memória (ML) ###")
    exemplos = ["oi", "olá", "tchau", "adeus", "me ajuda", "preciso de suporte"]
    respostas = ["Oi! Como vai?", "Oi! Como vai?", "Até logo!", "Até logo!",
                 "Claro, como posso ajudar?", "Estou aqui para te ajudar!"]

    estrategia_ml = RespostaML()
    estrategia_ml.treinar(exemplos, respostas)

    bot_ml = Chatbot(estrategia_ml)
    print(bot_ml.responder("oi"))
    print(bot_ml.responder("oi"))   # já perguntou antes
    print(bot_ml.responder("adeus"))
