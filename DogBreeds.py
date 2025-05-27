# Filter through dogs through size and weight, and recommend it to the user
import random


dogBreeds = ["Affenpinscher" , "AfghanHound" , "AiredaleTerrier" , "AkbashDog" , "Akita" , "AlapahaBlueBloodBulldog" , "AlaskanHusky" , "AlaskanMalamute" , "AmericanEskimoDog" , "AmericanFoxhound" , "AmericanPitBullTerrier" , "AmericanWaterSpaniel" , "AnatolianShepherdDog" , "AustralianKelpie" , "AustralianShepherd" , "Azawakh" , "Basenji" , "BassetBleudeGascogne" , "Beagle" , "Beauceron" , "BedlingtonTerrier" , "BelgianMalinois" , "BelgianTervuren" , "BerneseMountainDog" , "BlackandTanCoonhound" , "Bloodhound" , "BluetickCoonhound" , "Boerboel" , "BorderTerrier" , "BostonTerrier" , "BouvierdesFlandres" , "Boxer" , "BoykinSpaniel" , "BraccoItaliano" , "Briard" , "Brittany" , "Bullmastiff" , "CairnTerrier" , "CaneCorso" , "CardiganWelshCorgi" , "CatahoulaLeopardDog" , "CaucasianShepherd(Ovcharka)" , "CavalierKingCharlesSpaniel" , "ChineseCrested" , "Chinook" , "ChowChow" , "ClumberSpaniel" , "CockerSpaniel(American)" , "CotondeTulear" , "Dalmatian" , "DogoArgentino" , "EnglishShepherd" , "EnglishSpringerSpaniel" , "Eurasier" , "FieldSpaniel" , "FinnishLapphund" , "GermanPinscher" , "GermanShepherdDog" , "GermanShorthairedPointer" , "GiantSchnauzer" , "GlenofImaalTerrier" , "GoldenRetriever" , "GordonSetter" , "GreatDane" , "GreatPyrenees" , "Greyhound" , "Harrier" , "Havanese" , "IrishSetter" , "IrishWolfhound" , "ItalianGreyhound" , "JapaneseChin" , "Keeshond" , "Komondor" , "Kuvasz" , "LabradorRetriever" , "LagottoRomagnolo" , "Leonberger" , "LhasaApso" , "Maltese" , "MiniatureSchnauzer" , "Newfoundland" , "NorfolkTerrier" , "Papillon" , "PembrokeWelshCorgi" , "PharaohHound" , "Plott" , "Pug" , "RedboneCoonhound" , "RhodesianRidgeback" , "Rottweiler" , "Samoyed" , "Schipperke" , "ScottishDeerhound" , "ShihTzu" , "SilkyTerrier" , "SoftCoatedWheatenTerrier" , "SpanishWaterDog" , "Vizsla" , "Weimaraner"]
dogBreeds = [item.lower() for item in dogBreeds]

dogWeight =[ 13  ,  60  ,  65  ,  120  ,  115  ,  90  ,  50  ,  100  ,  40  ,  75  ,  60  ,  45  ,  150  ,  46  ,  65  ,  55  ,  24  ,  40  ,  35  ,  110  ,  23  ,  80  ,  65  ,  120  ,  100  ,  110  ,  80  ,  200  ,  16  ,  25  ,  110  ,  70  ,  40  ,  88  ,  90  ,  45  ,  130  ,  14  ,  120  ,  38  ,  95  ,  100  ,  18  ,  13  ,  90  ,  70  ,  85  ,  30  ,  15  ,  55  ,  100  ,  66  ,  50  ,  70  ,  50  ,  53  ,  45  ,  90  ,  70  ,  90  ,  40  ,  75  ,  80  ,  190  ,  115  ,  70  ,  60  ,  13  ,  70  ,  180  ,  15  ,  9  ,  45  ,  100  ,  115  ,  80  ,  35  ,  170  ,  18  ,  7  ,  20  ,  150  ,  12  ,  12  ,  30  ,  60  ,  60  ,  18  ,  80  ,  80  ,  110  ,  60  ,  16  ,  130  ,  16  ,  10  ,  40  ,  50  ,  65  ,  90 ]
filteredList =[]

