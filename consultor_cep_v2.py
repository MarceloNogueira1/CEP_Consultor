import requests



def consulta(cep):
    global adress_data
    r = requests.get(f'https://viacep.com.br/ws/{cep}/json')
    adress_data = r.json()


def resultado():
    global cep_resultado
    global rua_resultado
    global complemento_resultado
    global bairro_resultado
    global estado_resultado
    global ddd_resultado
    global titulo_resultado
    
    titulo_resultado = 'RESULTADO'
    cep_resultado = adress_data['cep']
    rua_resultado = adress_data['logradouro']
    complemento_resultado = adress_data['complemento']
    bairro_resultado = adress_data['bairro']
    estado_resultado = adress_data['uf']
    ddd_resultado = adress_data['ddd']







