import mongoengine as me
from .municipi import Municipi

# Classe que representa el concepte de franja horària, amb una hora d'inici i una hora final.
class FranjaHoraria(me.EmbeddedDocument):
    hora_obertura = me.StringField(min_length=5, max_length=5, regex="([01]\\d|2[0-3]):[0-5]\\d", required=True)
    hora_tancament = me.StringField(min_length=5, max_length=5, regex="([01]\\d|2[0-3]):[0-5]\\d", required=True)

# Classe que representa l'horari diari, indicant el dia de la setmana i les franges horàries.
class HorariDiari(me.EmbeddedDocument):
    dia = me.IntField(min_value=1, max_value=7, required=True)
    franges = me.ListField(me.EmbeddedDocumentField(FranjaHoraria))

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
    horari = me.ListField(me.EmbeddedDocumentField(HorariDiari), max_length=7, required=True)
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


# Classe Restaurant que té tot el que hereta d'Establiment, més l'atribut per definir l'oferta.
class Restaurant(Establiment):
    oferta_gastronomica = me.ListField(me.StringField(max_length=32, required=True, unique=True), required=False)



