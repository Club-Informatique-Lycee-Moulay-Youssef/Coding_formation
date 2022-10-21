
# First Example
password = "abcd123"

enter_you_password = str(input('Your Password :'))

if password == enter_you_password:
    print('Correct Password !!!!!')
else:
    print('Invalid Password !')


# Second Example
month = str(input('Le Mois:'))

if month == 'Janvier':
    print('Janvier : 31jrs')
elif month == 'Février':
    print('Février: 28 ou 29 jrs')
elif month == 'Mars':
    print('Mars : 31 jrs')
elif month == 'Avril':
    print('Avril: 30jrs')
elif month == 'Mai':
    print('Mai: 31jrs')
elif month == 'Juin':
    print('Juin:30jrs')
elif month == 'Juillet':
    print('Juillet:31jrs')
elif month == 'Aout':
    print('Aout: 31jrs')
elif month == 'Septembre':
    print('Septembre:30jrs')
elif month == 'Octobre':
    print('Octobre:31jrs')
elif month == 'Novembre':
    print('Novembre:30jrs')
elif month == 'Décembre':
    print('Décembre:31jrs')
else:
    print('Invalid !')

# Application
x = float(input('Entrez la valeur de x: '))
y = float(input('Entrez la valeur de y: '))

if x > y:
    print('yes')
elif x <= y:
    print('non')