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

class Calculadora_CR(object):
    def cr_aluno(self,linhas,lista_alunos):
        for linha in linhas:
            linha = linha.split(',')
            if linha[0] in lista_alunos:
                lista_alunos[linha[0]].processar_dados(linha[3],linha[4])
            else:
                lista_alunos[linha[0]] = Aluno()
                lista_alunos[linha[0]].processar_dados(linha[3],linha[4])
    
    def mostrar_cr(self,lista_alunos):
        print("------- O CR dos alunos é: --------")
        for i in lista_alunos:
            print(f"Matricula:{i}  CR:{lista_alunos[i].cr}")

def ler_csv():
    arquivo = open("notas.csv","r")
    linhas = arquivo.readlines()
    linhas.pop(0)
    arquivo.close()
    return linhas

    

def main():
    linhas = ler_csv()
    lista_alunos={}

    calculadora_cr = Calculadora_CR()
    calculadora_cr.cr_aluno(linhas,lista_alunos)
    calculadora_cr.mostrar_cr(lista_alunos)

main()
