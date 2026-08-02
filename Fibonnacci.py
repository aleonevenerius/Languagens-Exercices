valueF, valueS = 1, 0

i = int(input("Tell me a number and I will show you the sequence at Fibonacci: "))

while i > 0:
    soma = valueF+valueS
    print(f"{valueF}+{valueS}={soma}")
    valueS, valueF = valueF, soma
    i -= 1