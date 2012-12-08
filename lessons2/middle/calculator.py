# coding: utf-8
from sets import Set

#словарь операторов
operators = {
    '+' : float.__add__,
    '-' : float.__sub__,
    '*' : float.__mul__,
    '/' : float.__div__,
    '^' : float.__pow__,
}

#словарь приоритетов операторов
priority = {
    '(' : 1,
    '+' : 2,
    '-' : 2,
    '*' : 3,
    '/' : 3,
    '^' : 4,
}

def allowed_nums():
    return '0123456789.'

#вывод доступных операторов
def operations():
    print 'Желательно писать все через пробел. Конечно кроме унарных операторов.'
    print 'Доступные вам операторы:'
    print '"+" - сложение\n"-" - вычитание\n"*" - умножение\n"/" - деление\n"^" - возведение в степень' 

#функция проверки введенного выражения на коррктность
def correct_expression(expression):
    allowed_symbols = Set('1234567890-+*/^ ().')
    if Set(expression).issubset(allowed_symbols):
        return True

#функция проверки на правильность скобок
def check_brackets(expression):
    bracketsCount=0
    for symbol in expression:
        if symbol=='(':
            bracketsCount+=1
        elif symbol==')':
            bracketsCount-=1
    if bracketsCount!=0:
        return False
    return True

#функция преобразования выражения по обратной польской нотации
def return_Polish_record(expression):
    isSearch=False
    stack = []
    outstring=''
    iter=0
    for symbol in expression:
        if symbol=='-' or symbol=='+':
            try:
                if expression[iter+1] in allowed_nums():
                    outstring+=symbol
                    iter+=1
                    continue
            except IndexError:
                pass
        if symbol==')':
            i=0
            for elem in stack:
                if elem=='(':
                    pos=i
                i+=1
            if pos<len(stack):
                stack.pop(pos)
            k=len(stack)
            while k>pos:
                outstring+=stack.pop()
                k-=1
            outstring+=') '
        if symbol in allowed_nums():
            try:
                if expression[iter+1] in allowed_nums():
                    outstring+=symbol
                else:
                    outstring+=symbol+' '
            except IndexError:
                outstring+=symbol+' '
        if symbol=='(':
            stack.append(symbol)
            outstring+=' ('
        if symbol in operators.keys():
            if not stack:
                stack.append(symbol)
            else:
                if priority[symbol]>priority[stack[-1]]:
                    stack.append(symbol)
                else:
                    cnt=0
                    for elem in stack:
                        if elem=='(':
                            while cnt<len(stack):
                                if priority[stack[cnt]]>=priority[symbol]:
                                    outstring+=stack.pop(cnt)+' '
                                cnt+=1
                            stack.append(symbol)
                            isSearch=True
                            break
                        cnt+=1
                        if not isSearch:
                            for elem in stack:
                                if priority[elem]>=priority[symbol]:
                                    i=0
                                    while stack[i]!=elem:
                                        i+=1
                                    outstring+=stack.pop(i)+' '
                            stack.append(symbol)
        iter+=1
    for elem in reversed(stack):
        outstring+=elem+' '
    return outstring


#функция вычисления выражения, передаваемого в обратной польской записи
def calculate(expression):
    stack = []; #список для хранения чисел
    number='';  #строка в которую будем записывать число, затем преобразовывать его в int, и очищать эту строку, и так с каждым числом
    iter=0
    if expression=='': #если ниче не ввели то возвращаем что все плохо
        return 'Ошибка при вычислении. Проверьте корректность данного выражения'
    for symbol in expression: #идем по строке в которой выражение
        if symbol=='-' or symbol=='+':       #если символ равен "-" или "+"
            try:              #пробуем посмотреть следующий символ
                if expression[iter+1] in allowed_nums():    #смотрим, если следующий символ после минуса или плюса число
                    number+=symbol                          #то записываем минус или плюс в строку, которая будет числом
                    iter+=1
                    continue                                #переходим к следующему шагу цикла
            except IndexError:      #если не получается посмотреть, значит этот минус или плюс последний символ в строке, а следовательно он не может принадлежать числу, значит он оператор
                pass                #пропускаем и идем дальше
        if symbol in allowed_nums():      #если символ - число
            number+=symbol                #то записываем его в строку, в которой будет формироваться число
            iter+=1
            continue                      #переходим к следующему шагу цикла
        if number!='':                    #если в строке, формирующей число что-то есть
            try:
                num=float(number)             #то преобразуем это число в float
            except:
                return 'Слишком много точек'
            stack.append(num)             #и записываем его в стэк
            number=''                     #строку очищаем
        if not symbol in operators.keys():       #если символ не оператор
            iter+=1
            continue
        try:
            number2=stack.pop()
            number1=stack.pop()
        except IndexError:
            return 'Количество операторов должно быть меньше количества операндов на 1. Возможно вы ввели минус или плюс слитно с числом';
        try:
            result=operators[symbol](number1,number2)
        except ZeroDivisionError:
            return 'Ошибка: деление на 0'
        iter+=1
        stack.append(result);
    if len(stack)!=1:
        return 'Количество операторов должно быть меньше количества операндов на 1. Возможно вы ввели минус слитно с числом';
    res=str(stack.pop())
    return 'Ответ: '+str(res);


operations()
s = raw_input("Введите математическое выражение: ")
if correct_expression(s) and check_brackets(s):
    print(calculate(return_Polish_record(s)))
