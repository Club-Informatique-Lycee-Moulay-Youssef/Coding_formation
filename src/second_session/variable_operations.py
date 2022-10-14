# Opérations sur les variables
exam_1 = float(input('Entrez la note du premier examen: '))
exam_2 = float(input('Entrez la note du deuxième examen: '))
operation = (exam_1 + exam_2) / 2
# First Method to print
print('Votre note du premier examen est', exam_1, 'et votre note du deuxième examen est', exam_2, 'et votre moyenne est', operation)
# Second Method
print('Votre note du premier examen est {} et votre note du deuxième examen est {} et votre moyenne est {}'.format(exam_1, exam_2, operation))

#
# Calculate your age
annee_de_naissance = int(input('Entrez votre année de naissance: '))
annee_actuelle = int(input('Entrez l\'année actuelle : '))
age = annee_actuelle - annee_de_naissance
print('Vous avez', age, 'ans')

# Third Exercice
rayon = int(input('Entrez le rayon du cercle: '))
result = 3.14 * (rayon * 2)

#
# Calculate the power of a number
number = int(input('Entrez un nombre: '))
power = int(input('Entrez la puissance: '))
result = number ** power
print(result)

#
simple_division = 15 / 2
print(simple_division)
division_1 = 15 // 2
print(division_1)

# Modulus
division_2 = 15 % 7
print(division_2)