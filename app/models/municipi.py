import mongoengine as me

# Classe Municipi que representarà aquest concepte en la nostra aplicació.
class Municipi(me.Document):
   id = me.SequenceField(primary_key=True)
   codi_postal = me.StringField(max_length=5, min_length=5, regex="\\d{5}")
   nom = me.StringField(max_length=128, required=True, unique_with="codi_postal")
   meta = {"collection": "municipis"}