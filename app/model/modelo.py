import joblib

# Carrega o Model
modelo = joblib.load('modelo_cluster_cartao_credito.pkl')

respostas = {
    0: "São clientes que possuem grandes limites totais no cartão, mas não são bons pagadores, logo, não têm muito limite disponível.",
    1: "Clientes que gastam muito com saques. Compram pouco no crédito e são bons pagadores.",
    2: "Clientes com maior preferência em usar débito e saques ao invés do crédito.",
    3: "São os clientes que menos utilizam os serviços financeiros.",
    4: "Utilizam muito o serviço de crédito e são bons pagadores."
}