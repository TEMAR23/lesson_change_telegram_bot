
A_group = ["7a", "7b", "7c", "8a", "8b", "8c", "9a", "9b", "9c", "9d", "10a", "10b", "10c", "10d"]
B_group = ["11a", "11b", "11c", "11d", "11sb", "10e", "10sb", "11e", "12a", "12b", "12c", "12d", "12e", "12sb"]

def return_time_group(class_num):
    if class_num in A_group:
        return "A"
    elif class_num in B_group:
        return "B"

def send_consultations_list(page):
    text1 = """Konsultācijas 1/3
    ANSTRANGA INESE Pirmdiena 14:30-17:03 208,
    APINE SABĪNE Pirmdiena 15:30-18:10 216,
    IEVA APĪNE Pirmdiena 15:20-16:33 223
                Otrdiena 14:30-15:53 223
                Trešdiena 14:20-15:10 223
                Trešdiena 16:10-16:54 223,
    ARĀJS JĀNIS	Pirmdiena 8:00-8:30	205
                Pirmdiena 15:00-16:00 205
                Piektdiena 8:00-8:30 205
                Piektdiena 15:00-15:51 205,
    ĀBOLIŅŠ AIGARS Pirmdien 15:20-16:06 332,
    ANDRIS BABRIS Ceturtdiena 14:40-15:11	37,
    BARBĀNE GUNTA Trešdiena 16:00-16:54 220
                Ceturtdienas 15:20-16:31 220,
    BĒTS RAIVIS	Ceturtdienas 15:20-15:54 327,
    BOLDĀNE GINTA Trešdiena 16:50-18:56 227,
    BOMIS ALDIS	Otrdiena 8:00-9:30	304
                Otrdiena 15:20-16:33 304,
    BONDAREVA JEĻENA Pirmdiena 13:40-15:45 213,
    BREIDAKA INGRĪDA Trešdiena 16:00-16:52 25,
    BRĒDE ELEONORA Otrdiena 13:00-15:30 137
                Ceturtdiena 16:00-17:10	137
                Piektdiena 16:00-17:10 137,
    BRIŅĶE DAINA Piektdiena 15:20-17:07 307,
    CIFTLER ABDULLAH SINAN Trešdiena 16:00-16:32 209,
    DARĢE ILZE Trešdiena 14:30-14:41 110,
    DESMITNIECE KAIVA Pirmdiena 15:30-17:36 334,
    DONSKA ELITA Pirmdiena 16:10-17:00 333
                Piektdiena 14:40-15:44 333,
    DZIĻUMA KRISTĪNE Ceturtdiena 15:30-18:04	210,
    AIVARS ERIŅŠ Pirmdiena 14:30-15:38 133,
    FREIMANE ILGA Pirmdiena 14:30-14:53 141,
    GAVRASE MARIJA Otrdiena 16:10-17:00 215
                Piektdiena 15:20-16:36 215,"""

    text2 = """Konsultācijas 2/3
    GRAUDS KĀRLIS Piektdiena 16:00-17:14 418,
    GŪTMANIS OĻĢERTS Trešdiena 8:00-8:40 223
                Piektdiena 15:20-16:52 229,
    ĢĒRMANIS ANDRIS	Pirmdiena 14:30-17:38 142,
    KAPILINSKA ANTRA Pirmdiena 15:20-15:31 121,
    KLATENBERGS REINIS Otrdiena 15:10-15:29 216,
    KNOKA ŽANNA	Trešdienas 16:00-17:44 329,
    KRASTIŅA INETA Piektdiena 15:30-16:39 114,
    KRIEVIŅA VITA Otrdiena 8:54-9:30 220,
    KULAKOVS PĀVELS Pirmdiena 14:40-17:14 310,
    KUNGS JĀNIS Pirmdiena 16:00-16:34 226/210,
    ILVA LAZDĀNE Ceturtdiena 15:30-17:01 208,
    LAPIŅA LANA	Trešdiena 16:40-17:09 216,
    LAUBERTS KALVIS	Trešdiena 08:00-08:40 208
                Trešdiena 16:30-17:44 142,
    LIEPIŅŠ MĀRIS Otrdiena 8:00-9:14 418,
    LINIŅŠ AIVARS Trešdiena 15:20-15:54 418,
    LĪDUMNIECE ELITA Otrdiena 16:00-18:00 136
                Ceturtdiena 16:00-17:20	136,
    LŪSIS ERVĪNS Piektdiena 14:40-16:00 39,
    ĻUĻA LUDMILA Piektdiena 16:00-16:31 418,
    MEIJERE LAURA Otrdiena 15:10-17:33 208,
    MUIŽNIEKS VOLDEMĀRS	Otrdiena 14:30-16:30 133
                Piektdiena 8:00-8:40 133,
    NĀTRE AGNESE Trešdiena 15:30-17:47 140,
    NORE SANDRA	Otrdiena 14:40-16:10 311,
                Ceturtdiena 15:30-16:46	
    """

    text3 = """Konsultācijas 3/3
    OSTROVSKA MARIJA Pirmdiena 15:20-16:08 305
                Otrdiena 15:20-16:09 209,
    PELCE RUTA Pirmdiena 15:30-17:01 326,
    LINDA PILĀNE Otrdiena 16:10-17:25 313,
    PIZIKA ZAIGA Trešdiena 8:00-8:40 333
                Ceturtdiena 14:25-16:25 333,
    POROZOVA DZINTRA Otrdiena 8:00-8:30	221
                Otrdiena 15:20-16:00 221
                Trešdiena 14:40-15:36 221
                Ceturtdiena 14:40-15:20	221,
    ROZIŅA INĀRA Pirmdiena 15:20-17:03 334,
    RUĻUKA-PAŠA DIĀNA Ceturtdiena 14:40-15:20 141
                Pirmdiena 15:30-17:07 327,
    SKUTELE DACE Pirmdiena 15:30-17:07 428
                Piektdiena 8:00-8:40 428,
    STEPANOVA JULIJA Trešdiena 16:10-17:15 214
                Piektdiena 16:10-17:16 214,
    STRIGAĻOVA TATJANA Trešdiena 16:10-16:56 332,
    STROŽA ANNA	Pirmdiena 14:30-16:10 141
                Piektdiena 16:00-16:48 141,
    STŪRMANE MAIJA Trešdiena 14:40-17:32 312,
    SVAĻBA MODRIS Piektdiena 15:20-15:37 37,
    ŠTOKMANE DAINA Ceturtdiena 15:30-16:24 306
                Piektdiena 15:30-16:24 306,
    TREIJA KAIVA Otrdiena 08:00-09:20 305
                Piektdiena 14:30-14:53 305,
    TREIMANE INGA Trešdiena 16:00-16:46	111,
    VASIĻEVSKIS GUNTIS Otrdiena 8:45-9:30 313,
    VĀRTIŅA ANDRA Piektdiena 16:10-17:29 334,
    VASIĻIVA INDRA Pirmdienas 14:00-14:40 229
                Pirmdienas 16:00-17:20 229,
    VĪKSNA INETA Piektdiena 16:00-17:37 142,
    ZAUERS ALVILS Trešdiena 15:20-15:54	209,
    ŽUTAUTAS MARTINS Pirmdiena 15:30-16:59 213
                Pirmdiena 15:30-17:00 213
    """

    if page == 1:
        return text1
    elif page == 2:
        return text2
    elif page == 3:
        return text3