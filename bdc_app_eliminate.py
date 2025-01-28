import mongoengine as me
import bdc.controller as ct

if __name__ == "__main__":
    db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")

    print("\nLlistat d'establiments que hi ha a la base de dades:\n")
    establiments = ct.obtenir_establiments()
    for i, est in enumerate(establiments, start=1):
        print(f"    {i}: {est.nom:<40} ({est.municipi.codi_postal} - {est.municipi.nom})")

    select_est = input("\nSelecciona un estableciment pel seu numero: ")
    establiment_seleccionat = establiments[int(select_est) - 1]

    print("\nLes especialitats d'aquest establiment són:\n")
    for i, esp in enumerate(establiment_seleccionat.especialitats, start=1):
        print(f"    {i}: {esp}")

    select_esp = input("\nSelecciona una especialit pel seu numero per eliminarla: ")
    especialitat_a_eliminar = establiment_seleccionat.especialitats[int(select_esp) - 1]

    establiment_seleccionat.update(pull__especialitats=especialitat_a_eliminar)

    establiment_seleccionat.reload()

    print("\nLes especialitats actualitzades d'aquest establiment són:\n")
    for i, esp in enumerate(establiment_seleccionat.especialitats, start=1):
        print(f"    {i}: {esp}")