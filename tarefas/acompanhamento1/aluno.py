from datetime import datetime

class Aluno:
    # Situações possíveis para disciplinas
    SITUACOES_VALIDAS = ["Matriculado", "Cancelado", "Aprovado", "Reprovado"]

    def __init__(self, nome, dataNascimento, telefone, curso, disciplinas=None):
        """
        Inicializa um objeto Aluno.

        :param nome: Nome do aluno.
        :param dataNascimento: Data de nascimento no formato DD/MM/AAAA.
        :param telefone: Telefone do aluno.
        :param curso: Curso do aluno.
        :param disciplinas: Dicionário com disciplinas e suas situações.
        """
        self.nome = nome
        self.dataNascimento = self._validar_data(dataNascimento)
        self.telefone = telefone
        self.curso = curso
        self.disciplinas = disciplinas if disciplinas else {}

    def _validar_data(self, data):
        """
        Valida e converte a data de nascimento para o formato DD/MM/AAAA.

        :param data: Data de nascimento como string.
        :return: A data validada.
        :raises ValueError: Se o formato da data for inválido.
        """
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato DD/MM/AAAA.")

    def calcularIdade(self):
        """
        Calcula a idade do aluno com base na data atual.

        :return: Idade do aluno como inteiro.
        """
        data_atual = datetime.now()
        data_nascimento = datetime.strptime(self.dataNascimento, "%d/%m/%Y")
        idade = data_atual.year - data_nascimento.year
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        return idade

    def adicionarDisciplina(self, nome_disciplina, situacao="Matriculado"):
        """
        Adiciona uma disciplina ao aluno.

        :param nome_disciplina: Nome da disciplina.
        :param situacao: Situação inicial da disciplina (padrão: "Matriculado").
        :raises ValueError: Se a situação for inválida.
        """
        if situacao not in self.SITUACOES_VALIDAS:
            raise ValueError(f"Situação inválida: {situacao}. Situações válidas: {self.SITUACOES_VALIDAS}")
        self.disciplinas[nome_disciplina] = situacao

    def alterarSituacaoDisciplina(self, nome_disciplina, nova_situacao):
        """
        Altera a situação de uma disciplina.

        :param nome_disciplina: Nome da disciplina.
        :param nova_situacao: Nova situação da disciplina.
        :raises KeyError: Se a disciplina não estiver cadastrada.
        :raises ValueError: Se a nova situação for inválida.
        """
        if nome_disciplina not in self.disciplinas:
            raise KeyError(f"A disciplina '{nome_disciplina}' não está cadastrada.")
        if nova_situacao not in self.SITUACOES_VALIDAS:
            raise ValueError(f"Situação inválida: {nova_situacao}. Situações válidas: {self.SITUACOES_VALIDAS}")
        self.disciplinas[nome_disciplina] = nova_situacao

    def obterInformacoes(self):
        """
        Retorna todas as informações do aluno.

        :return: Dicionário com as informações do aluno.
        """
        return {
            "nome": self.nome,
            "dataNascimento": self.dataNascimento,
            "idade": self.calcularIdade(),
            "telefone": self.telefone,
            "curso": self.curso,
            "disciplinas": self.disciplinas
        }