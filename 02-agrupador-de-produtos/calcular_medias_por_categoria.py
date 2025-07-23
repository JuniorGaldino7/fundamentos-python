produtos = [

{"nome": "Camiseta", "preço": 29.99, "categoria": "Roupas"},

{"nome": "Calça", "preço": 59.99, "categoria": "Roupas"},

{"nome": "Livro", "preço": 39.99, "categoria": "Livros"},

{"nome": "Notebook", "preço": 3999.99, "categoria": "Eletrônicos"},

{"nome": "Smartphone", "preço": 2999.99, "categoria": "Eletrônicos"}

]


def calcular_medias_por_categoria(lista):
    resultado = {}
    soma = {}
    quantidade = {}
    for produto in lista:
        
        if produto["categoria"] not in soma:
            quantidade[produto["categoria"]] = 0
            soma[produto["categoria"]] = 0
            resultado[produto["categoria"]] = 0

        
        quantidade[produto["categoria"]] += 1 
        soma[produto["categoria"]] += produto["preço"]

    for chave, valor in resultado.items():
        resultado[chave] = soma[chave] / quantidade[chave]

    return resultado

resultado = calcular_medias_por_categoria(produtos)
print(resultado)