regras = {
    "febre e tosse": "Gripe",
    "febre e dor de cabeça": "Dengue",
    "tosse e falta de ar": "Asma",
    "fadiga e dor muscular": "Virose",
    "dor de garganta e febre": "Faringite",
    "dificuldade para respirar e tosse": "Pneumonia",
    "erupção cutânea e febre": "Varicela",
}

dieta_recomendacao = {
    "Gripe": ["Sopas quentes", "Chá de gengibre", "Frutas ricas em vitamina C"],
    "Dengue": ["Água de coco", "Frutas frescas", "Suco de laranja"],
    "Asma": ["Alimentos ricos em ômega-3", "Verduras e legumes", "Maçãs"],
    "Virose": ["Alimentos leves", "Água", "Sopas", "Arroz integral"],
    "Faringite": ["Chá de mel com limão", "Alimentos suaves", "Sopas mornas"],
    "Pneumonia": ["Alimentos ricos em proteínas", "Sopas nutritivas", "Frutas frescas"],
    "Varicela": ["Alimentos ricos em vitamina A", "Sopas de legumes", "Suco de cenoura"],
}

def diagnosticar(sintomas):
    sintomas_str = " e ".join(sorted(sintomas))
    diagnostico = regras.get(sintomas_str, "Diagnóstico não encontrado")
    recomendacao_alimentos = dieta_recomendacao.get(diagnostico, "Nenhuma recomendação de dieta disponível.")
    return diagnostico, recomendacao_alimentos

sintomas_usuario = ["febre", "tosse"]
diagnostico, recomendacao = diagnosticar(sintomas_usuario)

print(f"Diagnóstico: {diagnostico}")
print(f"Recomendação de alimentos: {recomendacao}")
