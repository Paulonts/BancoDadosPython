def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") #melhor para se usar
salvar_carro(**{"marca": "Fiat","modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) #dicionario
