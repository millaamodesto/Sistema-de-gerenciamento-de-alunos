from time import sleep


def add(matricula):
    if cadastro == [()]:
        nome = str(input("Informe o nome: "))
        telefone = str(input("Informe o telefone: "))
        endereco = str(input("Informe o endereço: "))
        aluno = {'matricula':matricula ,'aluno':nome,'contato': telefone,
                 'endereco':endereco, 'ad1': 'Não lançada', 'ad2': 'Não lançada',
                 'media': 'Não lançada', 'recuperacao': 'Não lançada'}
        print(31 * '-')
        print("Usuário cadastrado com sucesso!")
        print(31 * '-')
        return cadastro.append(aluno)
    else:
        for Naluno in cadastro:
            for dados in Naluno:
                if matricula in Naluno.values():
                    print("Usuário já cadastrado no sistema !:")
                    print(Naluno)
                    print()
                    break
                else:
                    nome = str(input("Informe o nome: "))
                    telefone = str(input("Informe o telefone: "))
                    endereco = str(input("Informe o endereço: "))
                    aluno = {'matricula':matricula ,'aluno':nome,'contato': telefone,
                            'endereco':endereco, 'ad1': 'Não lançada', 'ad2': 'Não lançada',
                            'media': 'Não lançada', 'recuperacao': 'Não lançada'}
                    print(30 * '-')
                    print("Usuário cadastrado com sucesso!")
                    print(30 * '-')
                    return cadastro.append(aluno)

def busca(matricula):
    for alunos in cadastro:
        for dados in alunos:
            if matricula in alunos.values():
                print("\nAluno encontrado!\n")
                print(30*'-')
                print("        Dados do aluno")
                print(30*'-')
                info(alunos)
                print()
                return 0

    print(35 * '-')
    print('Aluno não encontrado no sistema...')
    print(35 * '-')
    return 1

def edit(matricula):
    for Naluno in cadastro:
        for dados in Naluno:
            if matricula in Naluno.values():
                info(Naluno)
                print("Qual dado deseja alterar? \n")
                print("[1] MATRICULA: " + Naluno.setdefault('matricula'))
                print("[2] NOME: " + Naluno.setdefault('aluno'))
                print("[3] NUMERO: " + Naluno.setdefault('contato'))
                print("[4] ENDERECO: " + Naluno.setdefault('endereco'))
                op_alter = int(input("\nInforme o número da opção: "))
                if op_alter == 1:
                    new_mat = input("Informe o novo número da matricula: ")
                    Naluno.update(matricula=new_mat)
                elif op_alter == 2:
                    new_name = input("Informe o novo nome: ")
                    Naluno.update(aluno=new_name)
                elif op_alter == 3:
                    new_number = input("Informe o novo telefone: ")
                    Naluno.update(contato=new_number)
                elif op_alter == 4:
                    new_ender = input("Informe o novo endereço: ")
                    Naluno.update(endereco=new_ender)
                print("\nUsuário editado com sucesso!")
                return 0

def excluir(matricula):
    for alunos in cadastro:
        for user in alunos:
            if matricula in alunos.values():
                cadastro.remove(alunos)
                print("\nAluno removido do sistema!\n")
                return 0

def note(matricula):
    for alunos in cadastro:
        for dados in alunos:
            if matricula in alunos.values():
                new_ad1 = float(input("Informe a AD1: "))
                new_ad2 = float(input("Informe a AD2: "))
                print(f'AD1: {new_ad1}')
                print(f'AD2: {new_ad2}')
                new_media = (new_ad1 + new_ad2) / 2.0
                print(f'MÉDIA: {new_media}')
                new_ad1 = str(new_ad1)
                new_ad2 = str(new_ad2)
                new_media1 = str(new_media)
                alunos.update(ad1=new_ad1)
                alunos.update(ad2=new_ad2)
                alunos.update(media=new_media1)
                if new_media < 7.0:
                    new_rec=float(input("Informe a NOTA DE RECUPERAÇÃO: "))
                    new_rec=str(new_rec)
                    alunos.update(recuperacao=new_rec)
                    info(alunos)
                    return 0
                else:
                    return 0

