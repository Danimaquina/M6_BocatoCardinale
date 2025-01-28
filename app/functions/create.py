from app.models.municipi import Municipi
from app.models.establiment import Botiga, TipusBotiga, HorariDiari, FranjaHoraria

def create_basic():
    # Creem dos objectes de tipus Botiga, amb els seus tipus i els seus municipis.
    m1 = Municipi(
        nom="Folgueroles",
        codi_postal="08519"
    )
    m2 = Municipi(
        nom="Taradell",
        codi_postal="08552"
    )
    t1 = TipusBotiga(
        nom="Forn",
        sinonims=["Fleca", "Forn de pa"]
    )
    t2 = TipusBotiga(
        nom="Carnisseria",
        sinonims=["Cansaladeria", "Xarcuteria"]
    )
    b1 = Botiga(
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
        emails=["info@cocadelmossen.cat"],
        horari=[
            HorariDiari(
                dia=1,
                franges=[FranjaHoraria(hora_obertura="09:00", hora_tancament="13:30"),
                         FranjaHoraria(hora_obertura="17:00", hora_tancament="20:00")]
            )
        ],
        tipus=t1
    ).save(cascade=True)

    b2 = Botiga(
        nom="Carnisseria cansaladeria Codina",
        coordenades=(2.287847, 41.873690),
        domicili="C. de Sant Sebastià, 18",
        municipi=m2,
        localitat=None,
        lloc_web="https://carnisseriacodina.cat",
        especialitats=["Botifarra d'ou", "Llonganissa", "Bull de ratafia amb tòfona"],
        observacions=None,
        actiu=True,
        telefons=["93 880 11 75"],
        emails=["info@carnisseriacodina.com"],
        horari=[
            HorariDiari(
                dia=1,
                franges=[FranjaHoraria(hora_obertura="09:00", hora_tancament="13:30"),
                         FranjaHoraria(hora_obertura="17:00", hora_tancament="20:00")]
            )
        ],
        tipus=t2
    ).save(cascade=True)
