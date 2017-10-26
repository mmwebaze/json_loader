import bcrypt

hash = bcrypt.hashpw("district".encode('utf-8'),bcrypt.gensalt(rounds=10, prefix=b"2a"))
print(hash)

#password is between quotes b'$2a$10$JRiFtXlOA4QY/EyN9dSdFOkWqQqNu2SUbTadUKoqEz4eAUQeGlKxO'
#