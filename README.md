# Projeto de Software — 2026.2

Material de estudo de **Projeto de Software e Gestão Ágil**, organizado como um
site MkDocs Material e inspirado na estrutura do repositório
[Insper/ML](https://github.com/insper/ML).

Site publicado: <https://djairofilho.github.io/projsoft-2026-2/>

## Desenvolvimento local

```bash
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
mkdocs serve
```

No Linux ou macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

## Importar novas aulas

Baixe os PDFs do Blackboard para um diretório local que não esteja dentro do
repositório e execute:

```bash
python scripts/import_aulas.py --source CAMINHO_DOS_PDFS
```

O importador:

- calcula o SHA-256 de cada PDF;
- ignora arquivos já registrados;
- copia somente materiais novos;
- atualiza `data/aulas.yml`;
- cria uma página inicial sem sobrescrever notas existentes.

Revise a página criada, altere `published` para `true` no manifesto e inclua a
aula na navegação de `mkdocs.yml` antes de publicar.

## Validação

```bash
python -m unittest discover -s tests -v
mkdocs build --strict
```

## Segurança e direitos autorais

Nunca adicione chaves `.pem`, endereços de máquinas, senhas, tokens ou arquivos
de inventário da infraestrutura. Os PDFs originais permanecem sob os direitos de
seus autores e da instituição; este repositório não concede uma licença aberta
sobre esses arquivos.
