numbers = open("numbers.txt", "w")
numbers.write("")
numbers.close()

numbers = open("numbers.txt", "a")

for i in range(1, 11):
    numbers.write("{}\n".format(str(i)))
    # Colocando "\n", na ultima escrita pulará uma linha, ou seja o arquivo terá uma linha a mais do que elementos

numbers.close()