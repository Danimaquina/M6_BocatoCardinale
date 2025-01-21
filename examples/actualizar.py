import mongoengine as me

# Classe Municipi que representarà aquest concepte en la nostra aplicació.
class Municipi(me.Document):
    id = me.SequenceField(primary_key=True)
    codi_postal = me.StringField(max_length=5, min_length=5, regex="\\d{5}")
    nom = me.StringField(max_length=128, required=True, unique_with="codi_postal")
    meta = {"collection": "municipis"}

    def __str__(self):
        return "%-5s - %-80s" % (self.codi_postal, self.nom)

if __name__ == "__main__":
    # Connexió sobre la base de dades "boccato_di_cardinale".
    db = me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")
    
    # Consultem el municipi abans de modificar-lo.
    municipis = Municipi.objects(codi_postal="08519")
    print("Abans de la modificació: %s" % municipis[0])

    # Fem la modificació.
    resultat = Municipi.objects(codi_postal="08519").update_one(nom="La Ràpita")

    # Si s'ha fet la modificació, mostrem el municipi actualitzat.
    if resultat:
        print("Després de la modificació: %s" % municipis[0].reload())

    me.disconnect()
