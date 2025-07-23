turma = []

def cadastrar_aluno():
    while True:
        aluno = {}
        aluno["Nome"] = input("Digite o nome do aluno: ")
        aluno["Matricula"] = input("Digite a matrícula do aluno: ")
        turma.append(aluno)
        
        resposta = input("Deseja cadastrar outro aluno? (s/n): ")
        if resposta.lower() == "n":
            break

def listar_alunos():
    print(30 * "-")
    for indice, aluno in enumerate(turma, start=1):
        dados_do_aluno = ""
        for chave, valor in aluno.items():
            dados_do_aluno += f"{chave}: {str(valor)} | "
        print(f"{indice}. {dados_do_aluno.strip(' | ')}")
    print(30 * "-")

def identificar_aluno(identificador):
    for indice, aluno in enumerate(turma):
        if identificador == aluno["Nome"] or identificador == aluno["Matricula"]:
            return indice
    return -1

def inserir_notas(indice_aluno):
    lista_de_notas = []
    for i in range(3):
        nota = float(input(f"Insira a nota {i+1}: "))
        lista_de_notas.append(nota)
    turma[indice_aluno]["Notas"] = lista_de_notas

def remover_aluno(indice_aluno):
    return turma.pop(indice_aluno)

def calcular_media_do_aluno(indice_aluno):
    if "Notas" in turma[indice_aluno]:
        media = sum(turma[indice_aluno]["Notas"]) / len(turma[indice_aluno]["Notas"])
        return f"A média do aluno {turma[indice_aluno]['Nome']} é {media:.2f}"
    else:
        return f"O aluno {turma[indice_aluno]['Nome']} não tem notas cadastradas."

while True:
    print("\n" + 30 * "-")
    print("        ADM ESCOLAR")
    print(30 * "-")
    print("""
    1. Adicionar aluno
    2. Inserir notas do aluno
    3. Remover aluno
    4. Obter média do aluno
    5. Listar todos os alunos
    6. Sair
    """)
    
    opcao_selecionada = int(input("Selecione uma opção: "))
    
    if opcao_selecionada == 1:
        cadastrar_aluno()
        listar_alunos()

    elif opcao_selecionada == 2:
        identificador = input("Insira o nome ou a matrícula do aluno: ")
        indice = identificar_aluno(identificador)
        if indice == -1:
            print(f"Aluno '{identificador}' não foi encontrado.")
        else:
            inserir_notas(indice)
    
    elif opcao_selecionada == 3:
        identificador = input("Insira o nome ou a matrícula do aluno: ")
        indice = identificar_aluno(identificador)
        if indice == -1:
            print(f"Aluno '{identificador}' não foi encontrado.")
        else:
            aluno_removido = remover_aluno(indice)
            print(f"O aluno {aluno_removido['Nome']} foi removido com sucesso.")

    elif opcao_selecionada == 4:
        identificador = input("Insira o nome ou a matrícula do aluno: ")
        indice = identificar_aluno(identificador)
        if indice == -1:
            print(f"Aluno '{identificador}' não foi encontrado.")
        else:
            print(calcular_media_do_aluno(indice))

    elif opcao_selecionada == 5:
        listar_alunos()

    elif opcao_selecionada == 6:
        print(30 * "-")
        print("Programa encerrado.")
        print(30 * "-")
        break
