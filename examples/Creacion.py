import mongoengine as me

# Classe Municipi que representarà aquest concepte en la nostra aplicació.
class Municipi(me.Document):
   id = me.SequenceField(primary_key=True)
   codi_postal = me.StringField(max_length=5, min_length=5, regex="\\d{5}")
   nom = me.StringField(max_length=128, required=True, unique_with="codi_postal")
   meta = {"collection": "municipis"}


if __name__ == "__main__":
   # Connexió sobre la base de dades "boccato_di_cardinale". Si no existeix
   # aquesta base de dades, es crearà.
   me.connect(host="mongodb://127.0.0.1:27017/boccato_di_cardinale")

   # Creem dos objectes de tipus Municipi, executant directament el
   # mètode save() que és el que fa que es guardi a la base de dades.
   m1 = Municipi(
      nom="Folgueroles",
      codi_postal="08519"
   ).save()

   m2 = Municipi(
      nom="Solsona",
      codi_postal="25280"
   ).save()

   # Tanquem la connexió.
   me.disconnect()
