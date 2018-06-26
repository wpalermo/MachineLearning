import csv

def gender_list(data_list):
    gender = []
    for line in data_list:
        if line[-2] == '' :
            gender.append('undefined')
        else:
            gender.append(line[-2])

    return gender


def gender_count(data):
    male_count = 0;
    female_count = 0;

    for line in data:
        if line[-2] == "Male":
            male_count += 1
        elif line[-2]  == "Female":
            female_count += 1

    gender_count = (male_count, female_count)
    return gender_count


def count_items(column_list):

    print("\n\n Count ITEMS")
    print(column_list)

    item_types = list(set(column_list))
    print(item_types)


    count_items = [0]*len(item_types)

    print(count_items)

    for element in column_list:
        for i in range(len(item_types)):
            if element == item_types[i]:
                count_items[i] += 1

    print(count_items)
    print(sum(count_items))



    return item_types, count_items

def column_to_list(data, index):
    column_list = []
        # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line in data:
        column_list.append(line[index])

    return column_list



if __name__ == "__main__":
    print("Lendo o documento...")
    with open("chicago.csv", "r") as file_read:
        reader = csv.reader(file_read)
        data_list = list(reader)
    print("Ok!")

    print("Linha 0: ")
    print(data_list[0])

    print("Removendo cabecalho")
    data_list = data_list[1:]


    count_items(column_to_list(data_list[:20], -2))

    print("primeiros 20")
    for line in data_list[:20]:
        print(line)



    print("Gender only")
    genders = gender_list(data_list[:20])
    for gender in genders:
        print(gender)

    print("Gender Count")
    count = gender_count(data_list[:20])
    print(count)
