names = input('Введите имена через пробел: ').split()
k_names = filter(lambda name: 'к' in name or 'К' in name or 'k' in name or 'K' in name, names)
print(list(k_names))
