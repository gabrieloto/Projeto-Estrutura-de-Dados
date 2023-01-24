import gc


nan = float('NaN')
mult = 80
class discipli:
    def __init__(self, nome):
        self.back = None
        self.nome = nome
        self.notas = dict()
        self.next = None
    def add_estudante(self, estudante):
        self.notas[estudante.nome] = [0, 0]
        estudante.disciplinas.append(self)
class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = list()


    def add_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


    def remove_disciplina(self, disciplina):
        pass    
class DisciplinaList:
    def __init__(self):
        self.head = None


    def insert(self, nome):
        new_node = discipli(nome)      
        new_node.next = self.head
        new_node.back = None
        if self.head is not None:
            self.head.back = new_node
        self.head = new_node
    def insertStudent(self, disciplina, estudante):
        aux = self.head
        while (aux.nome != disciplina and aux != None):
            aux = aux.next


        if (aux == None):
            return -1
        aux.notas[estudante.nome] = [0, 0]
        estudante.disciplinas.append(disciplina)      
    def insertGrades(self):
        pass
    def selfPrint(self, data):
        print()
        aux = self.head
        counter = 0
        while aux != None:
            counter += 1
            if (data == 22):
                print(counter, " - ",aux.data,sep="")
            else:
                print(counter, " - ",aux.data[data],sep="")
            aux = aux.next
    def removeStudent(self):
        self.selfPrint(0)
        position = int(input("coloque o numero  do aluno que quer remover: ")) - 1
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("\nNúmero inválido.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
    def removeSubject(self):
        aux = self.head
        self.selfPrint(0)
        position = int(input("Digite o número do aluno que deseja remover a matéria: ")) - 1
        for i in range(position):
            aux = aux.next
        for i in range(len(aux.data[1])):
            print(i+1, "-", aux.data[1][i][0])
        self.selfPrint(1)
        position = int(input("Digite o número de matéria que deseja remover: ")) - 1
        aux.data[1].pop(position)    
    def modifyGrades(self):
        flag = False
        aux = self.head
        while aux  != None:
            print("\n", aux.data[0])
            if (aux.data[1] != None):
                aux.data[1] = int(input("coloque a 1º nota: "))
                flag = True
            if (aux.data[2] != None):
                aux.data[2] = int(input("coloque a 2º nota: "))
                flag = True
            aux = aux.next
        if (flag):
            print("Notas modificadas!")
        else:
            print("Não há cadeiras que precisam modificar notas!")
    def listaDisciplinas(self):
        aux = self.head
        if (aux == None): return None
        l = []
        while (aux != None):
            l.append(aux)
            aux = aux.next
        return l
def escolhe_d():
    global materias
    l = materias.listaDisciplinas()
    if (len(l) == 0):
        print('Não há matérias.')
        return None    
    for i, d in enumerate(l):
        print(f'[{i}] - {d.nome}')
    print('-'*mult)
    while (True):
        try:
            c = int(input('Escolha: '))
        except:
            return None
        if (0 <= c < len(l)):
            break        
    return l[c]
option = 0
materias = DisciplinaList()
estudantes = list()
print('-'*mult)
print("Bem vindo ao sistemade da UEPB")
print('-'*mult)
while (True):
    print("[1] Add disciplina\n[2] Ver disciplina\n[3] Cadastrar estudante\n[4] Cadastrar estudante em disciplina\n[5] Editar ou adicionar notas dos alunos\n[6] remover aluno\n[7] Remover disciplina de aluno\n[8] Nota de cada aluno\n[9] parametros \n[10] exit")
    print('-'*mult)
    while (True):
        try:
            option = int(input("Opção: "))
        except:
            continue


        if (1 <= option <= 10):
            break
    print('-'*mult)    
    if (option == 1):
        nome = input('nome da disciplina: ')
        materias.insert(nome)
    elif (option == 2):
        d = escolhe_d()
        if (d == None): continue
        print('-'*mult)
        print('{:^30}{:^10}{:^10}{:^10}'.format('Nome', 'Nota 1', 'Nota 2', 'Média'))
        print('-'*mult)
        for e in d.notas.keys():
            print('{:^30}{:^10.2f}{:^10.2f}{:^10}'.format(e, d.notas[e][0], d.notas[e][1], (d.notas[e][0] + d.notas[e][1])/2))
    elif (option == 3):
        while (True):
            nome = input('estudante [não digite mais nada e aperte enter para para ]: ')
            if (nome == ''): break
            estudantes.append(Estudante(nome))
    elif (option == 4):
        d = escolhe_d()
        if (d == None):
            continue            
        print('-'*mult)
        for e in estudantes:
            if (d not in e.disciplinas):
                c = input(f'Adicionar {e.nome} em {d.nome}? [s/n] ')
                if (c == 's'):
                    d.add_estudante(e)
    elif (option == 5):
        for e in estudantes:
            opc = input(f'Editar notas do aluno {e.nome}? [s/n] ')
            if (opc == 's'):
                print('-'*mult)
                for d in e.disciplinas:
                    opc = input(f'Editar notas em {d.nome}? [s/n] ')
                    if (opc == 's'):
                        for i in range(2):
                            try:
                                n = int(input(f'{i+1}ª nota: [enter para pular] '))
                                d.notas[e.nome][i] = n
                            except:
                                continue
                        print('-'*mult)                        
    elif (option == 6):
        for i, e in enumerate(estudantes):
            print(f'{i} - {e.nome}')
        while (True):
            i = input('Aluno para remover [x para cancelar]: ')
            if (i == 'x'):
                break
            try:
                opc = int(i)
            except:
                continue


            if (0 <= opc < len(estudantes)):
                break
        if (i == 'x'): continue
        for d in estudantes[opc].disciplinas:
            d.notas.pop(estudantes[opc].nome)
        estudantes.pop(opc)
    elif (option == 7):
        for i, e in enumerate(estudantes):
            print(f'{i} - {e.nome}')
        while (True):
            i = input('remove aluno [x para cancelar]: ')
            if (i == 'x'):
                break
            try:
                opc = int(i)
            except:
                continue
            if (0 <= opc < len(estudantes)):
                break
        if (i == 'x'): continue


        for j, d in enumerate(estudantes[opc].disciplinas):
            o = input(f'Remover o estudante de {d.nome}? [s/n] ')
            if (o == 's'):
                d.notas.pop(estudantes[opc].nome)
                estudantes[opc].disciplinas.pop(j)
    elif (option == 8):
        for e in estudantes:
            opc = input(f'Ver notas do aluno {e.nome}? [s/n] ')
            if (opc == 's'):
                print('-'*mult)
                for d in e.disciplinas:
                    print(f'{d.nome}: Nota1={d.notas[e.nome][0]} Nota2={d.notas[e.nome][1]} Média={(d.notas[e.nome][0] + d.notas[e.nome][1])/2}')
                print('-'*mult)
    elif (option == 9):
        d = escolhe_d()
        if (d == None):
            continue
        print('-'*mult)
        print('Ver alunos com média\n[1] maior ou igual a 7.\n[2] menor que 7.')
        print('-'*mult)
        while (True):
            try:
                opc = int(input('Escolha: '))
            except:
                continue
            if (0 < opc <= 2): break


        print('-'*mult)
        if (opc == 1):
            for k in d.notas.keys():
                media = (d.notas[k][0] + d.notas[k][1]) / 2
                if (media >= 7):
                    print(k)
        else:
            for k in d.notas.keys():
                media = (d.notas[k][0] + d.notas[k][1]) / 2
                if (media < 7):
                    print(k)
        print('-'*mult)
       
    elif (option == 10):
        break