def dogSize():
    x = input("What size dog are you looking for? (tiny, small, medium, large)")
    if x == "tiny":
        for i in range(len(dogWeight)):
            if dogWeight[i] <= 10:
                filteredList.append(dogBreeds[i])
        print(filteredList)

    if x == "small":
        for i in range(len(dogWeight)):
            if dogWeight[i] <= 20 and dogWeight[i] > 10:
                filteredList.append(dogBreeds[i])
        print(filteredList)

    if x == "medium":
        for i in range(len(dogWeight)):
            if dogWeight[i] <= 50 and dogWeight[i] > 20:
                filteredList.append(dogBreeds[i])
        print(filteredList)

    if x == "large":
        for i in range(len(dogWeight)):
            if dogWeight[i] <= 100 and dogWeight[i] > 50:
                filteredList.append(dogBreeds[i])
        print(filteredList)

    print("""
""" + "I recommend " + str(random.choice(filteredList)) + """
""")

#dogSize()



#------------------------------------------------------------------------------
#Goal 1: Create a Python function that allows users to
# look up information (temperament and image) about a specific dog breed.
# Necessary Data: Temperament , Image

#1. Prompt the user for a dog breed:
#   Use the input() function to get the dog breed from the user.
#2. Search for the dog breed:
#   Search the dataset for the entered dog breed.
#   Handle cases where the breed is not found.
#   Obtain the index of where you found the breed on the list.
#3. Print the temperament and display an image:
#   Use the index you found in the previous step to access this information
#   Display the temperament to the user.
#   Display an image of the breed

#############################
#Goal 2: Create a Python function that filters and displays dog breeds based on user-specified purpose (e.g., companion, guarding, herding).
#Necessary Data: Bred For

#1. Prompt the user for their desired purpose:
#   Use the input() function to get the purpose from the user.
#   Options to test can include: circus, companion, sled, hunt, farm, guard etc...
#2. Filter the dataset:
#   Loop through the the dog breed dataset.
#   Filter the dataset to find breeds where the "bred_for" column (or a similar column) contains the user's input. (Check resources for more info)
#   Handle cases where no matching breeds are found.
#3. Return matching breeds:
#   Display a recommendation for the user

##########################
#Goal 3:  Create a Menu and add your finishing touches

#1. Use your functions for your menu

#2. Add an option that will display all of the dog breeds

#3. Create a while loop to keep the program running

#4. Structure your code and add comments


# opening image function
from PIL import Image
import requests
from io import BytesIO
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


