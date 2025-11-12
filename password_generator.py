import random
import string

print("✨🗝️ Secure Password Generator ✨🗝️\n")

while True:
    longitud = int(input("Enter desired password length 🔢: "))
    if longitud >= 6:
        break 
    print("⚠️🐢 The password is too short, must be at least 6 characters.")


caracteres = string.ascii_letters + string.digits + string.punctuation
mayuscula = random.choice(string.ascii_uppercase)
numero = random.choice(string.digits)
simbolo = random.choice(string.punctuation)

resto_longitud = longitud - 3
resto_password = [random.choice(caracteres) for _ in range(resto_longitud)]

password_ready = [mayuscula, numero, simbolo] + resto_password
random.shuffle(password_ready)


password = ''.join(password_ready)
print("\n🔒 Your secure password is:", password, "🎉")
