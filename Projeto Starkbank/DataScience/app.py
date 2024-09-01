from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from textblob import TextBlob
import os

app = Flask(__name__)

# Definir o pipeline de classificação
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', MultinomialNB()),
])

# Treinar o classificador com dados de exemplo
train_data = [
    # seus dados de treinamento
]
train_labels = [
    # suas labels de treinamento
]

text_clf.fit(train_data, train_labels)

def check_invoices():
    # sua função de verificação de faturas
    return pd.DataFrame()

def check_fraudulent_invoices():
    # sua função de verificação de faturas fraudulentas
    return pd.DataFrame()

def generate_all_reports():
    # sua função para gerar todos os relatórios
    return "Relatórios gerados."

def generate_anomalous_report():
    # sua função para gerar relatório de faturas anômalas
    return "Relatório de faturas anômalas gerado."

def generate_suspect_report():
    # sua função para gerar relatório de faturas suspeitas
    return "Relatório de faturas suspeitas gerado."

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def respond_to_query(query):
    query = query.lower()
    category = text_clf.predict([query])[0]

    if category == "ignore":
        return "Entendido. Não exibindo faturas anômalas."
    elif category == "check_invoices":
        sentiment = analyze_sentiment(query)
        if sentiment < 0:
            return "Entendido. Não exibindo faturas anômalas."
        else:
            anomalous_invoices = check_invoices()
            if not anomalous_invoices.empty:
                report_path = r"Faturas_Anomalas.xlsx"
                anomalous_invoices.to_excel(report_path, index=False)
                return f"Arquivo salvo no download como 'Faturas_Anomalas.xlsx'."
            else:
                return "Nenhuma fatura anômala detectada."
    elif category == "generate_report":
        return generate_all_reports()
    elif category == "generate_anomalous_report":
        return generate_anomalous_report()
    elif category == "generate_suspect_report":
        return generate_suspect_report()
    else:
        return "Para ajuda com pagamento, entre em contato com o suporte."

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    response = respond_to_query(user_message)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
