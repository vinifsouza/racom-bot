

# Racom Chatbot

<!-- infos to portfolio
<iconfy>icon->vscode-icons:file-type-python<iconfy>
<iconfy>icon->logos:typescript-icon<iconfy>
<iconfy>icon->vscode-icons:file-type-mysql<iconfy>
<logo-url>logo_url->https://i.imgur.com/Kjc7lfV.png<logo-url>
-->

Chatbot construido com o framework Rasa.

![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54) [![Rasa](https://img.shields.io/badge/rasa-2.8.3-000000.svg?style=flat-square)](https://rasa.com/docs/rasa/) ![Scrapy](https://img.shields.io/badge/scrapy-2.5.0-60a839.svg?style=flat-square) ![Docker](https://img.shields.io/badge/docker-%2300f.svg?logo=docker&logoColor=white) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?logo=node.js&logoColor=white) ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?logo=typescript&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?logo=mysql&logoColor=white) 

# Como executar

Necessário instalar Docker e Docker Compose.

Para inicializar a aplicação, basta executar o comando abaixo na raiz do projeto:

```properties
docker-compose up
```

### Cainais
- **Telegram**: [@racom_bot](http://t.me/racom_bot)
- **Webchat**: [:4445](http://localhost:4445)

### Portas utilizadas

- `localhost:`**`3306`**: Racom Banco de dados (MySQL)
- `localhost:`**`4040`**: Túnel de conexão (Ngrok)
- `localhost:`**`4444`**: Racom API (Node.js)
- `localhost:`**`4445`**: Webchat
- `localhost:`**`5002`**: Rasa API
- `localhost:`**`5005`**: Rasa Server
- `localhost:`**`5055`**: Rasa Action Server

### Observações

* Ao executar a aplicação, o server do chatbot irá ser executado na porta `:5005` e irá criar um túnel nessa porta para que o server possa ser acessado através da rede externa, em vez de somente local.

* Quando Ngrok executa, ele gera uma URL aleatória. O arquivo `/chatbot/main.py` chamará o módulo `/chatbot/support/set_telegram_config.py` que irá extrair essa URL e atualizar o arquivo `chatbot/credentials.yml` em tempo de execução, definido a variável `$TELEGRAM_URL` com este valor. Com isso, o chatbot poderá ser utilizado no Telegram sem necessidade de outra configuração.

* A penúltima etapa da execução é treinamento do modelo. O output do progresso de treinamento é incompatível com o terminal do Docker, por isso pode parecer que o build travou na mensagem `Training NLU model...` mas está sendo executado em segundo plano.

# Estrutura

### Aplicações
* **faq**: Aplicação que utiliza o framework Scrapy para extrair os FAQs do site da Fiocruz e alimentar o banco de dados com as informações extraídas.

* **api**: Aplicação em TypeScript e Node.js para integração do banco de dados com o chatbot
 
* **chatbot**: Chatbot construído em Rasa para atendimento automatizado para auxílio de dúvidas sobre Coronavírus.

### Diretórios

```
.
├── api - Diretório da API para comunicação com o banco de dados
├── chatbot - Diretório de instalação do Rasa
├── faq - Diretório para scrapping e alimentação do banco de dados com FAQs
```

### Banco de dados

```
├── TFAQ - Armazena FAQs extraídos do site da Fiocruz
├── TCategory - Armazena categoria dos FAQs
├── TUnrecognizedMessage - Armazena mensagens não reconhecidas pelo chatbot
```

# Diagramas

## Documentação C4 [![Lucidchart](https://img.shields.io/badge/↗-Lucidchart-f96b13.svg)](https://lucid.app/lucidchart/invitations/accept/inv_a4b4c484-ea60-4957-89d0-65f57f8f70cb?viewport_loc=-49%2C-59%2C2452%2C1140%2C0_0)

![Contexto da aplicação](https://i.imgur.com/KBTUrnk.png)

# Responsável

- Vinícius Souza <<vinicius.fernando.souza@gmail.com>>