# List for GOAL 1:
dogTemper = ["Stubborn,Curious,Playful,Adventurous,Active,Fun-loving" , "Aloof,Clownish,Dignified,Independent,Happy" , "Outgoing,Friendly,Alert,Confident,Intelligent,Courageous" , "Loyal,Independent,Intelligent,Brave" , "Docile,Alert,Responsive,Dignified,Composed,Friendly,Receptive,Faithful,Courageous" , "Loving,Protective,Trainable,Dutiful,Responsible" , "Friendly,Energetic,Loyal,Gentle,Confident" , "Friendly,Affectionate,Devoted,Loyal,Dignified,Playful" , "Friendly,Alert,Reserved,Intelligent,Protective" , "Kind,Sweet-Tempered,Loyal,Independent,Intelligent,Loving" , "StrongWilled,Stubborn,Friendly,Clownish,Affectionate,Loyal,Obedient,Intelligent,Courageous" , "Friendly,Energetic,Obedient,Intelligent,Protective,Trainable" , "Steady,Bold,Independent,Confident,Intelligent,Proud" , "Friendly,Energetic,Alert,Loyal,Intelligent,Eager" , "Good-natured,Affectionate,Intelligent,Active,Protective" , "Aloof,Affectionate,Attentive,Rugged,Fierce,Refined" , "Affectionate,Energetic,Alert,Curious,Playful,Intelligent" , "Affectionate,Lively,Agile,Curious,Happy,Active" , "Amiable,EvenTempered,Excitable,Determined,Gentle,Intelligent" , "Fearless,Friendly,Intelligent,Protective,Calm" , "Affectionate,Spirited,Intelligent,Good-tempered" , "Watchful,Alert,Stubborn,Friendly,Confident,Hard-working,Active,Protective" , "Energetic,Alert,Loyal,Intelligent,Attentive,Protective" , "Affectionate,Loyal,Intelligent,Faithful" , "Easygoing,Gentle,Adaptable,Trusting,EvenTempered,Lovable" , "Stubborn,Affectionate,Gentle,EvenTempered" , "Friendly,Intelligent,Active" , "Obedient,Confident,Intelligent,Dominant,Territorial" , "Fearless,Affectionate,Alert,Obedient,Intelligent,EvenTempered" , "Friendly,Lively,Intelligent" , "Protective,Loyal,Gentle,Intelligent,Familial,Rational" , "Devoted,Fearless,Friendly,Cheerful,Energetic,Loyal,Playful,Confident,Intelligent,Bright,Brave,Calm" , "Friendly,Energetic,Companionable,Intelligent,Eager,Trainable" , "Stubborn,Affectionate,Loyal,Playful,Companionable,Trainable" , "Fearless,Loyal,Obedient,Intelligent,Faithful,Protective" , "Agile,Adaptable,Quick,Intelligent,Attentive,Happy" , "Docile,Reliable,Devoted,Alert,Loyal,Reserved,Loving,Protective,Powerful,Calm,Courageous" , "Hardy,Fearless,Assertive,Gay,Intelligent,Active" , "Trainable,Reserved,Stable,Quiet,EvenTempered,Calm" , "Affectionate,Devoted,Alert,Companionable,Intelligent,Active" , "Energetic,Inquisitive,Independent,Gentle,Intelligent,Loving" , "Alert,Quick,Dominant,Powerful,Calm,Strong" , "Fearless,Affectionate,Sociable,Patient,Playful,Adaptable" , "Affectionate,Sweet-Tempered,Lively,Alert,Playful,Happy" , "Friendly,Alert,Dignified,Intelligent,Calm" , "Aloof,Loyal,Independent,Quiet" , "Affectionate,Loyal,Dignified,Gentle,Calm,Great-hearted" , "Outgoing,Sociable,Trusting,Joyful,EvenTempered,Merry" , "Affectionate,Lively,Playful,Intelligent,Trainable,Vocal" , "Outgoing,Friendly,Energetic,Playful,Sensitive,Intelligent,Active" , "Friendly,Affectionate,Cheerful,Loyal,Tolerant,Protective" , "Kind,Energetic,Independent,Adaptable,Intelligent,Bossy" , "Affectionate,Cheerful,Alert,Intelligent,Attentive,Active" , "Alert,Reserved,Intelligent,EvenTempered,Watchful,Calm" , "Docile,Cautious,Sociable,Sensitive,Adaptable,Familial" , "Friendly,Keen,Faithful,Calm,Courageous" , "Spirited,Lively,Intelligent,Loving,EvenTempered,Familial" , "Alert,Loyal,Obedient,Curious,Confident,Intelligent,Watchful,Courageous" , "Boisterous,Bold,Affectionate,Intelligent,Cooperative,Trainable" , "StrongWilled,Kind,Loyal,Intelligent,Dominant,Powerful" , "Spirited,Agile,Loyal,Gentle,Active,Courageous" , "Intelligent,Kind,Reliable,Friendly,Trustworthy,Confident" , "Fearless,Alert,Loyal,Confident,Gay,Eager" , "Friendly,Devoted,Reserved,Gentle,Confident,Loving" , "StrongWilled,Fearless,Affectionate,Patient,Gentle,Confident" , "Affectionate,Athletic,Gentle,Intelligent,Quiet,EvenTempered" , "Outgoing,Friendly,Cheerful,Sweet-Tempered,Tolerant,Active" , "Affectionate,Responsive,Playful,Companionable,Gentle,Intelligent" , "Affectionate,Energetic,Lively,Independent,Playful,Companionable" , "Sweet-Tempered,Loyal,Dignified,Patient,Thoughtful,Generous" , "Mischievous,Affectionate,Agile,Athletic,Companionable,Intelligent" , "Alert,Loyal,Independent,Intelligent,Loving,Cat-like" , "Agile,Obedient,Playful,Quick,Sturdy,Bright" , "Steady,Fearless,Affectionate,Independent,Gentle,Calm" , "Clownish,Loyal,Patient,Independent,Intelligent,Protective" , "Kind,Outgoing,Agile,Gentle,Intelligent,Trusting,EvenTempered" , "Keen,Loyal,Companionable,Loving,Active,Trainable" , "Obedient,Fearless,Loyal,Companionable,Adaptable,Loving" , "Steady,Fearless,Friendly,Devoted,Assertive,Spirited,Energetic,Lively,Alert,Obedient,Playful,Intelligent" , "Playful,Docile,Fearless,Affectionate,Sweet-Tempered,Lively,Responsive,Easygoing,Gentle,Intelligent,Active" , "Fearless,Friendly,Spirited,Alert,Obedient,Intelligent" , "Sweet-Tempered,Gentle,Trainable" , "Self-confidence,Fearless,Spirited,Companionable,Happy,Lovable" , "Hardy,Friendly,Energetic,Alert,Intelligent,Happy" , "Tenacious,Outgoing,Friendly,Bold,Playful,Protective" , "Affectionate,Sociable,Playful,Intelligent,Active,Trainable" , "Bold,Alert,Loyal,Intelligent" , "Docile,Clever,Charming,Stubborn,Sociable,Playful,Quiet,Attentive" , "Affectionate,Energetic,Independent,Companionable,Familial,Unflappable" , "StrongWilled,Mischievous,Loyal,Dignified,Sensitive,Intelligent" , "Steady,Good-natured,Fearless,Devoted,Alert,Obedient,Confident,Self-assured,Calm,Courageous" , "Stubborn,Friendly,Sociable,Lively,Alert,Playful" , "Fearless,Agile,Curious,Independent,Confident,Faithful" , "Docile,Friendly,Dignified,Gentle" , "Clever,Spunky,Outgoing,Friendly,Affectionate,Lively,Alert,Loyal,Independent,Playful,Gentle,Intelligent,Happy,Active,Courageous" , "Friendly,Responsive,Inquisitive,Alert,Quick,Joyful" , "Affectionate,Spirited,Energetic,Playful,Intelligent,Faithful" , "Trainable,Diligent,Affectionate,Loyal,Athletic,Intelligent" , "Affectionate,Energetic,Loyal,Gentle,Quiet" , "Steady,Aloof,Stubborn,Energetic,Alert,Intelligent,Powerful,Fast"]
dogImage = ["https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg" , "https://cdn2.thedogapi.com/images/tChrH8dDJ.jpg" , "https://cdn2.thedogapi.com/images/PG8UPLSVU.jpg" , "https://cdn2.thedogapi.com/images/SyfsC19NQ_1280.jpg" , "https://cdn2.thedogapi.com/images/36TXlWMDf.jpg" , "https://cdn2.thedogapi.com/images/33mJ-V3RX.jpg" , "https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg" , "https://cdn2.thedogapi.com/images/GhtSdrW29.jpg" , "https://cdn2.thedogapi.com/images/EB8A5HQHX.jpg" , "https://cdn2.thedogapi.com/images/uISezUGDV.jpg" , "https://cdn2.thedogapi.com/images/HkC31gcNm_1280.png" , "https://cdn2.thedogapi.com/images/SkmRJl9VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/BJT0Jx5Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/Hyq1ge9VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/B1-llgq4m_1280.jpg" , "https://cdn2.thedogapi.com/images/SkvZgx94m_1280.jpg" , "https://cdn2.thedogapi.com/images/H1dGlxqNQ_1280.jpg" , "https://cdn2.thedogapi.com/images/BkMQll94X_1280.jpg" , "https://cdn2.thedogapi.com/images/Syd4xxqEm_1280.jpg" , "https://cdn2.thedogapi.com/images/HJQ8ge5V7_1280.jpg" , "https://cdn2.thedogapi.com/images/ByK8gx947_1280.jpg" , "https://cdn2.thedogapi.com/images/r1f_ll5VX_1280.jpg" , "https://cdn2.thedogapi.com/images/B1KdxlcNX_1280.jpg" , "https://cdn2.thedogapi.com/images/S1fFlx5Em_1280.jpg" , "https://cdn2.thedogapi.com/images/HJAFgxcNQ_1280.jpg" , "https://cdn2.thedogapi.com/images/Skdcgx9VX_1280.jpg" , "https://cdn2.thedogapi.com/images/rJxieg9VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/HyOjge5Vm_1280.jpg" , "https://cdn2.thedogapi.com/images/HJOpge9Em_1280.jpg" , "https://cdn2.thedogapi.com/images/rkZRggqVX_1280.jpg" , "https://cdn2.thedogapi.com/images/Byd0xl5VX_1280.jpg" , "https://cdn2.thedogapi.com/images/ry1kWe5VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/ryHJZlcNX_1280.jpg" , "https://cdn2.thedogapi.com/images/S13yZg5VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/rkVlblcEQ_1280.jpg" , "https://cdn2.thedogapi.com/images/HJWZZxc4X_1280.jpg" , "https://cdn2.thedogapi.com/images/r1ifZl5E7_1280.jpg" , "https://cdn2.thedogapi.com/images/Sk7Qbg9E7_1280.jpg" , "https://cdn2.thedogapi.com/images/r15m-lc4m_1280.jpg" , "https://cdn2.thedogapi.com/images/SyXN-e9NX_1280.jpg" , "https://cdn2.thedogapi.com/images/BJcNbec4X_1280.jpg" , "https://cdn2.thedogapi.com/images/r1rrWe5Em_1280.jpg" , "https://cdn2.thedogapi.com/images/HJRBbe94Q_1280.jpg" , "https://cdn2.thedogapi.com/images/B1pDZx9Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/Sypubg54Q_1280.jpg" , "https://cdn2.thedogapi.com/images/ry8KWgqEQ_1280.jpg" , "https://cdn2.thedogapi.com/images/rkeqWgq4Q_1280.jpg" , "https://cdn2.thedogapi.com/images/HkRcZe547_1280.jpg" , "https://cdn2.thedogapi.com/images/SyviZlqNm_1280.jpg" , "https://cdn2.thedogapi.com/images/SkJ3blcN7_1280.jpg" , "https://cdn2.thedogapi.com/images/S1nhWx94Q_1280.jpg" , "https://cdn2.thedogapi.com/images/H1QyMe5EQ_1280.jpg" , "https://cdn2.thedogapi.com/images/Hk0Jfe5VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/S1VWGx9Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/SkJfGecE7_1280.jpg" , "https://cdn2.thedogapi.com/images/S1KMGg5Vm_1280.jpg" , "https://cdn2.thedogapi.com/images/B1u4zgqE7_1280.jpg" , "https://cdn2.thedogapi.com/images/SJyBfg5NX_1280.jpg" , "https://cdn2.thedogapi.com/images/SJqBMg5Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/H1NIzlcV7_1280.jpg" , "https://cdn2.thedogapi.com/images/H1oLMe94m_1280.jpg" , "https://cdn2.thedogapi.com/images/HJ7Pzg5EQ_1280.jpg" , "https://cdn2.thedogapi.com/images/SJ5vzx5NX_1280.jpg" , "https://cdn2.thedogapi.com/images/B1Edfl9NX_1280.jpg" , "https://cdn2.thedogapi.com/images/B12uzg9V7_1280.png" , "https://cdn2.thedogapi.com/images/ryNYMx94X_1280.jpg" , "https://cdn2.thedogapi.com/images/B1IcfgqE7_1280.jpg" , "https://cdn2.thedogapi.com/images/rkXiGl9V7_1280.jpg" , "https://cdn2.thedogapi.com/images/S1osGeqVm_1280.jpg" , "https://cdn2.thedogapi.com/images/Hyd2zgcEX_1280.jpg" , "https://cdn2.thedogapi.com/images/SJAnzg9NX_1280.jpg" , "https://cdn2.thedogapi.com/images/r1H6feqEm_1280.jpg" , "https://cdn2.thedogapi.com/images/S1GAGg9Vm_1280.jpg" , "https://cdn2.thedogapi.com/images/Bko0fl547_1280.jpg" , "https://cdn2.thedogapi.com/images/BykZ7ecVX_1280.jpg" , "https://cdn2.thedogapi.com/images/B1uW7l5VX_1280.jpg" , "https://cdn2.thedogapi.com/images/ryzzmgqE7_1280.jpg" , "https://cdn2.thedogapi.com/images/ByrmQlqVm_1280.jpg" , "https://cdn2.thedogapi.com/images/SJp7Qe5EX_1280.jpg" , "https://cdn2.thedogapi.com/images/B1SV7gqN7_1280.jpg" , "https://cdn2.thedogapi.com/images/SJIUQl9NX_1280.jpg" , "https://cdn2.thedogapi.com/images/Sk4DXl54m_1280.jpg" , "https://cdn2.thedogapi.com/images/B1ADQg94X_1280.jpg" , "https://cdn2.thedogapi.com/images/SkJj7e547_1280.jpg" , "https://cdn2.thedogapi.com/images/rJ6iQeqEm_1280.jpg" , "https://cdn2.thedogapi.com/images/Byz6mgqEQ_1280.jpg" , "https://cdn2.thedogapi.com/images/B1i67l5VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/HyJvcl9N7_1280.jpg" , "https://cdn2.thedogapi.com/images/HJMzEl5N7_1280.jpg" , "https://cdn2.thedogapi.com/images/By9zNgqE7_1280.jpg" , "https://cdn2.thedogapi.com/images/r1xXEgcNX_1280.jpg" , "https://cdn2.thedogapi.com/images/S1T8Ee9Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/SyBvVgc47_1280.jpg" , "https://cdn2.thedogapi.com/images/SkNjqx9NQ_1280.jpg" , "https://cdn2.thedogapi.com/images/BkrJjgcV7_1280.jpg" , "https://cdn2.thedogapi.com/images/ByzGsl5Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/HJHmix5NQ_1280.jpg" , "https://cdn2.thedogapi.com/images/HJf4jl9VX_1280.jpg" , "https://cdn2.thedogapi.com/images/r1o0jx9Em_1280.jpg" , "https://cdn2.thedogapi.com/images/SyU12l9V7_1280.jpg"]


