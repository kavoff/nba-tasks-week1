import keyword

##### 1 >

data = [1, 5, 16, 184, 93, 104]
g = sorted(data)
f = sorted(data, reverse=True)

##### 2 >

z = [1, 4, 5, 7, 23, 36, 67, 78, 99, 134, 142, 150]
v = [3, 5, 6, 19, 67, 77, 123, 134, 172, 323, 434]
def c(z,v):
    return [x for x in z if x in v]
print(c(z,v))

##### 3 >

a = float(15)
b = float(14)
def summa(a,b):
    g = a + b
print(g)

##### 4 >

def checktype(dannye):
    if dannye.isdigit() == True:
        print('число')
    else:
        print('строка')
checktype('24')

##### 5 >

a = int(4)
if (a % 2) == 0:
    print('Четные есть')
else:
    print('Четных нет')

###### 6 >

age = 17
def sell_alcohol(age):
    if age < 21:
        return('Мы не продаем алкоголь несовершеннолетним')
    else:
        return
print (sell_alcohol(age))

###### 7 >

print(', '.join(keyword.kwlist))

def keylist(phrase):
    print(keyword.iskeyword(phrase))
keylist('def')

##### 8 >

def symbol(x,y):
    print(x.count(y))
symbol('aezakmi','a')