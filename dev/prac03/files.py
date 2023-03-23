# 1.

in_file = open('name.txt', 'w')
name = input("Name: ")
print(name, file=in_file)
in_file.close()

# 2.

out_file = open('name.txt', 'r')
name = out_file.readline()
print(f"Your name is {name}")
out_file.close()

# 3.

out_file = open('numbers.txt', 'r')
num = out_file.readlines()
total = int(num[0]) + int(num[1])
print("Total for 2 numbers: ", total)
out_file.close()

# 4.

out_file = open('numbers.txt', 'r')
total = 0
for line in out_file:
    total += int(line)
print("Total for all numbers in list= ", total)
out_file.close()


