# coding: utf-8

# Começando com os imports
import csv
import statistics
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")


# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

for line in data_list[:20]:
    print(line)


# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")


# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

#Ternary Operator no python, pesquisado na internet no site abaixo.
#http://book.pythontips.com/en/latest/ternary_operators.html
for gender in data_list[:20]:
    print(gender[-2] if gender[-2] != "" else "undefined")

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")



# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """ Recebe uma lista de listas, no caso CSV e retorna apenas uma coluna dessa lista,
    na mesma ordem da lista de entrada
    INPUT:
        data: list. lista completa com todas as linhas e colunas
        index: int. indice da coluna que sera retornada
    OUTPUT:
        column_list: list. lista com a coluna relativa ao indice passado na entrada
    """

    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line in data:
        column_list.append(line[index])

    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem


# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.

male = 0
female = 0

for line in data_list:
    if line[-2] == "Male":
        male += 1
    elif line[-2] == "Female":
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """ Recebe uma lista de genereos e retorna a quantidade de cada um.

    INPUT:
        data_list: list. lista de generos

    OUTPUT:
        return: list. lista com 2 valores o primeiro de numero de generos Masculinos
        e o segundo com numero de generos femininos
    """

    male = 0
    female = 0

    for line in data_list:
        if line[-2] == "Male":
            male += 1
        elif line[-2] == "Female":
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """ Recebe uma lista de generos e retorna a qual é mais popular (qual tem mais).

    INPUT:
        data_list: list. lista de generos

    OUTPUT:
        answer: string. Retorna o genero mais popular, caso sejam iguais retorna IGUAL
    """

    answer = ""
    genders = count_gender(data_list)

    if genders[0] > genders[1]:
        answer = "Masculino"
    elif genders[1] > genders[0]:
        answer = "Feminino"
    else:
        answer = "Igual"


    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")



# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_type(type_list):
    """ Recebe uma lista de tipos e retorna a quantidade de cada um.

    INPUT:
        data_list: list. lista de tipos

    OUTPUT:
        list. lista com a quantidade de cada um dos tipos da lista. No caso
              Costumer, Subscriber ou Dependent
    """
    cost = 0
    sub = 0
    dep = 0

    for line in type_list:
        if line == "Customer":
            cost += 1
        elif line == "Subscriber":
            sub += 1
        elif line == "Dependent":
            dep += 1

    #print(cost)
    #print(sub)
    #print(dep)

    return [cost, dep, sub]



type_list = column_to_list(data_list, -3)
types = sorted(list(set(type_list)))
#print(sorted(list(set(type_list))))
quantity = count_type(type_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuario')
plt.show(block=True)





input("Aperte Enter para continuar...")


# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Pois exitem algumas linhas onde o sexo nao foi informado pelo usuario"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = list(map(int, column_to_list(data_list, 2)))

max_trip = 0
min_trip = trip_duration_list[0]
total_trip = 0

for value in trip_duration_list:
    if value > max_trip:
        max_trip = value
    if value < min_trip:
        min_trip = value

    total_trip += value



sorted_duration_list = sorted(trip_duration_list)

if len(sorted_duration_list) % 2 == 1:
    median_trip = sorted_duration_list[len(trip_duration_list) // 2]
else:
    index1 = sorted_duration_list[(len(trip_duration_list) // 2)]
    index2 = sorted_duration_list[(len(trip_duration_list) // 2) + 1]
    mean_trip = (index1 + index2) // 2

median_trip = sorted(trip_duration_list)[len(trip_duration_list) // 2]
mean_trip = total_trip / len(trip_duration_list)



print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")



# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(list(start_stations))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """ Recebe uma lista de qualquer e retorna a quantidade de tipos e a Quantidade
    de cada um dos tipos.

    INPUT:
        data_list: list. lista generica

    OUTPUT:
        item_types: list. lista com os tipos encontrados na colunas
        count_items: list. lista com a contagem de itens relativas ao seu tipo
    """
    #print("\n\n Count ITEMS")
    #print(column_list)

    item_types = list(set(column_list))
    #print(item_types)

    #Inicializacao encontrada na em pesquisa na internet
    #stackoverflow
    count_items = [0]*len(item_types)
    #print(count_items)

    for element in column_list:
        for i in range(len(item_types)):
            if element == item_types[i]:
                count_items[i] += 1

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
