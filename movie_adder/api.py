import requests
import os
from dotenv import load_dotenv

load_dotenv()


def obter_dados_filme(imdb_id):
    """
    Obtém os dados do filme usando a API OMDb.
    """
    api_key = os.getenv("OMDB_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "A variável de ambiente OMDB_API_KEY não está configurada.")

    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if dados.get("Response") == "True":
            return {
                "Título": dados.get("Title"),
                "Gênero": dados.get("Genre"),
                "Ano": dados.get("Year"),
                "Nota": dados.get("imdbRating"),
                "Assistido": "Não"
            }
        else:
            raise ValueError(f"Erro na API: {dados.get('Error')}")
    else:
        raise ConnectionError(
            f"Erro na conexão com a API. Status code: {response.status_code}")
