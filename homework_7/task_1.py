def dz_v_sm(n):
    return print(float(n) * 2.54, 'sm')

def sm_v_dz(n):
    return print(float(n) * 0.393701, 'dz')

def ml_v_kl(n):
    return print(float(n) * 1.60934, 'kl')

def kl_v_ml(n):
    return print(float(n) * 0.621371, 'ml')

def f_v_kg(n):
    return print(float(n) * 0.453592, 'kg')

def kg_v_f(n):
    return print(float(n) * 2.20462, 'f')

def unc_v_g(n):
    return print(float(n) * 28.3495, 'g')

def g_v_unc(n):
    return print(float(n) * 0.035274, 'unc')

def ga_v_l(n):
    return print(float(n) * 4.54609, 'l')

def l_v_ga(n):
    return print(float(n) * 0.219969, 'ga')

def pi_v_l(n):
    return print(float(n) * 0.473176, 'l')

def l_v_pi(n):
    return print(float(n) * 2.11338, 'pi')

cod = 13
while cod != 0:
    cod = int(input('Выберите операцию: \n 1. Дюймы в сантиметры \n 2. Сантиметры в дюймы \n 3. Мили в километры \n 4. Километры в мили \n 5. Фунты в килограммы \n 6. Килограммы в фунты \n 7. Унции в граммы \n 8. Граммы в унции \n 9. Галлон в литры \n 10. Литры в галлоны \n 11. Пинты в литры \n 12. Литры в пинты \n'))
    if cod == 0:
        break
    elif cod < 0 or cod >= 13:
        print("Введите другое число")
        continue
    x = input("Введите число, которое необхомо перевести: ")
    if cod == 1:
        dz_v_sm(x)
    elif cod == 2:
        sm_v_dz(x)
    elif cod == 3:
        ml_v_kl(x)
    elif cod == 4:
        kl_v_ml(x)
    elif cod == 5:
        f_v_kg(x)
    elif cod == 6:
        kg_v_f(x)
    elif cod == 7:
        unc_v_g(x)
    elif cod == 8:
        g_v_unc(x)
    elif cod == 9:
        ga_v_l(x)
    elif cod == 10:
        l_v_ga(x)
    elif cod == 11:
        pi_v_l(x)
    elif cod == 12:
        l_v_pi(x)
