def genereate_numbers(N:int, M:int, prefix=None):
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    