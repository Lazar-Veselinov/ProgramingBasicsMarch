name = input()
password = input()
log_pass = input()

while True:
    if password == log_pass:
        print(f"Welcome {name}!")
        break
    log_pass = input()