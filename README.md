<h1 align="center" style="font-weight: bold">
    API Automação com Chat 💬
</h1>

<p align="center">
    <a href="#tech">Tecnologias</a> - 
    <a href="#iniciando">Iniciando o Projeto</a> -
    <a href="#endpoints">Endpoints</a> - 
    <a href="#colab">Colaboradores</a>
</p>

<p align="center">
    Permite a conexão com um chatbot de IA de forma mais fácil e com o contexto da empresa.
</p>

<h2 id="tech">Tecnologias 💻</h2>

- Python
- FastApi
- Pydantic
- SQLAlchemy
- SQLite
- Groq

<h2 id="iniciando">Iniciando o Projeto 🚀</h2>

<h3>Pré-Requisitos</h3>

- Git
- Python
- pip

<h3>Clonando o Projeto</h3>

<p>Crie uma pasta dedicada para colocar os projetos, se ainda não o fez, abra o seu terminal e digite: </p>

```bash
mkdir projetos-git
cd projetos-git
```

<br>
<p>Agora clone o projeto com o git, se estiver no windows use o git bash: </p>

```bash
git clone https://github.com/House-On/api-automacao
cd api-automacao
```

<br>
<p>
    Configure as variáveis de ambiente, <strong>crie um arquivo .env dentro da pasta api-automacao</strong>.
    Use o exemplo a seguir para colocar dentro do seu arquivo .env
</p>
.env (exemplo):

```yaml
ENV=dev
API_KEY={Sua API KEY do Groq}
MODELO_TEXTO={O modelo de IA de sua Escolha}
```

<h3>Instalando as dependências</h3>

<p>
    Antes de tudo, crie um ambiente virtual em python usando a biblioteca padrão do python, lembre de estar na pasta do projeto "api-automacao", no seu terminal digite:
</p>

```bash
cd api-automacao
python -m venv venv
```

<br>
<p>
    Ative o ambiente no seu terminal com:
</p>

<p><strong>No windows: </strong></p>

```bash
.\venv\Scripts\activate
```

<p><strong>No Linux: </strong></p>

```bash
source venv/bin/activate
```

<br>
Tenha certeza de que seu interpretador esteja no ambiente certo com:

```bash
pip list
```

<br>
Por fim, instale as dependencias do projeto a partir do `requirements.txt` com: 

```bash
pip install -r requirements.txt
```

<h3>Iniciando...</h3>

<p>
    Entre na pasta que definiu anteriormente, com o seu terminal digite: 
</p>

```bash
cd projetos-git/api-automacao
```

<p>
    E então comece o projeto usando o server padrão do fastapi com:
</p>

```bash
fastapi run app/main.py
```

<br>
<h2 id="endpoints">Endpoints 🚩</h2>

| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /</kbd> | Mostra uma mensagem padrão para o acesso à API
| <kbd>POST /chat/</kbd>|Envia a mensagem para o chatbot IA e retorna uma a sua resposta

<br>
<h2 id="colab">Colaboradores 👥</h2>

<p>Desenvolvedores da parte do backend e banco de dados do projeto.</p>

<table>
    <tr>
        <td align="center">
            <a href="https://github.com/MarcosHenriqueFr">
                <img src="https://avatars.githubusercontent.com/u/161951682?v=4" width="100px" alt="foto perfil MarcosHenriqueFr"><br>
                <sub>
                    <strong>Marcos Henrique<strong>
                </sub>
            </a>
        </td>
    </tr>

    <tr>
        <td align="center">
            <a href="https://github.com/LuizGustavo-029">
                <img src="https://avatars.githubusercontent.com/u/216095318?v=4" width="100px" alt="foto perfil LuizGustavo-029"><br>
                <sub>
                    <strong>Luiz Gustavo<strong>
                </sub>
            </a>
        </td>
    </tr>
</table>

<br>
<p><strong>Agradeço pela sua atenção!</strong></p>