global dogBreeds
def Temper_Image(): #Finds dog image and temperment.....

    # finds image
    print("What Dog Breed Do You Want?")
    try:
        dog = input("What Dog Breed Do You Want?")
        x = dogBreeds.index(dog)
    except:
        print("ERROR! THIS DOG IS NOT ON THE LIST! TRY ANOTHER BREED!")

    y = dogImage[x]
    open_image(y)

    # finds temperment
    z = dogTemper[x]
    print("""
""" + "The temperments are: " + str(z) + """
""")

#Temper_Image()




#LIST FOR GOAL 2:
BredFors = ["smallrodenthunting" , "lapdog Coursingandhunting Badger" , "otterhunting Sheepguarding Huntingbears Guarding Sledpulling Haulingheavyfreight" , "Sledpulling Circusperformer Foxhunting" , "scenthound Fighting Birdflushingandretrieving Livestockherding Farmdog" , "Cattleherding Sheepherding Livestockguardian" , "hunting Hunting Huntingonfoot. Rabbit" , "harehunting Boarherding" , "hunting" , "guarding Killingrat" , "badger" , "othervermin Stockherding Guarding" , "Drafting" , "Policework. Draftwork Huntingraccoons" , "nighthunting Trailing Huntingwithasuperiorsenseofsmell. Guardingthehomestead" , "farmwork. Foxbolting" , "ratting Ratting" , "Companionship Cattleherding Bull-baiting" , "guardian Turkeyretrieving Versatilegundog Herding" , "guardingsheep Pointing" , "retrieving Estateguardian Boltingofotter" , "foxes" , "othervermin Companion" , "guarddog" , "andhunter Cattledroving Drivinglivestock Guarddogs" , "defendingsheepfrompredators" , "mainlywolves" , "jackalsandbears Flushingsmallbirds" , "companion Ratting" , "lapdog" , "curio Sledpulling Guardian" , "cartpulling" , "hunting Birdflushing" , "retrieving HuntingtheAmericanwoodcock Accompanyingladiesonlongseavoyages" , "rattersonboardship. Carriagedog-trotalongsidecarriagestoprotecttheoccupantsfrombanditryorotherinterference Big-gamehunting Herding&guardinglivestock" , "farmwatchdog Birdflushing" , "retrieving Companionship Birdflushing" , "retrieving Herdingreindeer Watchdog" , "Huntingverminonthefarm. Herding" , "Guarddog Generalhunting Herding" , "guarding Ridthehomeandfarmofvermin" , "andhuntbadgerandfox Retrieving Findandpointgamebirds Hunting&holdingboars" , "Guardian Sheepguardian Coursinghares Huntingharesbytrailingthem Companionship Birdsetting" , "retrieving Coursingwolves" , "elk Lapdog Lapdog Bargewatchdog Sheepguardian Guardian" , "huntinglargegame Waterretrieving WaterretrievaldoginthemarshesofRomagna Guardian" , "appearance. Guardinginsidethehome" , "companion Lapdog Ratting Allpurposewaterdog" , "fishingaid Ratting" , "foxbolting Lapdog DrivingstocktomarketinnorthernWales Huntingrabbits Huntingbig-gamelikeBoar. Lapdog Huntingraccoon" , "deer" , "bear" , "andcougar. Biggamehunting" , "guarding Cattledrover" , "guardian" , "draft Herdingreindeer" , "guardian" , "draft Bargewatchdog Coursingdeer Lapdog Smallverminhunting" , "companionship Verminhunting" , "guarding" , "all-aroundfarmhelper Herdingflocksofsheepandgoatsfromonepasturetoanother Pointingandtrailing Largegametrailingandversatilegundog"]
BredFor = [item.lower() for item in BredFors]

