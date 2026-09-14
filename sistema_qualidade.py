print("Sistema de Controle de Qualidade de Peças Industriais")

# Estruturas usadas para armazenar os dados
pecas = []
caixa_atual = []
caixas_fechadas = []

# Cada caixa comporta no máximo 10 peças
CAPACIDADE_CAIXA = 10

def validar_peca(peso, cor, comprimento):
    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("Peso fora do padrão de 95g a 105g")

    if cor not in ["azul", "verde"]:
        motivos.append("Cor inválida: deve ser azul ou verde")

    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora do padrão de 10cm a 20cm")

    return motivos

def cadastrar_peca():
    print("\n--- CADASTRO DE NOVA PEÇA ---")

    id_peca = input("Digite o ID da peça: ").strip()

    for peca_existente in pecas:
        if peca_existente["id"] == id_peca:
            print("Erro: já existe uma peça com esse ID.")
            return

    try:
        peso = float(input("Digite o peso em gramas: ").replace(",", "."))
        cor = input("Digite a cor da peça: ").strip().lower()
        comprimento = float(
            input("Digite o comprimento em centímetros: ").replace(",", ".")
        )
    except ValueError:
        print("Erro: peso e comprimento devem ser números.")
        return

    motivos = validar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": "Reprovada" if motivos else "Aprovada",
        "motivos": motivos
    }

    pecas.append(peca)

    if motivos:
        print(f"Peça {id_peca} REPROVADA.")
        for motivo in motivos:
            print(f"- {motivo}")
    else:
        caixa_atual.append(peca)
        print(f"Peça {id_peca} APROVADA e adicionada à caixa atual.")

        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas_fechadas.append(caixa_atual.copy())
            caixa_atual.clear()
            print("Caixa fechada com 10 peças. Uma nova caixa foi iniciada.")

def listar_pecas():
    print("\n--- PEÇAS APROVADAS ---")
    encontrou_aprovada = False

    for peca in pecas:
        if peca["status"] == "Aprovada":
            encontrou_aprovada = True
            print(
                f"ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm"
            )

    if not encontrou_aprovada:
        print("Nenhuma peça aprovada cadastrada.")

    print("\n--- PEÇAS REPROVADAS ---")
    encontrou_reprovada = False

    for peca in pecas:
        if peca["status"] == "Reprovada":
            encontrou_reprovada = True
            print(
                f"ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm"
            )
            print(f"Motivos: {', '.join(peca['motivos'])}")

    if not encontrou_reprovada:
        print("Nenhuma peça reprovada cadastrada.")
def reorganizar_caixas():
    caixas_fechadas.clear()
    caixa_atual.clear()

    for peca in pecas:
        if peca["status"] == "Aprovada":
            caixa_atual.append(peca)

            if len(caixa_atual) == CAPACIDADE_CAIXA:
                caixas_fechadas.append(caixa_atual.copy())
                caixa_atual.clear()


def remover_peca():
    print("\n--- REMOVER PEÇA ---")
    id_peca = input("Digite o ID da peça que deseja remover: ").strip()

    for peca in pecas:
        if peca["id"] == id_peca:
            pecas.remove(peca)
            reorganizar_caixas()
            print(f"Peça {id_peca} removida com sucesso.")
            return

    print("Peça não encontrada.")   
# Menu principal
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas e reprovadas")
    print("3. Remover uma peça")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_peca()

    elif opcao == "2":
        listar_pecas()

    elif opcao == "3":
        print("Você escolheu remover uma peça.")

    elif opcao == "4":
        print("Você escolheu listar as caixas fechadas.")

    elif opcao == "5":
        print("Você escolheu gerar o relatório final.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Digite um número de 0 a 5.")