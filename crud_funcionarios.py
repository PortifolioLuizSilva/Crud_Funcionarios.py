import sqlite3
import hashlib
from datetime import datetime

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('funcionarios.db')
cursor = conn.cursor()

# Criar a tabela de funcionários
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    data_cadastro TEXT NOT NULL
)
''')

def gerar_id(nome):
    """Gera um ID único baseado no hash MD5 do nome e do tempo atual."""
    tempo_agora = datetime.now().isoformat()
    id_unico = hashlib.md5(f'{nome}{tempo_agora}'.encode()).hexdigest()
    return id_unico

def cadastrar_funcionario(nome):
    """Cadastra um novo funcionário com um ID único e a data/hora atual."""
    id_funcionario = gerar_id(nome)
    data_cadastro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
    INSERT INTO funcionarios (id, nome, data_cadastro)
    VALUES (?, ?, ?)
    ''', (id_funcionario, nome, data_cadastro))
    conn.commit()
    print(f'Funcionário {nome} cadastrado com sucesso!')

def listar_funcionarios():
    """Lista todos os funcionários cadastrados."""
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()
    for func in funcionarios:
        print(f'ID: {func[0]}, Nome: {func[1]}, Data de Cadastro: {func[2]}')

def atualizar_funcionario(id_funcionario, novo_nome):
    """Atualiza o nome de um funcionário pelo ID."""
    cursor.execute('''
    UPDATE funcionarios
    SET nome = ?
    WHERE id = ?
    ''', (novo_nome, id_funcionario))
    conn.commit()
    print(f'Funcionário ID {id_funcionario} atualizado para {novo_nome}.')

def deletar_funcionario(id_funcionario):
    """Deleta um funcionário pelo ID."""
    cursor.execute('DELETE FROM funcionarios WHERE id = ?', (id_funcionario,))
    conn.commit()
    print(f'Funcionário ID {id_funcionario} deletado com sucesso!')

# Exemplos de uso
cadastrar_funcionario('João Silva')
cadastrar_funcionario('Maria Oliveira')
listar_funcionarios()

# Atualizar o nome do funcionário
atualizar_funcionario('insira_id_aqui', 'João Santos')

# Deletar o funcionário
deletar_funcionario('insira_id_aqui')

# Listar novamente para verificar as alterações
listar_funcionarios()

# Fechar a conexão com o banco de dados
conn.close()
