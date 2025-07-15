# KML Generator

Scripts em Python para gerar arquivos `.kml` com pontos (sites) e links (enlaces) a partir de planilhas Excel. Ideal para visualização em ferramentas como Google Earth.

## 📁 Estrutura

```
kml-generator/
├── data/
│ ├── template_sites.xlsx # Planilha de exemplo com dados de sites
│ └── template_links.xlsx # Planilha de exemplo com dados de enlaces
│
├── output/
│ ├── points.kml # Saída gerada com os pontos
│ └── links.kml # Saída gerada com os enlaces
│
├── points.py # Script para gerar pontos (sites)
├── links.py # Script para gerar enlaces (links)
├── requirements.txt # Dependências do projeto
└── README.md # Instruções e informações do projeto
```

## 🐍 Requisitos

- Python 3.8+
- Instalar as dependências:

```
pip install -r requirements.txt
```

▶️ Como usar

Gerar pontos (sites):
```
python points.py
```
Isso irá ler o arquivo data/template_sites.xlsx e gerar output/points.kml.

Gerar enlaces (links):
```
python links.py
```
Isso irá ler data/template_links.xlsx e gerar output/links.kml.


📌 Observações

- Os arquivos .kml podem ser abertos diretamente no Google Earth.
- As planilhas .xlsx devem conter as colunas esperadas pelo script (veja os exemplos em data/).
- Se necessário, edite os caminhos de entrada/saída diretamente nos scripts points.py e links.py.


📄 Licença
Este projeto está licenciado sob os termos da licença MIT.
