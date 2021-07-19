import requests

def register_kwh_data(load, kwh, user="admin"):
    """
    Registra uma nova linha na tabela Kwh do banco de dados.

    Args:
        load: String com o nome do equipamento registrado na tabela
              Load do banco.
        kwh: float com o valor do consumo em kWh.
        user: String com o nome do usuário registrado na tabela 
              Users do banco. (default="admin")

    Returns:
        status_code: Código Http da requisição.
    """

    url = f'https://noseri-api.herokuapp.com/api/{user}/kwh'

    data = {
        'load': load,
        'kwh': kwh,
        }

    response = requests.post(url, data = data)
    return response.status_code


def register_new_load(load):
    """
    Registra uma nova carga na tabela Load do banco de dados.

    Args:
        load: String com o nome do novo equipamento a ser registrado.

    Returns:
        status_code: Código HTTP da requisição.
    """
    url = 'https://noseri-api.herokuapp.com/api/load'

    data = {'load': load}

    response = requests.post(url, data)
    return response.status_code