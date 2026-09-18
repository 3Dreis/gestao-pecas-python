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
def listar_caixas():
    print("\n--- CAIXAS FECHADAS ---")

    if not caixas_fechadas:
        print("Nenhuma caixa fechada ainda.")
    else:
        numero_caixa = 1

        for caixa in caixas_fechadas:
            ids_pecas = []

            for peca in caixa:
                ids_pecas.append(peca["id"])

            print(
                f"Caixa {numero_caixa}: "
                f"IDs: {', '.join(ids_pecas)}"
            )

            numero_caixa += 1

    print("\n--- CAIXA ATUAL ---")

    if caixa_atual:
        ids_atuais = []

        for peca in caixa_atual:
            ids_atuais.append(peca["id"])

        print(
            f"Peças armazenadas: {len(caixa_atual)} de "
            f"{CAPACIDADE_CAIXA} | IDs: {', '.join(ids_atuais)}"
        )
    else:
        print("A caixa atual está vazia.")

def gerar_relatorio():
    total_aprovadas = 0
    total_reprovadas = 0

    for peca in pecas:
        if peca["status"] == "Aprovada":
            total_aprovadas += 1
        else:
            total_reprovadas += 1

    caixas_utilizadas = len(caixas_fechadas)

    if caixa_atual:
        caixas_utilizadas += 1

    print("\n--- RELATÓRIO FINAL ---")
    print(f"Total de peças cadastradas: {len(pecas)}")
    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print(f"Caixas fechadas: {len(caixas_fechadas)}")
    print(f"Peças na caixa atual: {len(caixa_atual)}")
    print(f"Quantidade de caixas utilizadas: {caixas_utilizadas}")

    if total_reprovadas > 0:
        print("\n--- MOTIVOS DE REPROVAÇÃO ---")

        for peca in pecas:
            if peca["status"] == "Reprovada":
                motivos = ", ".join(peca["motivos"])
                print(f"ID {peca['id']}: {motivos}")



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
        remover_peca()  

    elif opcao == "4":
        listar_caixas()

    elif opcao == "5":
            gerar_relatorio()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Digite um número de 0 a 5.")