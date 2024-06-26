import math

def is_prime(num):
    if num <= 1:
        return False
    for divisor in range(2, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False
    return True

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = [i for i in range(2, phi) if is_prime(i) and phi % i != 0]

    d = []
    for candidate in range(2, 500):
        if (candidate * e[0]) % phi == 1:
            d.append(candidate)
            break

    return (e[0], n), (d[0], n)

def encrypt(message, public_key):
    e, n = public_key
    return (message ** e) % n

def decrypt(ciphertext, private_key):
    d, n = private_key
    return (ciphertext ** d) % n

if __name__ == "__main__":
    p = int(input("Введи p: "))
    q = int(input("Введи q: "))
    
    public_key, private_key = generate_keys(p, q)
    
    print("Число n:", p * q)
    print("Число φи(n):", (p - 1) * (q - 1))
    print("Открытый ключ:", f"{public_key}")
    print("Закрытый ключ:", f"{private_key}")
    
    message = int(input("Введи сообщение (число, не большее n): "))
    ciphertext = encrypt(message, public_key)
    print("Шифрованное сообщение:", ciphertext)
    
    decrypt_query = input("Произвести расшифровку? (Да или нет): ").lower()
    if decrypt_query == "да":
        decrypted_message = decrypt(ciphertext, private_key)
        print("Расшифрованное сообщение:", decrypted_message)
    else:
        print("Ок. Работа закончена")

