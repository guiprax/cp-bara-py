testes = [
    (52.0, 1.75),   # IMC 17.0 → Abaixo do peso
    (70.0, 1.75),   # IMC 22.9 → Peso normal
    (85.0, 1.70),   # IMC 29.4 → Sobrepeso
    (110.0, 1.65),  # IMC 40.4 → Obesidade
]

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25.0:
        return "Peso normal"
    elif imc >= 25.0 and imc < 30.0:
        return "Sobrepeso"
    else:  
        return "Obesidade"


for peso, altura in testes:
  
    imc = peso / (altura ** 2)
    
  
    imc_arredondado = round(imc, 1)
    

    classificacao = classificar_imc(imc)
    

    print(f"Peso: {peso} kg | Altura: {altura} m")
    print(f"IMC: {imc_arredondado} - {classificacao}")
    print() 
