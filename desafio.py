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

class Curso(object):
    def __init__(self):
        self.lista_alunos={}
        self.cr = 0
        

    def cr_curso(self):
        soma_cr = 0
        for key in self.lista_alunos:
            soma_cr += self.lista_alunos[key].cr
        
        self.cr = soma_cr/len(self.lista_alunos)

class Calculadora_CR(object):
    def ler_csv(self):
        arquivo = open("notas.csv","r")
        linhas = arquivo.readlines()
        linhas.pop(0)
        arquivo.close()
        return linhas

    def cr_aluno(self,linhas,lista_alunos):
        for linha in linhas:
            linha = linha.split(',')
            if linha[0] in lista_alunos:
                lista_alunos[linha[0]].processar_dados(linha[3],linha[4])
            else:
                lista_alunos[linha[0]] = Aluno()
                lista_alunos[linha[0]].processar_dados(linha[3],linha[4])
    
    def mostrar_cr_alunos(self,lista_alunos):
        print("------- O CR dos alunos é: --------")
        for i in lista_alunos:
            print(f"Matricula:{i}  CR:{lista_alunos[i].cr}")
        print("-----------------------------------")
    
    def cr_por_curso(self,linhas,lista_de_cursos):
        for linha in linhas:
            linha = linha.split(',')
            matricula = linha[0]
    
            if linha[2] not in lista_de_cursos:
                lista_de_cursos[linha[2]] = Curso()
                lista_de_cursos[linha[2]].lista_alunos[matricula] = Aluno()
            
            if matricula not in lista_de_cursos[linha[2]].lista_alunos:
                lista_de_cursos[linha[2]].lista_alunos[matricula] = Aluno()

            lista_de_cursos[linha[2]].lista_alunos[matricula].processar_dados(linha[3],linha[4])
            lista_de_cursos[linha[2]].cr_curso()

    def mostrar_media_cr_cursos(self,lista_de_cursos):
        print("----- Média de CR dos cursos ------")
        for curso in lista_de_cursos:
            
            print(f"Curso:{curso}  Média do CR:{lista_de_cursos[curso].cr}")

def main():
    lista_alunos={}
    lista_de_cursos = {}

    calculadora_cr = Calculadora_CR()
    linhas = calculadora_cr.ler_csv()

    calculadora_cr.cr_aluno(linhas,lista_alunos)
    calculadora_cr.mostrar_cr_alunos(lista_alunos)

    calculadora_cr.cr_por_curso(linhas,lista_de_cursos)
    calculadora_cr.mostrar_media_cr_cursos(lista_de_cursos)

main()

