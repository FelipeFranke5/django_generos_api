
# API de gêneros

Um projeto simples feito para consolidar meus conhecimentos em geração de API's, usando Django vanilla.


## O que a API faz?

Basicamente, se trata de um CRUD simples. Cria/lista/atualiza/apaga um ou mais gêneros de filmes.


## Testes?

A API pode facilmente ser testada via Postman, ou usando os arquivos .http que inclui no app 'genres'. Nesse ponto, a ideia é ainda não incluir DRF e nem um API que pode ser testado via navegador (Mas será o meu próximo API, provavelmente).


## Rodar o projeto (localmente)?

Se por algum motivo você que está lendo deseja aproveitar algum conceito desse projeto, fique à vontade! Você pode facilmente instalar as dependências da seguinte forma:

1 - Clone o projeto:

```bash
git clone https://github.com/FelipeFranke5/django_generos_api
```

2 - Entre na pasta do projeto:

```bash
cd django_generos_api
```

3 - Crie a venv:

Linux:

```bash
python3 -m venv .venv
```

Windows:

```bash
python -m venv .venv
```

4 - Ative a venv:

Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

5 - Instale as dependências:

```bash
pip install -r requirements.txt
```

Pronto! O projeto estará à sua disposição, conforme a convenção da documentação oficial do Django:
https://docs.djangoproject.com/en/4.2/


## Inspiração

Esse projeto é um espelho do flix-api em seu estágio inicial, com algumas modificações. Créditos ao ADM, a base vêm forte!

Link do repositório:
https://github.com/pycodebr/flix-api
