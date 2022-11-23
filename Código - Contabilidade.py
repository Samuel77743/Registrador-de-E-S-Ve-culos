# cadastro de veiculos

input(str("Digite a placa do veículo de acordo com o modelo(AAA1111) ou modelo (AAA1A11): "))
input(str("Digite o modelo do veiculo: "))
input(str("Digite a montadora do veiculo: "))
int(input("Digite o ano de modelo do veiculo: "))

print("-----------------------------")
print(f"Veiculo cadastrado !")
print("-----------------------------")

# definindo horario

hentrada = int(input("Digite a hora de entrada do veículo:  "))
minentrada = int(input("Digite os minutos de entrada do veículo:  "))

hsaida = int(input("Digite a hora de saída do veículo:  "))
minsaida = int(input("Digite os minutos de saída do veículo:  "))

hfinal = hsaida - hentrada
if minentrada > minsaida:
    minfinal = (minsaida + 60) - minentrada
    hfinal = 0
else:
    minfinal = minsaida - minentrada

print("---------------------------------------------------------------------------")
print(f"O veículo ficou no estacionamento por {hfinal} horas e {minfinal} minutos.")
print("---------------------------------------------------------------------------")

# definindo valores por tempo

print("-------------------------------------")
print("Lista de valores por tempo de servico")
print("-------------------------------------")

print("1 HORA ---------- R$10 REAIS\nMEIA HORA ---------- R$5 REAIS\n**Apos uma hora, a cada 15 MIN R$2,50")

if hfinal == 00:
    if minfinal >= 15 and minfinal < 30:
        valor = + 2, 50
    elif minfinal == 30:
        valor = + 5
    elif minfinal >= 30 and minfinal < 60:
        valor = + 5
    elif minfinal < 15:
        valor = + 2, 50
elif hfinal > 0:
    if minfinal >= 15 and minfinal < 30:
        valor = (hfinal * 10) + 2, 50
    elif minfinal == 30:
        valor = (hfinal * 10) + 5
    elif minfinal >= 30 and minfinal < 60:
        valor = (hfinal * 10) + 5
    else:
        valor = hfinal * 10

print("---------------------------------------------")
print(f"O valor total do servico e de: R${valor}")
print("---------------------------------------------")
