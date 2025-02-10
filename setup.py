from setuptools import setup, find_packages

setup(
    name="movie-adder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "xlwings",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "adicionar-filme=movie_adder.main:adicionar_filmes"
        ]
    },
    author="Seu Nome",
    author_email="seu@email.com",
    description="Um pacote para adicionar filmes em planilhas do Excel usando a API OMDb.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/marceloppaz/movie-adder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
