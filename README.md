
# Portfólio Leonardo Wallace - Automação de Geração

Este projeto é uma ferramenta de automação em Python desenvolvida para gerenciar e gerar o portfólio profissional de Leonardo Wallace. Segue os padrões corporativos de organização de projetos.

## Estrutura do Projeto

```
portfolio_leonardo_wallace/
│
├── main.py                # Ponto de entrada (Build)
├── config/
│   └── settings.py       # Dados do portfólio (Bio, Projetos, Experiências)
│
├── data/
│   ├── input/            # Arquivos de entrada (Imagens, PDFs)
│   ├── output/           # Site gerado (index.html, index.css)
│   └── backup/           # Backups de builds anteriores
│
├── src/
│   ├── processor.py      # Lógica de geração de UI/UX
│   ├── exporter.py       # Manipulação de arquivos e backups
│   └── utils.py          # Funções auxiliares
│
├── logs/
│   └── app.log           # Rastreabilidade de execução
│
├── requirements.txt
└── README.md
```

## Como Executar

Para atualizar o site:
1. Edite os dados em `config/settings.py`.
2. Execute o script principal:
   ```bash
   python main.py
   ```
3. Os arquivos prontos para hospedagem estarão em `data/output/`.

## Tecnologias Utilizadas
- **Backend/Automação**: Python (Standard Lib)
- **Frontend**: HTML5, CSS3 (Modern Glassmorphism Design)
- **Hospedagem**: Netlify
