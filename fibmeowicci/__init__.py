from time import sleep


def meow(limit: int | None = None, sleep_factor=0.01):
    """Make with the meows."""
    fibb, follow = 0, 1
    while True:
        if limit and fibb >= limit:
            break
        meows = " ".join(["meow"] * fibb).capitalize()
        if len(meows):
            print(f"{meows}.\n")
        fibb, follow = follow, fibb + follow
        if sleep_factor:
            sleep(fibb * sleep_factor)
