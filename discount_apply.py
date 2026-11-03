#  função que calcula o preço final de um item após aplicar um desconto percentual.

# Neste laboratório, você vai escrever uma função que calcula o preço final de um item após aplicar um desconto percentual.

# Por exemplo, se o preço de um item é 50 e um desconto de 20 é aplicado, o valor do desconto é 10 e o preço final é 40.

# Objetivo: Cumprir as user stories abaixo e fazer todos os testes passarem para completar o laboratório.

# Histórias de Usuário:

# Você deve definir uma função chamada apply_discount.

# A função apply_discount deve receber exatamente dois parâmetros: price e discount.

# Se price não for um número (int ou float), a função deve retornar a string The price should be a number.

# Se discount não for um número (int ou float), a função deve retornar a string The discount should be a number.

# Se price for menor ou igual a 0, a função deve retornar a string The price should be greater than 0.

# Se discount for menor que 0 ou maior que 100, a função deve retornar a string The discount should be between 0 and 100.

# Se ambas as entradas forem válidas, a função deve calcular o desconto como uma porcentagem do preço.

# A função deve retornar o preço final após aplicar o desconto.

def apply_discount(price, discount):
    # 3. Verifica se o preço é um número (int ou float, excluindo booleanos)
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        return "The price should be a number"
    
    # 4. Verifica se o desconto é um número (int ou float, excluindo booleanos)
    if not isinstance(discount, (int, float)) or isinstance(discount, bool):
        return "The discount should be a number"
    
    # 5. Verifica se o preço é maior que 0
    if price <= 0:
        return "The price should be greater than 0"
    
    # 6. Verifica se o desconto está entre 0 e 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # 7 e 8. Calcula o preço final com o desconto aplicado e o retorna
    final_price = price * (1 - discount / 100)
    return final_price