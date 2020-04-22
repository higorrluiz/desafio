class Curso(object):
    def __init__(self):
        self.lista_alunos={}
        self.num_alunos = 0

    def calcular_cr(self): #vai em cada objeto aluno pega o cr deles e soma todos, depois divide pelo numero de alunos
        soma_cr = 0
        self.num_alunos = len(self.lista_alunos)
        for i in self.lista_alunos:
            soma_cr += self.lista_alunos[i].cr
            
        cr = soma_cr/self.num_alunos
        return cr
        
class Aluno(object):
    def __init__(self):
        self.cr=0
        self.tCargaHoraria=0
        self.nota = 0
        self.ch = 0
        self.operacao = 0
       

    def processar_dados(self,nota,ch):
        self.nota = int(nota)
        self.ch = int(ch)

        self.tCargaHoraria += self.ch
        self.operacao += self.nota * self.ch
                
        self.cr = self.operacao/self.tCargaHoraria


def main():
    arquivo = open("notas.csv","r")
    arquivo.readline()
    linha = arquivo.readline().split(',')

    dic_cursos = {}
    geral_alunos = {}

    while linha[0] != '': 
        curso = linha[2]
        matricula = linha[0]
        nota = linha[3]
        ch = linha[4] 
        if curso in dic_cursos and matricula in dic_cursos[curso].lista_alunos and matricula in geral_alunos:
            aluno_curso = dic_cursos[curso].lista_alunos[matricula]
            aluno_curso.processar_dados(nota,ch)
            geral_alunos[matricula].processar_dados(aluno_curso.cr,aluno_curso.tCargaHoraria)
        
        elif curso in dic_cursos and matricula not in dic_cursos[curso].lista_alunos and matricula in geral_alunos:
            dic_cursos[curso].lista_alunos[matricula] = Aluno() #adicionar matricula in dic_alunos
            
            aluno_curso = dic_cursos[curso].lista_alunos[matricula]
            aluno_curso.processar_dados(nota,ch)
            geral_alunos[matricula].processar_dados(aluno_curso.cr,aluno_curso.tCargaHoraria)
            
        
        elif curso in dic_cursos and matricula not in dic_cursos[curso].lista_alunos and matricula not in geral_alunos:
            dic_cursos[curso].lista_alunos[matricula] = Aluno()#adicionar matricula in dic_alunos
            geral_alunos[matricula] = Aluno() #matricula in geral_alunos

            aluno_curso = dic_cursos[curso].lista_alunos[matricula]
            aluno_curso.processar_dados(nota,ch)
            geral_alunos[matricula].processar_dados(aluno_curso.cr,aluno_curso.tCargaHoraria)

        elif curso not in dic_cursos and matricula in geral_alunos:
            dic_cursos[curso] = Curso() #adicionar curso in dic_cursos
            dic_cursos[curso].lista_alunos[matricula] = Aluno()#adicionar matricula in dic_alunos

            aluno_curso = dic_cursos[curso].lista_alunos[matricula]
            aluno_curso.processar_dados(nota,ch)
            geral_alunos[matricula].processar_dados(aluno_curso.cr,aluno_curso.tCargaHoraria)

        elif curso not in dic_cursos and matricula not in geral_alunos:
            dic_cursos[curso] = Curso() #adicionar curso in dic_cursos
            dic_cursos[curso].lista_alunos[matricula] = Aluno() #adicionar matricula in dic_alunos
            geral_alunos[matricula] = Aluno() #matricula in geral_alunos

            aluno_curso = dic_cursos[curso].lista_alunos[matricula]
            aluno_curso.processar_dados(nota,ch)
            geral_alunos[matricula].processar_dados(aluno_curso.cr,aluno_curso.tCargaHoraria)


        linha = arquivo.readline().split(',')
       
    arquivo.close()

    print("------- O CR dos alunos é: --------")
    for i in geral_alunos:
        print(f"Matricula:{i}  CR:{geral_alunos[i].cr}")
    print("-----------------------------------")

    print("----- Média de CR dos cursos ------")
    for i in dic_cursos:
        cr = dic_cursos[i].calcular_cr()
        print(f"Curso:{i}  CR:{cr}")
    print("-----------------------------------")

main()
