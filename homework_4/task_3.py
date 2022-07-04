x = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
y = list(x.keys())
for i in range(len(y)):
    y[i] += str(len(y[i]))
a = x.values()
print(x)
print({k:v for k, v in zip(y, a)})
# не знаю как через while
