from operator import methodcaller,attrgetter


class Student:
    def __init__(self, F, I, O, russian, math, physics, check_att):
        self.F = F
        self.I = I
        self.O = O
        self.russian = russian
        self.math = math
        self.physics = physics
        self.check_att = check_att

    def __repr__(self):
        return repr([self.F, self.I, self.O, self.russian, self.math, self.physics, self.check_att])

    def summ_grade(self):
        return self.russian + self.math + self.physics


def readfile():
    print('Введите название файла:', end=' ')
    inpt = str(input())
    file = open(inpt, encoding="utf-8")
    N = file.readline()
    lines = file.readlines()[0:]
    list_new = []
    for st in lines:
        F = st.split()[0]
        I = st.split()[1]
        O = st.split()[2]
        russian = int(st.split()[3])
        math = int(st.split()[4])
        physics = int(st.split()[5])
        check_att = st.split()[6].lower().title()
        list = (Student(F, I, O, russian, math, physics, check_att))
        list_new.append(list)
    return list_new, N

def entrance(list_new, N):
    list_middle = sorted(list_new, key=attrgetter('math', 'physics'), reverse=True)
    #list_middle = sorted(list_new, key=lambda student: (student.physics), reverse=True)
    #list_middle = sorted(list_middle, key=lambda student: student.math, reverse=True)
    list_middle = sorted(list_middle, key=methodcaller('summ_grade'), reverse=True)
    list_end = sorted(list_middle, key=lambda student: student.check_att, reverse=False)  # print('Нет'>'Да')
    list_end = list_end[:int(N)]
    return list_end

def save_answer(list,list_new):
    fout = open('answer.txt', 'w')
    print("Абитуриенты, которые подали заявление:", end='\n\n', file=fout)
    print(*list,sep="\n",file=fout)
    print("\n\nПоступившие абитуриенты:", end='\n\n', file=fout)
    print(*list_new,sep="\n",file=fout)
    fout.close()

list, N = readfile()
list_new = entrance(list, N)
save_answer(list, list_new)

#test1.txt