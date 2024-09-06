# Como Usar o Programa

## 1. Instalar o PyInstaller

Se você ainda não tem o PyInstaller instalado, pode instalá-lo via pip:

```sh
pip install pyinstaller
```

## 2. Organizar o Projeto

Certifique-se de que seu script Python (o que você escreveu anteriormente) esteja salvo em um arquivo, por exemplo, `crud_funcionarios.py`.

## 3. Usar o PyInstaller para Criar o Executável

No terminal (ou prompt de comando), navegue até o diretório onde está o arquivo `crud_funcionarios.py` e execute o seguinte comando:

```sh
pyinstaller --onefile --name=CrudFuncionarios crud_funcionarios.py
```

## 4. Estrutura do Comando

- `--onefile`: Faz com que o PyInstaller crie um único arquivo executável `.exe`.
- `--name=CrudFuncionarios`: Define o nome do executável como `CrudFuncionarios.exe`.
- `crud_funcionarios.py`: O nome do script Python que estamos convertendo para `.exe`.

## 5. Encontrar o Executável

Após a execução do comando, o PyInstaller criará uma pasta chamada `dist`. Dentro dessa pasta, você encontrará o arquivo `CrudFuncionarios.exe`.

## 6. Executar o Arquivo `.exe`

Agora, você pode executar o `CrudFuncionarios.exe` em qualquer computador com Windows sem a necessidade de ter o Python instalado.

