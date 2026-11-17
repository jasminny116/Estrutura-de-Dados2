def decimal_para_binario_recursivo(numero):
    if numero == 0:
        return "0"
    if numero == 1:
        return "1"
    return decimal_para_binario_recursivo(numero // 2) + str(numero % 2)

if __name__ == "__main__":
    num = 13
    resultado = decimal_para_binario_recursivo(num)
    print(f"O decimal {num} em binário (recursivo) é: {resultado}")
