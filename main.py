## 1ª etapa: Permitir cadastro dos pacientes (nome, idade, telefone)

def cadastrar_paciente():
  print('\n ### CADASTRO DE NOVO PACIENTE ###')
  nome = input("Insira o nome do paciente: ")
  idade = input("Insira a idade do paciente: ")
  telefone = input("Insira o telefone do paciente")
 
  paciente = {'nome': nome, 'idade': idade, 'telefone': telefone}
  pacientes = []
  pacientes.append(paciente)

  print('Paciente cadastrado com sucesso')
  print(pacientes)

def menu():
  print('SISTEMA CLINICA VIDA+')

def main():
  while True:
    menu()
    opcao = int(input('Selecione a opção desejada'))

    if opcao == 1:
      cadastrar_paciente()
    elif opcao == 2:
      break
main()



## 2ª Calcule e exiba: Número total de pacientes, Idade média dos pacientes e Paciente mais novo e mais velho






## 3ª Permitir busca de um paciente pelo nome





## 4ª Exibir todos os pacientes cadastrados de forma organizada 




## Use listas e dicionários para armazenar os dados* Implamente um menu simples para navegação* Trate possíveis erros de entrada* O programa deve funcionar até o usuário apertar em Sair



