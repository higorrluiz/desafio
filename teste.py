from desafio import Aluno,Curso

def teste_cr1(): #mesma carga horaria
    aluno=Aluno()
    aluno.processar_dados(5,30)
    aluno.processar_dados(8,30)
    assert aluno.cr == 6.5

def teste_cr2(): #mesma nota
    aluno=Aluno()
    aluno.processar_dados(5,30)
    aluno.processar_dados(5,80)
    assert aluno.cr == 5

def teste_cr3(): #apenas uma disciplina
    aluno = Aluno()
    aluno.processar_dados(5,30)
    assert aluno.cr == 5

def teste_cr4(): #diversas notas e carga horarias diferentes
    aluno = Aluno()
    aluno.processar_dados(80,60)
    aluno.processar_dados(0,70)
    aluno.processar_dados(93,50)
    aluno.processar_dados(77,30)
    assert aluno.cr == 56

def teste_cr5(): # notas e carga horarias iguais
    aluno = Aluno()
    aluno.processar_dados(80,60)
    aluno.processar_dados(80,60)
    aluno.processar_dados(80,60)
    aluno.processar_dados(80,60)
    assert aluno.cr == 80


def teste_media_cr1(): #todos os alunos com o mesmo cr
    curso = Curso()
    curso.lista_alunos={1:Aluno(), 2: Aluno(), 3:Aluno()}
    curso.lista_alunos[1].processar_dados(5,6)
    curso.lista_alunos[2].processar_dados(5,6)
    curso.lista_alunos[3].processar_dados(5,6)
    curso.cr_curso()
    assert curso.cr == 5

def teste_media_cr2(): #todos os alunos com cr diferentes
    curso = Curso()
    curso.lista_alunos={1:Aluno(), 2: Aluno(), 3:Aluno()}
    curso.lista_alunos[1].processar_dados(5,6)
    curso.lista_alunos[2].processar_dados(3,6)
    curso.lista_alunos[3].processar_dados(10,6)
    curso.cr_curso()
    assert curso.cr == 6

def teste_media_cr3(): #apenas 1 aluno
    curso = Curso()
    curso.lista_alunos={1:Aluno()}
    curso.lista_alunos[1].processar_dados(5,6)
    curso.cr_curso()
    assert curso.cr == 5
