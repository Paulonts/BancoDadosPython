def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): #quando tem a / tudo que vem antes eu sou obrigado a passar os dados sem parametros nomeados
                                                                    #depois da / eu posso passar os dados com parametros nomeados
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro("Palio", 1999, "ABC-1234",#parametros não nomeados, por posição.
             marca="Fiat", motor="1.0", combustivel="Gasolina"# parametros nomeados.
             ) # válido

#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido



#passar so por parametros nomeados coloque "*" antes de chamar as variaveis
def criar_carro (*, modelo, ano, placa, marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro (modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# válido
#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# inválido




#para passar os valores so por parametros nomeados coloque "*" antes de chamar as variaveis, e se colocar / depois de chamar os valores = parametros nao nomeados(por posicao)
def criar_carro (modelo, ano, placa, /, *, marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro ("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# inválido