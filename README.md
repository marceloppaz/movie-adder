# Movie Adder

Movie Adder é um pacote Python que permite adicionar filmes a uma planilha do Excel com informações obtidas automaticamente da API OMDb.

## Recursos
- Consulta informações de filmes pelo IMDb ID na API OMDb.
- Adiciona os filmes a uma planilha Excel preservando a formatação.
- Indica automaticamente se o filme foi assistido ou não.

## Instalação
Para instalar o Movie Adder, utilize o `pip`:
```bash
pip install movie-adder
```

## Configuração
Antes de utilizar o pacote, é necessário configurar uma chave de API da OMDb:

1. Registre-se em [OMDb API](https://www.omdbapi.com/) e obtenha sua chave de API.
2. Altere o arquivo `.env` no diretório do projeto e adicione sua api na linha:
   ```
   OMDB_API_KEY="SUA_CHAVE_AQUI"
   ```

## Uso

### Exemplo de Uso
```python
from movie_adder import adicionar_filmes

imdb_ids = ["tt4216984"]  # Lista de IMDb IDs dos filmes
arquivo_planilha = "Filmes.xlsx"  # Nome do arquivo Excel

adicionar_filmes(imdb_ids, arquivo_planilha)
```

Isso adiciona os filmes especificados à planilha `Filmes.xlsx` com as seguintes colunas:

| Título | Gênero | Ano | Nota IMDb | Assistido |
|--------|--------|-----|-----------|-----------|
| Exemplo | Ação  | 2020 | 7.5       | Não       |

### Uso via Linha de Comando

Depois de instalar o pacote, você também pode rodar diretamente pelo terminal:
```bash
adicionar-filme tt4216984 Filmes.xlsx
```

## Dependências
- `requests`
- `xlwings`
- `python-dotenv`

Se precisar instalar manualmente, utilize:
```bash
pip install requests xlwings python-dotenv
```

## Contribuição
Contribuições são bem-vindas! Para contribuir:
1. Fork este repositório.
2. Crie uma branch (`git checkout -b minha-feature`).
3. Faça commit das alterações (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
