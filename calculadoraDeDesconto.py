produto = "Camiseta"
preco = 50.00
desconto = 0.20

valor_desconto = preco * desconto
preco_final = preco - valor_desconto

print(f"Produto: {produto}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

