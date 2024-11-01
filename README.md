# Sober Streak API

Este repositório contém a API desenvolvida em Django para o projeto **Sober Streak**, um aplicativo que funciona como uma mini rede social, permitindo que os usuários compartilhem com seus amigos quantos dias estão sem consumir bebidas alcoólicas.

## Descrição

Sober Streak é um aplicativo desenvolvido em Ionic que oferece uma interface intuitiva e interativa, promovendo a motivação e o apoio mútuo entre os usuários.

## Funcionalidades da API

- **Autenticação de Usuários**: Permite que os usuários se registrem e façam login.
- **Registro de Dias**: Os usuários podem registrar se consumiram bebida alcoólica em um determinado dia.
- **Ranking de Amigos**: Fornece dados sobre quantos dias os amigos estão sem beber.

## Tecnologias Utilizadas

- **Django**: Para o desenvolvimento da API.
- **Django REST Framework**: Para a construção de APIs RESTful.
- **MySQL**: Para o armazenamento de dados.

## Repositório do Projeto

O aplicativo que consome esta API pode ser encontrado no seguinte repositório: [Sober Streak App](https://github.com/davydmoraes/sober-strike).

## Contato

Para mais informações, entre em contato com [ronaldo.tbj@gmail.com].

## 🚀 Configuração do Projeto

### 1. Clone o projeto
```bash
git clone https://github.com/bragaronaldo/sober-streak-api.git
```
### 2. Navegue até a pasta do projeto
```bash
cd sobriety-streak-api
```
### 3. Crie um ambiente virtual:
```bash
python -m venv venv
```
### 4. Ative o ambiente virtual
No windows:
```bash
venv\Scripts\activate
```
No macOs/Linux:
```bash
source venv/bin/activate
```
### 4. Instale as dependências
```bash
pip install -r requirements.txt
```
### 5. Configuração de Ambiente
Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:
```bash
SECRET_KEY=seu_secret_key
DEBUG=
ALLOWED_HOSTS=localhost,127.0.0.1
ALLOWED_CORS=*
DB_NAME=seu_nome_do_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=
DB_PORT=
```
### 6. Rode as migrações
```bash
python manage.py migrate
```
### 7. Inicie o Servidor
```bash
python manage.py runserver
```
