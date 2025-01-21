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

    # Eliminem un municipi. Ho fem seleccionant el municipi a eliminar per codi postal.
    eliminats = Municipi.objects(codi_postal="08519").delete()
    print("Quantitat de municipis eliminats: %d" % eliminats)

    # Eliminem tots els municipis de la província de Barcelona.
    eliminats = Municipi.objects(codi_postal__startswith="08").delete()
    print("Quantitat de municipis eliminats: %d" % eliminats)

    me.disconnect()