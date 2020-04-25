import hashlib

puzzle_input = "uqwqemis"

# i = 0
# while True:
#     h = hashlib.md5(f'{puzzle_input}{i}'.encode())
#     digest = h.hexdigest()
#     if digest.startswith('00000'):
#         print(digest[5], end='', flush=True)
#     i+=1

i = 0
password = ["_"] * 8
while True:
    h = hashlib.md5(f"{puzzle_input}{i}".encode())
    digest = h.hexdigest()
    if digest.startswith("00000"):
        pos = int(digest[5], base=16)
        if pos < len(password) and password[pos] == "_":
            password[pos] = digest[6]
            print("".join(password))
    if "_" not in password:
        break
    i += 1
