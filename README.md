# Лабораторная работа 1

## Лабораторная работа 1

### Задание 1
```python
ime=input('Имя: ')
vozrast=int(input('Возраст: '))
print(f'Привет, {ime}! Через год тебе будет {vozrast+1}.')
```
![Картинка 1](images/lab01/1.png)

### Задание 2
```python
a=(input('Число a: ')).replace(',','.')
b=(input('Число b: ')).replace(',','.')
sum=round((float(a)+float(b)),2)
avg=round((float(a)+float(b))/2,2)
print(f'Сумма = {sum} ; Среднее арифметическое = {avg}')
```
![Картинка 2](images/lab01/2.png)


### Задание 3
```python
price = float(input('Введите цену: '))
disc = float(input('Введите скидку: '))
vat = float(input('Введите НДС: '))
base = price * (1 - disc / 100)
vat_amount =base * (vat / 100)
total = base + vat_amount
print(f'База после скидки:{base:.2f} Р')
print(f'НДС:{vat_amount:.2f} Р')
print(f'Итого к оплате:{total:.2f} Р')
```
![Картинка 3](images/lab01/3.png)

### Задание 4
```python
vrema=int(input('Введите кол-во минут '))
chas=vrema//60
print(f' Результат перевода: {chas}:{vrema-(chas*60)}')
```
![Картинка 4](images/lab01/4.png)

### Задание 5
```python
fio=input('ФИО: ')
inic=''
dl=0
x=fio.split()
for i in range(0,len(x)):
    inic=inic+x[i][0]+'.'
    dl=len(x[i])+dl
print(f'Инициалы: {inic[:-1]}')
print(f'Длина (символов): {dl+2}')
```
![Картинка 5](images/lab01/5.png)
