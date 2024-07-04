import textwrap

def exibir_menu():
    menu = """
    ================ MENU ================
    [1]    Depositar
    [2]    Sacar
    [3]    Extrato
    [4]    Nova conta
    [5]    Listar contas
    [6]    Novo usuário
    [0]    Sair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito:    R$ {valor:.2f}")
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    except ValueError:
        print("\n@@@ Operação falhou! Valor inválido. @@@")
    
    return saldo, extrato


def sacar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor > 0:
            if valor <= saldo:
                saldo -= valor
                extrato.append(f"Saque:        R$ {valor:.2f}")
                print("\n=== Saque realizado com sucesso! ===")
            else:
                print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    except ValueError:
        print("\n@@@ Operação falhou! Valor inválido. @@@")
    
    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo:        R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        print(f"""
            Agência:      {conta['agencia']}
            C/C:          {conta['numero_conta']}
            Titular:      {conta['usuario']['nome']}
        """)
    print("==================================================")


def main():
    saldo = 0
    extrato = []
    usuarios = []
    contas = []
    numero_conta = 1
    agencia = "0001"

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, extrato = sacar(saldo, extrato)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            criar_conta(agencia, numero_conta, usuarios, contas)
            numero_conta += 1

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
