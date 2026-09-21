from nome import nome


def cadastrar_aluno(alunos):
idade = input("Digite a idade do aluno: ")
curso = input("Digite o curso do aluno: ")
aluno = {"nome": nome, "idade": idade, "curso": curso}
alunos.append(aluno)
print("Aluno cadastrado com sucesso!")