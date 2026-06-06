pegar_peso = (input("Digite seu peso em kg: (ex: 70): "))
pegar_altura = (input("Digite sua altura em metros: (ex: 1.75 ou 1,75): "))

peso = float(pegar_peso.replace(",", "."))
altura = float(pegar_altura.replace(",", "."))

def calcularIMC(peso, altura):
    imc = peso / (altura * altura)
    return imc

print(f"Seu IMC é: {calcularIMC(peso, altura):.2f}")