global dogBreeds
def Breed_Purpose():
    print("What is your dog user-specified purpose (e.g., circus, companion, sled, hunt, farm, guard etc...)?")

    reasoning = input("What is your dog user-specified purpose (e.g., circus, companion, sled, hunt, farm, guard etc...)?")
    try:
        for i in range(len(BredFor)):
            if reasoning in BredFor[i]:
                x = i
                z = dogBreeds[x]
                print("""
""" + "Dog Purpose: " + str(reasoning))
                print("""
""" + "Recommend: " + str(z) + """
""")
    except:
        if reasoning not in BredFor:
            print("ERROR! THIS PURPOSE IS NOT LISTED! TRY ANOTHER!")



#Breed_Purpose()



#GOAL 3: MENU
def Dogmenu():
    print("WELCOME TO THE DOG MENU!")
    print("WE HELP YOU FIND YOUR PERFECT DOG BREED MATCH ACCORDING TO YOUR PREFERENCES!")
    print("""
HERE ARE THE OPTIONS:
1. DOG SIZE
2. DOG TEMPERMENT + IMAGE
3. DOG SPECIFIED PURPOSE
4. QUIT""")
    print("""
WHAT'S YOUR CHOICE?""")

    while True:
        choice = int(input("WHAT'S YOUR CHOICE?"))
        if choice == 1:
            dogSize()

        if choice == 2:
            Temper_Image()

        if choice == 3:
            Breed_Purpose()

        if choice == 4:
            print("Bye!")
            break

Dogmenu()









