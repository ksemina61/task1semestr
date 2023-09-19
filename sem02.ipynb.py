n = int(input()) #task 2
if n % 2 == 0:
  print(n // 4)
elif n % 2 != 0:
  print(n % 4)
  

t = int(input()) #task 3
if - 10 <= t >= -5:
  print(bool(t))
elif 0 < t >15:
  print(bool(t))
  
  
string = input(('')) #task 4?
if string == '':
  print('Вы ввели пустую строку')
elif string == ('Б'):
  print ('в строке есть буква Б ')
elif string != ('Б'):
  print ('в строке нет буквы Б ')


a = float(input('a:')) #задание 5
b = float(input('a:'))
c = float(input('a:'))
D = b**2 - 4 * a * c
if D < 0:
  print('Корней нет')
if D == 0:
  print('t =', -b / (2 * a))
if D > 0:
  print('t =', -b - D**0.5 / (2*a))
  print('t =', -b + D**0.5 / (2*a))
  
  
  
t = int(input()) #задание 7
if t % 3 == 0:
  print(t)
  
t = int(input()) #задание 6
e = int(input())
t1 = int(input())
e1 = int(input())
if t == t1 or e == e1:
  print('Yes')
else:
  print('No')
  
  
a = int(input('a = ')) #задание 8
b = 3
print((a + b) ** 2)


#семинар 2, задача 1 из домашнего задания
n = int(input()) 
a = n // 3600
b = a % 60
a1 = n // 60
c = n % 60
print(a, a1, c, sep = ':')


kg = float(input('введите кг:')) # задача 2 из домашнего задания
kg = float(kg)
pounds = kg * 2.2
print(kg, 'кг - это', pounds)


a = int(input('Дано число:')) # задача 3 из домашнего задания
b = 70
b = (70 * a) / 100
print(b, '%')


x = float(input()) # задача 4 из домашнего задания
print(int(x * 10) % 10)


X = float(input()) #семинар 3, задание 4
print(int(X * 10) % 10)


sentence = input('') #семинар 3, задание 5???
if sentence == sentence [::-1]:
  print(sentence, 'is a palindrome')
else:
  print(sentence, 'is not a palindrome.')
  
  
  # задания из 3-ий домашней работы
  
s = 'hahahahah' #задание 10
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)


s = input() #задание 9
a = s[:s.find('h')]
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)


s = 'salutcava' #задание 3
print(s[: : -1])


s = input() #задание 5
word1 = s[:s.find(' ')]
word2 = s[s.find(' ') + 1:]
print(word2 + ' ' + word1)
