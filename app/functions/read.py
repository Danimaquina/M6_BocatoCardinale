from app.models.establiment import Establiment

def read_basic():
    establiments = Establiment.objects()

    for establiment in establiments:
        print(establiment.nom, establiment.municipi.nom, sep=", ")