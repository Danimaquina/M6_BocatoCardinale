import mongoengine as me
import bdc.controller as ct

if __name__ == "__main__":
    db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")

    print("\nLlistat d'establiments que hi ha a la base de dades:\n")
    establiments = ct.obtenir_establiments()
    for i, est in enumerate(establiments, start=1):
        print(f"    {i}: {est.nom:<40} ({est.municipi.codi_postal} - {est.municipi.nom})")
    
    select = input("\nSelecciona un establecimiento por su numero: ")
    establiment_seleccionat = establiments[int(select) - 1]

    print("\nLes especialitats d'aquest establiment són:\n")
    for i, esp in enumerate(establiment_seleccionat.especialitats, start=1):
        print(f"    {i}: {esp}")

    especialitat = input("\nIntrodueix una nova especialitat: ")
    establiment_seleccionat.update(push__especialitats=especialitat)