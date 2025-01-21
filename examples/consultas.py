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

     # Consultem tots els municipis de la base de dades.
     municipis = Municipi.objects()

     print("TOTS ELS MUNICIPIS:\n")
     for municipi in municipis:
        print(municipi)

     # Consultem el municipi que té un codi postal concret.
     municipi = Municipi.objects(codi_postal="08519")
     print("\n\nMUNICIPI AMB CODI POSTAL 08506:\n")
     print(municipi[0])

     # Consultem tots els municipis de la província de Barcelona, ordenats per nom.
     municipis = Municipi.objects(codi_postal__startswith="08").order_by("nom")
     print("\n\nMUNICIPIS DE LA PROVÍNCIA DE BARCELONA ORDENATS ALFABÈTICAMENT:\n")
     for municipi in municipis:
        print(municipi)

     # Tanquem la connexió.
     me.disconnect()
