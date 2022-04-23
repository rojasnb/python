#Generador de tablas de verdad

booleanos = [False, True]

# Tabla de verdad de not

print('p\tnot p')
print('-'*13)
for p in booleanos:
    print(p, not p, sep = '\t')

print()

# Tabla de verdad de and

print('p\tq\tp and q')
print('-'*22)
for p in booleanos:
    for q in booleanos:
        print(p, q, p and q, sep = '\t')
        
print()

# Tabla de verdad de or

print('p\tq\tp or q')
print('-'*22)
for p in booleanos:
    for q in booleanos:
        print(p, q, p or q, sep = '\t')

print()

# Tabla de verdad de ^

print('p\tq\tp ^ q')
print('-'*21)
for p in booleanos:
    for q in booleanos:
        print(p, q, p ^ q, sep = '\t') 