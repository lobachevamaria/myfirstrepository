price = float(input('Введите цену: '))
disc = float(input('Введите скидку: '))
vat = float(input('Введите НДС: '))
base = price * (1 - disc / 100)
vat_amount =base * (vat / 100)
total = base + vat_amount
print(f'База после скидки:{base:.2f} Р')
print(f'НДС:{vat_amount:.2f} Р')
print(f'Итого к оплате:{total:.2f} Р')