names = input("Enter names separated by commas: " ).split(',')
assignments = input("Enter assignments counts separated by commas: ").split(',')
grades = input("Enter the grades separated by commas: ").split(',')


print ("nomes: {}".format(len(names)))
print ("assignments: {}".format(len(assignments)))
print ("grades: {}".format(len(grades)))

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments \
before the due date.\n\n"

for index in range(len(names)):
    print("INDEX: " + str(index))
    print(message.format(names[index], assignments[index], grades[index], int(assignments[index])*2))



#Outro jeito mais legal de fazer esse tipo de for..
for name, assignment, grade in zip(names, assignments, grades):
    print (message.format(name, assignment, grade, int(assignment)*2))
