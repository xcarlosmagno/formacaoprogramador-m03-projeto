# -*- coding: utf-8 -*-
"""ProjetoOperacoesBancarias.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SMPnaY1KT_l-LEVlISK68wWrBKXA-zlc
"""

contas = []

def criar_conta():
  verificador_conta_existe = False
  dados_nova_conta = {}
  dados_nova_conta['numero_conta'] = input('\nDigite o número da nova conta: ')

  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == dados_nova_conta['numero_conta']:
      verificador_conta_existe = True
      break

  if verificador_conta_existe:
    print('\nO número informado já está associado à outra conta.')

  else:
    dados_nova_conta['saldo_conta'] = float(input('\nDigite o saldo da nova conta: '))
    contas.append(dados_nova_conta)
    print('\nOperação realizada com sucesso!')

def remover_conta():
  numero_conta = input('\nDigite o número da conta para a remoção: ')
  conta_encontrada = False

  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == numero_conta:
      conta_encontrada = True
      contas.remove(conta_em_consulta)
      print('\nOperação realizada com sucesso!')
      break

  if not conta_encontrada:
    print('\nConta inexistente. Remoção de conta não realizada!')

def listar_contas():
  if len(contas) == 0:
    print('\nNão há contas cadastradas.')

  else:
    for conta_em_consulta in contas:
      print(f"Conta: {conta_em_consulta['numero_conta']}\nSaldo: {conta_em_consulta['saldo_conta']:.2f}\n")

def adicionar_saldo_conta():
  numero_conta = input('\nDigite o número da conta:')

  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == numero_conta:
      valor_credito = float(input('Digite o valor a ser creditado:'))

      if valor_credito < 0:
        print('\nNão são permitidos valor menos que 0 (zero).')
        return

      else:
        conta_em_consulta['saldo_conta'] += valor_credito
        print('\nOperação realizada com sucesso.')
        return

  print('\nConta não encontrada.')

def remover_saldo_conta():
  numero_conta = input('\nDigite o número da conta:')

  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == numero_conta:
      valor_debito = float(input('Digite o valor a ser debitado:'))

      if valor_debito < 0:
        print('\nNão são permitidos valores menores que 0 (zero).')
        return

      else:
        conta_em_consulta['saldo_conta'] -= valor_debito
        print('\nOperação realizada com sucesso.')
        return

  print('\nConta não encontrada.')

def transferir_saldo():
  conta_partida = input('\nDigite o número da sua conta: ')
  verificar_etapa = 0

  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == conta_partida:
      verificar_etapa = 1
      conta_destino = input('\nDigite o número da conta de destino: ')

      if conta_destino != conta_partida:
        for conta_destino_em_consulta in contas:
          if conta_destino_em_consulta['numero_conta'] == conta_destino:
            valor_transferencia = float(input('\nDigite o valor a ser transferido: '))

            if valor_transferencia < 0:
              print('\nNão são permitidos valores menores que 0 (zero).')
              return

            elif valor_transferencia > conta_em_consulta['saldo_conta']:
              print(f"\nSaldo insuficiente. Valor em conta: R$ {conta_em_consulta['saldo_conta']:.2f}")
              return

            else:
              conta_em_consulta['saldo_conta'] -= valor_transferencia
              conta_destino_em_consulta['saldo_conta'] += valor_transferencia
              print('\nOperação realizada com sucesso.')
              return

      else:
        verificar_etapa = 2
        break

  if verificar_etapa == 0:
    print('\nA sua conta não foi encontrada.')

  elif verificar_etapa == 1:
    print('\nA conta de destino não foi encontrada.')

  elif verificar_etapa == 2:
    print('\nNão é possível transferir dinheiro para a mesma conta.')

def consultar_saldo():
  numero_conta = print('\nDigite o número da conta: ')

  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == numero_conta:
      print(f"Conta: {conta_em_consulta['numero_conta']}\nSaldo: {conta_em_consulta['saldo_conta']:.2f}\n")
      return

  print('\nA conta não foi encontrada.')

print('***** Bem vindo ao sistema bancário *****')

while True:

  print('\n*** Menu ***')
  print('0 - Sair')
  print('1 - Criar conta')
  print('2 - Remover conta')
  print('3 - Listar todas as contas')
  print('4 - Adicionar saldo (creditar)')
  print('5 - Remover saldo (debitar)')
  print('6 - Transferir saldo')
  print('7 - Consultar saldo')

  numero_operacao = input('\nSelecione a operação que deseja executar: ')

  if numero_operacao == '0':
    print('\nSistema encerrado.')
    break

  elif numero_operacao == '1':
    criar_conta()

  elif numero_operacao == '2':
    remover_conta()

  elif numero_operacao == '3':
    listar_contas()

  elif numero_operacao == '4':
    adicionar_saldo_conta()

  elif numero_operacao == '5':
    remover_saldo_conta()

  elif numero_operacao == '6':
    transferir_saldo()

  elif numero_operacao == '7':
    consultar_saldo()

  else:
    print('\nOperação inválida!')