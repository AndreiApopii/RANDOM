from random import randint as rand
intrebari=[
    ['BOTANICA',
    'care este cel mai important organ al plantei ce participa la fotosinteza?',
    'care este denumirea populara a plantei <Crăița>?',
    'din ce familie de plante face parte pomul de cireșe?',
    'Mușețelul face parte din familia de plante...?',
    'in ce domeniu al medicinii sunt folosite plantele de camp?',
    'de unde provine gutuiul?',
    'in care parte a Moldovei creste Piersicul?',
    'cate petale are floarea de Măceș?',
    'din ce familie face parte Pinul?',
    'pe care parte a unui truchi sunt situati muschii intr-o padure?'
    ],
    ['ZOOLOGIE',
    'cel mai mare animal care locuieste pe Terra?',
    'din ce regn face parte cainele?',
    'este lacusta un animal vertebrat?',
    'in ce tara vaca este considerat animal sacru?',
    'cum se numeste fatul calului?',
    'cum se numeste fatul caprei?',
    'cum se numeste fatul oii?',
    'din ce familie de animale face parte pisica salbatica?',
    'cati ochi are un paianjen saritor?',
    'cate camere are stomacul unui animal rumegator?',
    ],
    ['MOLDOVA',
    'care este cel mai mare rau din Moldova?',
    'care este cea mai veche manastire din Moldova?',
    'care municipiu este capitala de nord a Republicii Moldova?',
    'cate raioane sunt in Moldova?',
    'care este cel mai mare raion dupa suprafata din Moldova?',
    'care este raionul cu cel mai mic numar de locuitori?',
    'al catalea loc ocupa Moldova dupa suprafata in lume?',
    'cate pene are in coada sa vulturul de pe stema Moldovei?',
    'animalul simbol al Moldovei?',
    'forma de relief predominanta in Moldova?'
    ],
    ['ORNITOLOGIE',
    'pasarea care depune cele mai mari oua?',
    'care este cea mai raspandita specie de bufnite din Moldova?',
    'din ce ordin face parte lebada?',
    'din ce ordin face parte gaina?',
    'unde ierneaza cocostarcii?',
    'in ce mediu natural locuieste egreta mica?',
    'hrana preferata a graurilor?',
    'ce culoare au ouale sturzului cantator?',
    'unica pasare care poate zbura in urma?',
    'care este prima pasare domesticita de om?',
    'care pasare isi lasa puii in cuiburi straine?'
    ],
    ['ANATOMIA OMULUI',
    'cel mai lung os din corpul uman?',
    'cel mai puternic muschi din corpul uman?',
    'cate camere are inima unui om?',
    'care este cea mai mare artera?',
    'unde se afla osul zigomatic?',
    'cum se numeste muschiul inimii?',
    'cate perechi de coaste are omul?',
    'hemofilia este o boala ...?',
    'anemia poate aparea din cauza lipsei de...?',
    'cum se numeste osul bratului?',
    ]
    
    ]
raspunsuri=[['','frunza','ȚIGĂNCUȘA','rozacee','asteracee','farmaceutica','Caucaz','sud','5','pinaceae','nordica'],
            ['','balena','animalia','nu','India','minz','ied','miel','felidae','8','4'],
            ['','Nistru','Manastirea Varzaresti','Balti','32','Cahul','Basarabeasca','139','3','zimbru','campie'],
            ['','strutul','cucuveaua','anseriforme','galiforme','Africa','mediul acvatic','albastra','colibri','disca','cucul'],
            ['','femurul','limba','4','artera aorta','cap','miocard','12','12','singelui','oxigen','humerus']
]
def vreau_milionul():
    x=0
    tema=rand(0,4)
    intrebare=rand(1,10)
    intrebari_puse=[]
    print('Tema:',intrebari[tema][0])
    while x<10:
        x=x+1
        while intrebare in intrebari_puse:
            intrebare=rand(1,10)

        intrebari_puse.append(intrebare)
        print(intrebari[tema][intrebare]) 
        input("pentru raspuns tasteeaza ENTER")
        print(raspunsuri[tema][intrebare])
        print("\n")
    return print("FINISH!")
vreau_milionul()
