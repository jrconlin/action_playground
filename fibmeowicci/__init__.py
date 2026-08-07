from time import sleep


def meow(limit: int | None = None):
    fibb, follow = 0, 1
    while True:
        if limit and fibb >= limit:
            break
        print(" ".join(["meow"] * fibb))
        fibb, follow = follow, fibb + follow
        sleep(fibb * 0.10)
