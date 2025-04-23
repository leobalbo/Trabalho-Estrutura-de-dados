# Dicionários
orientadores = {}

def exibir_menu():
    print("""
========== MENU ==========
1. Cadastrar alunos e orientadores
2. Registrar versões do TCC entregues
3. Atribuir notas dos orientadores
4. Verificar pendências de entrega por aluno
5. Gerar relatórios para o orientador
6. Sair
===========================
""")

def cadastrar_orientador():
    print("Função de cadastro de orientador em desenvolvimento...\n")


while True:
    exibir_menu()
    
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Por favor, digite um número válido.\n")
        continue

    match opcao:
        case 1:
            cadastrar_orientador()
        case 2:
            print("Função de registro de versões em desenvolvimento...\n")
        case 3:
            print("Função de atribuição de notas em desenvolvimento...\n")
        case 4:
            print("Função de verificação de pendências em desenvolvimento...\n")
        case 5:
            print("Função de geração de relatórios em desenvolvimento...\n")
        case 6:
            print("Saindo do sistema. Até logo!")
            break
        case _:
            print("Opção inválida. Tente novamente.\n")
