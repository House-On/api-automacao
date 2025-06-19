
def reposta_api(dado = None, mensagem = "Sucesso", status = True, erro = None):
    return {
        "status": status,
        "mensagem": mensagem,
        "dado": dado,
        "erro": erro
    }