def info(alunos):
    print("MATRICULA: " + alunos.setdefault('matricula'))
    print("NOME: " + alunos.setdefault('aluno'))
    print("TELEFONE: " + alunos.setdefault('contato'))
    print("ENDERECO: " + alunos.setdefault('endereco'))
    print(30*'-')
    print("NOTA DA AD1: " + alunos.setdefault('ad1'))
    print("NOTA DA AD2: " + alunos.setdefault('ad2'))
    print("NOTA DA MÉDIA: " + alunos.setdefault('media'))
    if alunos.setdefault('recuperacao') != 'Não lançada':
        print("NOTA DA RECUPERAÇÃO: " + alunos.setdefault('recuperacao'))
    else:
        print("não há nota de recuperação ")
        print(30*'-')

def relatorios():
    print(''' 
  [1] - Gerar lista de frequência
  [2] - Gerar relatório de notas
  [3] - Gerar relatório final da disciplina\n ''')
    op_dados = int(input("Informa a opção: "))
    if op_dados == 1:
        print('|' + '-' * 70 + '|')
        print(f'| {"---------- LISTA DE FREQUÊNCIA ----------".center(68)} |')
        print('|' + '-' * 70 + '|')
        print(f'|{"MATRICULA".center(11)} | {"ALUNO".center(20)} | {"ASSINATURA".center(32)} |')
        print('|' + '-' * 70 + '|') 
        for alunos in cadastro:
            if alunos != ():
                print("|" + alunos.setdefault('matricula').center(12) + "|" + alunos.setdefault('aluno').center(22) + ('| ________________________________ |') ) 
    if op_dados == 2:
        print('|' + '-' * 83 + '|')
        print(f'| {"---------- RELATÓRIO DE NOTAS ----------".center(81)} |')
        print('|' + '-' * 83 + '|')
        print(f'|{"MATRICULA".center(11)} | {"ALUNO".center(11)} | {"AD1".center(11)} | {"AD2".center(11)} | {"MÉDIA".center(11)} | {"RECUPERAÇÃO".center(12)} |')
        print('|' + '-' * 83 + '|') 
        for alunos in cadastro:
            if alunos != ():
                print("|" + alunos.setdefault('matricula').center(12) + "|" + alunos.setdefault('aluno').center(13) + "|" + alunos.setdefault('ad1').center(13) + "|" + alunos.setdefault('ad2').center(13) + "|" + alunos.setdefault('media').center(13) + "|" + alunos.setdefault('recuperacao').center(14) + "|" ) 

    if op_dados == 3:
        print("| ---------- RELATÓRIO FINAL DA DISCIPLINA ---------- |")


op = -1
aluno = {}
cadastro = [()]

while op != 0:
    print(38 * '=')
    print("               |FADAM|")
    print(38 * '=')
    print('''- SISTEMA DE GERENCIAMENTO DO ALUNO -
--------------------------------------
    [1] - Cadastrar Aluno
    [2] - Buscar Aluno
    [3] - Editar dados do Aluno
    [4] - Excluir Aluno
    [5] - Lançar Notas
    [6] - Relatórios
    [0] - Sair''')
    op = int(input("\nEscolha uma opção: "))
    if op == 1:
        matricula = input("Informe o número da matrícula: ")
        add(matricula)
        sleep(2)
    elif op == 2:
        if cadastro != [()]:
            matricula = input("\nInforme a matrícula: ")
            busca(matricula)
        else:
            print("\nAinda não há usuários cadastrados!\n")

    elif op == 3:
        if cadastro != [()]:
            matricula = input("\nInforme a matrícula do aluno que deseja realizar alterações: ")
            edit(matricula)
        else:
            print("\nAinda não há usuários cadastrados!\n")

    elif op == 4:
        if cadastro != [()]:
            matricula = input("\nInforme a matrícula do aluno a ser removido: ")
            excluir(matricula)
        else:
            print(60 * '=')
            print('''\nNão possui alunos cadastrados no sistema... 
\nRealize o devido cadastro de alunos a serem excluídos.\n''')
            print(60 * '=')

    elif op == 5:
        if cadastro != [()]:
            matricula = input("Informe a matrícula do aluno que deseja lançar as notas: ")
            note(matricula)
        else:
            print("Matricula não cadastrada, utilize outra !")

    elif op == 6:
        if cadastro != [()]:
            relatorios()
        else:
            print("Não há usuários!")

    elif op == 0:
        print("Usuário deslogado do sistema...\nOBRIGADA!\n")
        exit(0)
