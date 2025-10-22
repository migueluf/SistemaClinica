## 1ª etapa: Permitir cadastro dos pacientes (nome, idade, telefone)


def cadastrar_paciente(pacientes): ## Opção 1
  print('\n ### CADASTRO DE NOVO PACIENTE ###')
  nome = input("Insira o nome do paciente: ")
  idade = input("Insira a idade do paciente: ")
  telefone = input("Insira o telefone do paciente")
 
  paciente = {'nome': nome, 'idade': idade, 'telefone': telefone}
  
  pacientes.append(paciente)

  print('Paciente cadastrado com sucesso')
  print(pacientes)

def buscar_paciente(pacientes): ## Opção 2
  if not pacientes:
    print("Nenhum paciente cadastrado!")
    return
  print("***** Busca de paciente pelo nome ******")
  nome_busca = input("Digite o nome a ser buscado: ").lower().strip()

  encontrados = [p for p in pacientes if nome_busca in p['nome'].lower()]

  if not encontrados:
    print(f"Não foi encontrada pessoa com o nome {nome_busca}")
  else:
    print(f"\n{len(encontrados)} pacientes encontrados que contém o nome {nome_busca}")
    for i, paciente in enumerate(encontrados, 1):
      print(f"\n{i} Nome: {paciente['nome']}")
      print(f"\n Idade {paciente['idade']}")
      print(f"\n telefone: {paciente['telefone']}")

def menu():
  print('SISTEMA CLINICA VIDA+')
  print('1 - Cadastro de cliente\n2 - Buscar por nome\n3 - Sair')

def main():
  pacientes = []
  while True:
    menu()
    opcao = int(input('Selecione a opção desejada'))

    if opcao == 1:
      cadastrar_paciente(pacientes)
    elif opcao == 2:
      buscar_paciente(pacientes)
    elif opcao == 3:
      break
main()



## 2ª Calcule e exiba: Número total de pacientes, Idade média dos pacientes e Paciente mais novo e mais velho






## 3ª Permitir busca de um paciente pelo nome





## 4ª Exibir todos os pacientes cadastrados de forma organizada 




## Use listas e dicionários para armazenar os dados* Implamente um menu simples para navegação* Trate possíveis erros de entrada* O programa deve funcionar até o usuário apertar em Sair



