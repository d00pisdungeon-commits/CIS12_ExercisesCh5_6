def countdown_by_two(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown_by_two(n-2)

countdown_by_two(5)