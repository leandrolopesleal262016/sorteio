# Aplicação de Sorteio Web

Uma aplicação web para realizar sorteios de forma interativa, com suporte a áudio e feedback por voz.
Pode ser acessada em https://wise360.org/sorteio/
## Estrutura do Projeto

```
sorteio-webapp/
├── app.py
├── static/
│   ├── audio/
│   │   └── furem_os_tambores.mp3
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── requirements.txt
├── .gitignore
└── README.md
```

## Requisitos

- Python 3.6 ou superior
- Flask
- pyttsx3

## Instalação

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Adicione o arquivo de áudio:
- Coloque `furem_os_tambores.mp3` na pasta `static/audio/`

## Executando

1. Execute o servidor:
```bash
python app.py
```

2. Acesse no navegador:
```
http://localhost:5000
```

## Funcionalidades

- Adição de nomes à lista
- Sorteios sem repetição
- Feedback por voz com controles de velocidade e tom
- Som de tambores durante o sorteio
- Interface responsiva
- Histórico de ganhadores
- Reinício da aplicação

## Gerando Executável

```bash
pyinstaller sorteio.spec
```

O executável será gerado na pasta `dist/`.

## Licença

MIT License
