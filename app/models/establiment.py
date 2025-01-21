import mongoengine as me
from .municipi import Municipi

class Establiment(me.Document):
    nom = me.StringField(max_length=128, required=True, unique=True)
    coordenades = me.PointField(required=True)
    domicili = me.StringField(max_length=256, required=True)
    municipi = me.ReferenceField(Municipi)
    localitat = me.StringField(max_length=128)
    lloc_web = me.URLField()
    especialitats = me.ListField(me.StringField(max_length=64, required=True))
    observacions = me.StringField(max_length=256)
    actiu = me.BooleanField(required=True, default=True)
    telefons = me.ListField(me.StringField(max_length=32, required=True))
    emails = me.ListField(me.StringField(max_length=64, required=True))
    meta = {"collection": "establiments", "allow_inheritance": True}

# Classe TipusBotiga que ha de permetre representar els diversos tipus de botigues que podem tenir
# a la base de dades.
class TipusBotiga(me.Document):
     id = me.SequenceField(primary_key=True)
     nom = me.StringField(max_length=64, unique=True)
     sinonims = me.ListField(me.StringField(max_length=32, required=True, unique=True))
     meta={"collection": "tipus_botigues"}

class Botiga(Establiment):
    tipus = me.ReferenceField(TipusBotiga, required=True)


