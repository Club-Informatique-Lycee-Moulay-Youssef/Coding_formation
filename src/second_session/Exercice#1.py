"""
Tentez d’écrire un script qui convertit un montant en Euros vers les Dollars.
Le montant en Euros est demandé à l’utilisateur et récupéré dans une variable dont le nom est nb_euro.
Le taux de change, ´1 EUR = 1.09 USD´, est stocké dans une variable taux_change, mais sa valeur ne change pas au cours du script.
On print ensuite à l'écran " ... Euros vaut ... Dollars " avec les valeurs correspondantes.
"""
nb_euro = float(input('Entrez le montant en Euros :'))
taux_change = nb_euro * 1.09
# Print
print(nb_euro, "Euros vaut", taux_change, "Dollars")
print("{} Euros vaut {} Dollars".format(nb_euro, taux_change))
print(f"{nb_euro} Euros vaut {taux_change} Dollars")