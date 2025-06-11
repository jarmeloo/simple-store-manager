# loja.py

# Dicionário global para armazenar os produtos
produtos = {
    101: {"nome": "Camiseta Branca", "preco": 39.90, "estoque": 10},
    102: {"nome": "Calça Jeans", "preco": 89.90, "estoque": 5},
    103: {"nome": "Tênis Esportivo", "preco": 199.90, "estoque": 7},
}

# Variáveis globais
vendas_realizadas = []
valor_total_vendido = 0
alteracoes = []  # ← lista de log das alterações

# -----------------------------
# Cadastro de produtos
# -----------------------------
def cadastrar_produto(codigo, nome, preco):
    if codigo in produtos:
        return f"Produto com código {codigo} já cadastrado."
    produtos[codigo] = {"nome": nome, "preco": preco, "estoque": 0}
    alteracoes.append(f"Produto cadastrado: {nome} (Cód. {codigo}) - R$ {preco:.2f}")
    return f"Produto '{nome}' cadastrado com sucesso."

# -----------------------------
# Gerenciamento de estoque
# -----------------------------
def atualizar_estoque(codigo, quantidade):
    if codigo not in produtos:
        return f"Produto com código {codigo} não encontrado."
    produtos[codigo]["estoque"] += quantidade
    alteracoes.append(f"Estoque atualizado: {produtos[codigo]['nome']} (Cód. {codigo}) +{quantidade} unidades")
    return f"Estoque do produto '{produtos[codigo]['nome']}' atualizado. Quantidade atual: {produtos[codigo]['estoque']}"

def consultar_estoque():
    if not produtos:
        return "Nenhum produto cadastrado."
    print("\n--- Estoque Atual ---")
    for codigo, dados in produtos.items():
        print(f"Código: {codigo} | Nome: {dados['nome']} | Estoque: {dados['estoque']}")
    print("----------------------")

# -----------------------------
# Registro de vendas
# -----------------------------
def registrar_venda(codigo, quantidade):
    global valor_total_vendido
    if codigo not in produtos:
        return f"Produto com código {codigo} não existe."
    if produtos[codigo]["estoque"] < quantidade:
        return f"Estoque insuficiente para o produto '{produtos[codigo]['nome']}'."
    produtos[codigo]["estoque"] -= quantidade
    total = quantidade * produtos[codigo]["preco"]
    vendas_realizadas.append((codigo, produtos[codigo]["nome"], quantidade, total))
    valor_total_vendido += total
    alteracoes.append(f"Venda realizada: {quantidade}x {produtos[codigo]['nome']} - Total R$ {total:.2f}")
    return f"Venda registrada: {quantidade}x {produtos[codigo]['nome']} - Total: R$ {total:.2f}"

# -----------------------------
# Exibir resumo final
# -----------------------------
def mostrar_resumo_final():
    print("\n=== RESUMO FINAL ===")

    print("\n📌 Alterações realizadas:")
    if alteracoes:
        for a in alteracoes:
            print(f"- {a}")
    else:
        print("Nenhuma alteração realizada.")

    print("\n🛒 Vendas realizadas:")
    if vendas_realizadas:
        for venda in vendas_realizadas:
            codigo, nome, quantidade, total = venda
            print(f"- {quantidade}x {nome} (Cód. {codigo}) - R$ {total:.2f}")
        print(f"\n💰 Valor total vendido: R$ {valor_total_vendido:.2f}")
    else:
        print("Nenhuma venda registrada.")

    print("\n📦 Estoque final:")
    for codigo, dados in produtos.items():
        print(f"- {dados['nome']} (Cód. {codigo}) | Estoque: {dados['estoque']}")
    print("====================\n")

# -----------------------------
# Menu de interação
# -----------------------------
def menu():
    while True:
        print("\n=== Loja Virtual ===")
        print("1. Cadastrar Produto")
        print("2. Atualizar Estoque")
        print("3. Consultar Estoque")
        print("4. Registrar Venda")
        print("5. Sair e Mostrar Resumo")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = int(input("Código do produto: "))
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            print(cadastrar_produto(codigo, nome, preco))

        elif opcao == "2":
            codigo = int(input("Código do produto: "))
            quantidade = int(input("Quantidade a adicionar: "))
            print(atualizar_estoque(codigo, quantidade))

        elif opcao == "3":
            consultar_estoque()

        elif opcao == "4":
            codigo = int(input("Código do produto: "))
            quantidade = int(input("Quantidade a vender: "))
            print(registrar_venda(codigo, quantidade))

        elif opcao == "5":
            mostrar_resumo_final()
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()