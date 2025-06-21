
def resposta_api(dados = None, mensagem_sistema = "Sucesso", status_code = 404, erro = None):
    '''Resposta padrão da api para quem enviou a requisição
    
    Args:
        dados: Representa a resposta final para o usuário da api.
        mensagem_sistema: Representa a mensagem do sistema em relação à requisição.
        status_code: Representa uma abstração do código HTTP para o frontend.

    
    '''

    return {
        "status": status_code,
        "mensagem": mensagem_sistema,
        "dado": dados,
        "erro": erro
    }