import json
from aluno import Aluno

# Criando um aluno
aluno = Aluno(
    nome="Maria Oliveira",
    dataNascimento="20/05/1998",
    telefone="(48) 98888-8888",
    curso="Ciência da Computação"
)

# Adicionando disciplinas
aluno.adicionarDisciplina("Algoritmos")
aluno.adicionarDisciplina("Banco de Dados", "Aprovado")

# Alterando a situação de uma disciplina
aluno.alterarSituacaoDisciplina("Algoritmos", "Cancelado")

# Obtendo informações do aluno
print("Saída atual:")
print(json.dumps(aluno.obterInformacoes(), indent=4, ensure_ascii=False))

# Saída Esperada
print("""Saída esperada:
{
    'nome': 'Maria Oliveira',
    'dataNascimento': '20/05/1998',
    'idade': 26,
    'telefone': '(48) 98888-8888',
    'curso': 'Ciência da Computação',
    'disciplinas': {
        'Algoritmos': 'Cancelado',
        'Banco de Dados': 'Aprovado'
    }
}
""")