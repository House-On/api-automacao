
from groq import Groq
from dotenv import load_dotenv
from os import getenv

load_dotenv()

GROQ_KEY = getenv("API_KEY")
GROQ_MODEL = getenv("MODELO_TEXTO")

client = Groq(api_key=GROQ_KEY)

def enviar_para_groq(mensagem: str, descricao: str, nome: str):

    '''Método para comunicação com a interface do Groq

    Args:
        mensagem (str): mensagem do usuário vinda do controller do chat
        descricao (str): descrição geral da empresa que enviou a requisição
        nome (str): nome da empresa que enviou a requisição.

    Raises:
        Exception: Problema na comunicação com a interface do Groq.

    Returns:
        response.choices[0].message.content: Mensagem gerada pelo modelo de texto da IA a partir da mensagem do usuário.
    
    '''

    prompt_sistema = f"""
        Você é um assistente da empresa {nome} com descrição {descricao},
        seu trabalho é ajudar o dono da empresa para que ele tenha sucesso no seu empreendimento. Responda claramente e com paciência, usando bullet points.
        Mantenha sua resposta menor do que 120 palavras.
    """

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": mensagem}
            ],
            model=GROQ_MODEL
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Erro de consulta na IA: {e}"