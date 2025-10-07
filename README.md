# Лабораторные работы

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
## Лабораторная работа 2
### Задание 1.1
```python
def min_max(nums:list[float|int])->tuple[float|int, float| int]:
    if len(nums)==0:
         return ValueError
    mi=100000000000000000
    ma=-100000000000000000
    for i in range(0,len(nums)):
        if nums[i]<mi:
            mi=nums[i]
        if nums[i]>ma:
            ma=nums[i]
    return tuple([mi, ma])
print(min_max([1.5, 2, 2.0, -3.1]))
```
![Картинка 1](images/lab02/1.1.png)

### Задание 1.2
```python
def unique_sorted(nums:list[float|int])->list[float|int]:
    return sorted(set(nums))
print(unique_sorted([3,1,2,1,3]))
```
![Картинка 2](images/lab02/1.2 .png)

### Задание 1.3
```python
def flatten(mat:list[list| tuple])->list:
    array=list()
    for arr in mat:
        if not(isinstance(arr,tuple) or isinstance(arr,list)):
            return TypeError
        for member in arr:
            array.append(member)
    return array
print(flatten([[1,2],[3,4]]))
```
![Картинка 3](images/lab02/1.3 .png)

### Задание B.1
```python
def transpose(mat:list[list[float|int]])->list[list]:
    if len(mat)==0:
        return []
    if any(len(mat[0])!=len(mat[i]) for i in range(len(mat))):
        return ValueError
    new=[[0 for j in range(len(mat))] for i in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            new[j][i]=mat[i][j]
    return new
print(transpose([[1,2],[3,4]]))
```
![Картинка 4](images/lab02/B.1 .png)

### Задание B.2
```python
def row_sums(mat:list[list[float|int]])->list[float]:
    if any(len(mat[0]) != len(mat[i]) for i in range(len(mat))):
        return ValueError
    array=list()
    for arr in mat:
        array.append(sum(arr))
    return array
print(row_sums([[1,2,3], [4,5,6]]))
```
![Картинка 5](images/lab02/B.2 .png)

### Задание B.3
```python
ef col_sums(mat:list[list[float|int]])->list[float]:
    if any (len(mat[0])!=len(mat[i]) for i in range (len(mat))):
        return ValueError
    array=list(0 for i in range(len(mat[0])))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            array[j]+=mat[i][j]
    return array
print(col_sums([[1,2,3],[4,5,6]]))
```
![Картинка 6](images/lab02/B.3 .png)

### Задание C
```python
def format_record(rec:tuple[str,str,float]):
    name_data=rec[0].strip().split()
    if len(name_data)>2:
        surname,name,otchestvo=rec[0].strip().split()
        new_name_data=f'{surname[0].upper()}{surname[1:]} {name[0].upper()} {otchestvo[0].upper()}'
    elif len(name_data)==2:
        surname, name = rec[0].strip().split()
        new_name_data = f'{surname[0].upper()}{surname[1:]} {name[0].upper()} '
    elif len(name_data)==1:
        surname,  = rec[0].strip().split()
        new_name_data = f'{surname[0].upper()}{surname[1:]} '
    else:
        return ValueError
    group=rec[1].strip()
    if group=='':
        return ValueError
    try:
        gpa=float(rec[2])
    except Exception as _:
        return TypeError
    return f'{new_name_data}, гр. {group}, GPA {gpa:.2f}'
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))

```
![Картинка 7](images/lab02/C.png)
