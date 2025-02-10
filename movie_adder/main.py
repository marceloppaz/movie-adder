from .api import obter_dados_filme
from .planilha import adicionar_filme_planilha


def adicionar_filmes(imdb_ids, arquivo_planilha):
    for imdb_id in imdb_ids:
        dados_filme = obter_dados_filme(imdb_id)
        adicionar_filme_planilha(arquivo_planilha, dados_filme)


if __name__ == "__main__":
    imdb_ids = ["tt4216984"]
    arquivo_planilha = "Filmes.xlsx"
    adicionar_filmes(imdb_ids, arquivo_planilha)
