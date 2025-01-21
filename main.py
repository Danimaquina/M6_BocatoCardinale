from app import connect, disconnect
from app.models.municipi import Municipi
from app.models.establiment import Establiment


if __name__ == '__main__':
    db = connect('mongodb://localhost:27017/boccato_di_cardinale')

    # Creem un objecte de tipus Establiment i l'objecte de tipus Municipi que
    # correspon per poder definir la seva localització.
    m1 = Municipi(
        nom="Folgueroles",
        codi_postal="08519"
    )

    e1 = Establiment(
        nom="Forn de Sant Jordi",
        coordenades=(2.318286, 41.938136),
        domicili="C. Atlàntida, 8",
        municipi=m1,
        localitat=None,
        lloc_web="http://www.cocadelmossen.cat",
        especialitats=["Coca de pa", "Coca de sucre", "Coca amb xocolata",
                       "Coca de cabell d'àngel"],
        observacions=None,
        actiu=True,
        telefons=["93 888 72 25"],
        emails=["info@cocadelmossen.cat"]
    ).save(cascade=True)

    # Tanquem la connexió.
    disconnect()