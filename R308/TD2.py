"""
*************
Exercice 1 :

Création programme pour effectuer une division entre deux nombres réels passés en argument d'une fonction
Gérer toutes les exceptions qui peuvent être générée par ce code.
Traiter le cas ou l’un des deux arguments n’est pas de type réel
*************
"""

def division_reelle(a, b): # défini la foncion "division_reelle
    try: # permet de définir à partir de quelle ligne on doit etre attentif
        if not isinstance(a, float) or not isinstance(b, float):# Si ce n'est pas un nombre reel, alors, on affiche le message d'erreur
            raise TypeError("Les deux arguments doivent être de type float (réel).")# Message d'erreur pour l'utilisateur
            # Vérification de la division par zéro
        if b == 0.0: # Si le nombre de la variable "b" est égale à zéro, alors, on affiche un message d'erreur
            raise ZeroDivisionError("Division par zéro impossible.")# Message erreur indiquant qu'il n'est pas possible de diviser par zéro
            # Autrement, si tout est correct, effectuer la division
            resultat = a / b

    except TypeError as te: # te = TypeError (c'est un alias "as", utile dans un programme, évite les erreurs de frappe et autres....)
        print("Erreur de type :", te) # Si le type est mauvais, alors on affiche un message d'erreur
        return None

    except ZeroDivisionError as zde: # impossible de diviser par zéro
        print("Erreur de division :", zde) # message d'erreur
        return None

    except Exception as e: # traitement des autres exceptions de la classe Exception
        print("Erreur inattendue :", e) # Message d'erreur
        return None

    else:
        print("Résultat de la division :", resultat)#
        return resultat

    finally:
        print("Fin de l'exécution de la fonction.")
