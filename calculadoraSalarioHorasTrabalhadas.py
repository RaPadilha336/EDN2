numero_funcionario = int(input("Digite o número da matrícula do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora (R$): "))

salario = horas_trabalhadas * valor_por_hora

print(f"Número do funcionário = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")
