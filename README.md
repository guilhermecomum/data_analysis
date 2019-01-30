# Data analysis
Sistema para analise de arquivos .dat

## Desenvolvimento

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

## Execução

1. Clone o repositório.
2. Crie um virtualenv with `Python 3.7`
3. Active o virtualenv
4. Instale as dependências
5. Os dados que deseja analizar deve estar em: `$HOME/data/in`
6. Caso não tenha crie um diretório para os relatórios: `$HOME/data/out`
5. Execute as analises

```console
git clone git@github.com:guilhermecomum/data_analysis.git
cd data_analysis
python -m venv .data_analysis
source .data_analysis/bin/activate
pip install -r requirements.txt
mkdir -p $HOME/data/in
mkdir -p $HOME/data/out
python data_analysis.py
```

Os relatórios estão disponíveis em: `$HOME/data/out`

## Considerações
* Os dados fornecidos não tem informações duplicadas
* Os diretórios `$HOME/data/in` `$HOME/data/out` estão criados
