message = int(input("Введи числовое сообщение: "))
random_coefficient_b = random.randint(1, 100)
print("Коэф b:", random_coefficient_b)
random_coefficient_g = random.randint(1, 100)
print("Коэф g:", random_coefficient_g)
random_coefficient_p = random.randint(1, 100)
print("Коэф p:", random_coefficient_p)

A = (random_coefficient_g ** message) % random_coefficient_p
print("Коэф для общего ключа (A):", A)

B = (random_coefficient_g ** random_coefficient_b) % random_coefficient_p
print("Коэф для общего ключа (B):", B)

shared_key_from_message = (B ** message) % random_coefficient_p
print("Ваш общий ключ:", shared_key_from_message)

shared_key_from_b = (A ** random_coefficient_b) % random_coefficient_p
print("Общий ключ друга:", shared_key_from_b)

print("Ka = Kb =", shared_key_from_b)
