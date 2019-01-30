# Data analysis
Sistema para analise de arquivos .dat

## Development

1. Clone o repositório.
2. Crie um virtualenv with `Python 3.7`
3. Active o virtualenv
4. Instale as dependências
6. Execute os testes

```console
git clone git@github.com:guilhermecomum/data_analysis.git
cd data_analysis
python -m venv .data_analysis
source .data_analysis/bin/activate
pip install -r requirements.txt
python tests.py
```

## Considerações
* Os dados fornecidos não tem informações duplicadas
* Os diretórios `$HOME/data/in` `$HOME/data/out` estão criados
