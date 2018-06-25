f = open("./resources/camelot.txt", 'r')
file_data = f.read()
f.close()

print(file_data)

with open("./resources/camelot.txt", 'r') as f2:
    file_data2 = f2.read()
    print(file_data2)
