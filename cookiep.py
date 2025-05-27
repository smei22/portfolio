import random
import time

#Lists
CookieName = ["OatmealRaisinCookies" , "SugarCookies" , "ChocolateChipCookies" , "SnickerdoodlesCookies" , "PeanutButterCookies" , "ShortbreadCookies" , "ButterCookies" , "MacaronCookies" , "BiscottiCookies" , "GingerSnapCookies" , "RussianTeaCakeCookies" , "ThumbPrintCookies" , "MeringueCookies" , "FortuneCookies" , "CrinkleCookies" , "PinwheelCookies" , "WaferCookies" , "IceboxCookies" , "GingerbreadCookies" , "MacaroonCookies"]
CookieTexture = ["Chewy" , "Soft" , "Chewy,Crispy" , "Soft,Chewy" , "Soft,Chewy" , "Soft,Tender,Melty" , "Crispy" , "Delicate,Chewy" , "Hard,Crunchy" , "Crispy,Soft,Chewy" , "Tender,Soft" , "Tender,Soft" , "Light,Airy,Crispy" , "Crispy" , "Fudgy,Chewy" , "Soft" , "Soft" , "Crunchy,Crispy" , "Soft,Crispy" , "Crispy,Soft,Chewy"]
CookieBakeTime = ["11" , "11" , "8" , "10" , "8" , "9" , "8" , "12" , "30" , "10" , "12" , "8" , "60" , "10" , "9" , "10" , "15" , "8" , "7" , "12"]
CookieIngredient = ["APflour,BakingSoda,BakingPowder,Salt,UnsaltedButter,GranulatedSugar,Eggs,VanillaExtract,Oats,Raisin" , "APflour,BakingPowder,Salt,UnsaltedButter,GranulatedSugar,Egg,VanillaExtract,AlmondExtract,Icing,Buttercream,Sprinkles" , "SaltedButter,BrownSugar,GranulatedSugar,Vanilla,Egg,APflour,BakingSoda,BakingPowder,Salt,ChocolateChip" , "UnsaltedButter,GranulatedSugar,Egg,VanillaExtract,APflour,CreamOfTarTar,BakingSoda,Salt,Cinnamon," , "PeanutButter,UnsaltedButter,GranulatedSugar,BrownSugar,Egg,Milk,VanillaExtract,APflour,BakingPowder,Salt" , "UnsaltedButter,PowderedSugar,VanillaExtract,APflour,Cornstarch,Salt" , "UnsaltedButter,GranulatedSugar,Egg,VanillaExtract,APflour,Salt" , "AlmondFlour,GranulatedSugar,VanillaExtract,Tartar,UnsaltedButter,Egg,Water,Salt" , "UnsaltedButter,Sugar,Eggs,VanillaExtract,APflour,BakingPowder,Salt,Almonds,ChocolateChips,Wafers" , "CinnamonSugar,APflour,GroundGinger,BakingSoda,GroundCinnamon,Salt,Butter,GranulatedSugar,Egg,Molasses" , "UnsaltedButter,VanillaExtract,APflour,PowderedSugar,Walnuts" , "Egg,UnsaltedButter,BrownSugar,APflour,VanillaExtract,Salt,Walnuts,Jam" , "Egg,Tartar,Salt,GranulatedSugar,VanillaExtract" , "Egg,GranulatedSugar,UnsaltedButter,VanillaExtract,AlmondExtract,APflour,Water" , "VegetableOil,Chocolate,VanillaExtract,Egg,Apflour,BakingPowder,Salt,PowderedSugar" , "APflour,BakingPowder,Salt,UnsaltedButter,GranulatedSugar,Egg,AlmondExtract,FoodColoring,Sprinkles" , "APflour,Salt,UnsaltedButter,Egg,VanillaExtract" , "UnsaltedButter.BrownSugar,Egg,VanillaExtract,APflour,BakingSoda,Tartar,Walnuts" , "APflour,BakingPowder,BakingSoda,Salt,GroundGinger,GroundCinnamon,GroundCloves,UnsaltedButter,BrownSugar,Egg,Molasses,VanillaExtract,LemonZest" , "EggWhites,GranulatedSugar,Coconut"]
CookieLinks = ["https://www.food.com/recipe/oatmeal-raisin-cookies-35813" , "https://sallysbakingaddiction.com/best-sugar-cookies/#tasty-recipes-67590" , "https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/" , "https://www.modernhoney.com/the-best-snickerdoodle-cookie-recipe/" , "https://www.allrecipes.com/recipe/11024/joeys-peanut-butter-cookies/" , "https://sugarspunrun.com/best-shortbread-cookie-recipe/" , "https://www.allrecipes.com/recipe/10011/butter-cookies-ii/" , "https://preppykitchen.com/french-macarons/" , "https://sugarspunrun.com/biscotti/" , "https://www.allrecipes.com/recipe/10365/grandmas-gingersnap-cookies/" , "https://www.allrecipes.com/recipe/10192/russian-tea-cakes-i/" , "https://www.allrecipes.com/recipe/9618/thumbprint-cookies-i/" , "https://sugarspunrun.com/meringue-cookie-recipe/comment-page-1/" , "https://www.allrecipes.com/recipe/58640/fortune-cookies-so-easy/" , "https://www.bettycrocker.com/recipes/chocolate-crinkle-cookies-recipe/941e22b3-9a48-4fb1-bdb0-27479e76d484" , "https://www.delish.com/holiday-recipes/christmas/a30210803/christmas-pinwheel-cookies-recipe/" , "https://www.delish.com/cooking/recipe-ideas/a25482462/wafer-cookies-recipe/" , "https://www.tasteofhome.com/recipes/icebox-cookies/" , "https://www.food.com/recipe/the-most-wonderful-gingerbread-cookies-80156" , "https://www.goodto.com/recipes/coconut-macaroon"]
CookiePictures = ["https://tinyurl.com/3zdz88wx" , "https://tinyurl.com/yh7ve3cy" , "https://tinyurl.com/jh6xpym4" , "https://tinyurl.com/2d5vt2sa" , "https://tinyurl.com/54jjsshc" , "https://tinyurl.com/mvam7sfr" , "https://tinyurl.com/2np8xzff" , "https://tinyurl.com/4tyvpzf6" , "https://tinyurl.com/f5v9cwjs" , "https://tinyurl.com/2842anca" , "https://tinyurl.com/4ejjh4t9" , "https://tinyurl.com/46tsm9xw" , "https://tinyurl.com/3eam47ks" , "https://tinyurl.com/m2vd277v" , "https://tinyurl.com/4vvpfwtf" , "https://tinyurl.com/mwx7ea55" , "https://tinyurl.com/7am3dua7" , "https://tinyurl.com/2aex6xe22" , "https://tinyurl.com/3rax3y6n" , "https://tinyurl.com/yc6pmnmf"]
CookieRating = ["5/5" , "4.7/5" , "5/5" , "5/5" , "4.5/5" , "4.9/5" , "4.5/5" , "4.97/5" , "4.96/5" , "4.8/5" , "4.7/5" , "4.6/5" , "4.94/5" , "3.8/5" , "4.5/5" , "4/5" , "5/5" , "4/5" , "4.5/5" , "4/5"]
CookieWebsite = ["Food.com" , "Sally's" , "Baking" , "Addiction" , "Joy" , "Food" , "Sunshine" , "Modern" , "Honey" , "Allrecipes" , "Sugar" , "Spun" , "Run" , "Allrecipes" , "Preppy" , "Kitchen" , "Sugar" , "Spun" , "Run" , "Allrecipes" , "Allrecipes" , "Allrecipes" , "Sugar" , "Spun" , "Run" , "Allrecipes" , "Betty" , "Crocker" , "Delish" , "Delish" , "Taste" , "Of" , "Home" , "Food.com" , "Goodto"]

#Case-Insensitive List
Name = [item.lower() for item in CookieName]  # This Case sensitive list code is taken from https://stackoverflow.com/questions/1801668/convert-a-list-with-strings-all-to-lowercase-or-uppercase
Texture = [item.lower() for item in CookieTexture]
Ingredient = [item.lower() for item in CookieIngredient]

# Opening Image Code
from PIL import Image
import requests
from io import BytesIO
def open_image(url):                    # This code for printing an image in the interactive window is taken from the Dog Breeds Assignment Practice learned during class.
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


#-----------------------------------------------------------------


#Intro

def intro():
    print("""Welcome To Cookie Generator!
This Program Will Ask You Some Questions To Help Generate The Perfect Cookie Recipe For You!""")
    time.sleep(1)  # This code to delay is from https://realpython.com/python-sleep/


intro()


#-----------------------------------------------------------------


#Filtering Texture

filteredTexture = []
global Texture
global CookieName
global filteredTexture

def TextureOP():
    print("-------------------------------------------------")
    print("What Do You Want Your Cookie Texture To Be?")
    print("Cookie Textures: Chewy, Soft, Crispy, Tender, Hard, Crunchy")
    Qtexture = input("What Do You Want Your Cookie Texture To Be?").casefold()

    try:
        for i in range(len(Texture)):
            if Qtexture in Texture[i]:
                x = i
                z = CookieName[x]

                filteredTexture.append(z)


        print("""
""" + "Cookie Texture: " + str(Qtexture))
        time.sleep(1)
        print("""
""" + "Recommend: " + """
""")
        print(*filteredTexture, sep='\n')
        print("""
""")

    except:
        if Qtexture not in Texture:
            print("ERROR! THIS TEXTURE IS NOT LISTED! TRY ANOTHER!")


#-----------------------------------------------------------------



filteredIngredient = []
global Ingredient
global CookieName
global filteredIngredient

def IngredientOP(filteredIngredient):
    print("-------------------------------------------------")
    print("What Do You Want Your Ingredients To Be?")
    print("""Cookie Ingredients: APflour, UnsaltedButter, GranulatedSugar,
BakingSoda, Raisin, Sprinkles, ChocolateChip, Cinnamon, PeanutButter, etc...""")
    print("""
Make Sure There Is No Space Between Ingredient Names!""")
    QIngredient = input("What Ingredients Do You Want Your Cookie To Have?").casefold()

    try:
        for i in range(len(Ingredient)):
            if QIngredient in Ingredient[i]:
                x = i
                z = CookieName[x]

                filteredIngredient.append(z)
    except:
        if QIngredient not in Ingredient[i]:
            print("ERROR! THIS INGREDIENT IS NOT LISTED! TRY ANOTHER!")


    print("""
""" + "Cookie Ingredient: " + str(QIngredient))
    time.sleep(1)
    print("""
""" + "Recommend: " + """
""")
    print(*filteredIngredient, sep='\n')
    print("""
""")


#-----------------------------------------------------------------


#random generated cookie
global CookieName
global Texture
global CookieBakeTime
global CookieIngredient
global CookieLinks
global CookiePictures
global CookieRating
global CookieWebsite

def randomCookie():
    print("-------------------------------------------------")
    print("This Is A Tool To Help You Generate A Random Cookie Recipe!")
    print("""
Press 1 To Roll!""")
    print("Press 0 To Opt Out!")


    while True:
        roll = int(input("Ready To Roll?"))

        if roll == 1:
            x = random.randint(0, len(CookieName) - 1)  # this code for randomization is from https://stackoverflow.com/questions/306400/how-can-i-randomly-select-choose-an-item-from-a-list-get-a-random-element
            y = CookiePictures[x]

            time.sleep(1)
            print("""
""" + CookieName[x] + """
""" + "--------------------------------------")
            print("""
Cookie Texture: """ + str(Texture[x]))
            print("Bake Time (mins): " + str(CookieBakeTime[x]))
            print("Cookie Ingredients: " + str(Ingredient[x]))
            print("Cookie Picture: ")
            open_image(y)
            print("Cookie Recipe Rating: " + str(CookieRating[x]))
            print("Cookie Website Name: " + str(CookieWebsite[x]))
            print("Cookie Recipe Link: " + str(CookieLinks[x]))


        if roll == 0:
            break


#-----------------------------------------------------------------


#Search Recipe

global CookieName
global Name
global CookieTexture
global CookieBakeTime
global CookieIngredient
global CookieLinks
global CookiePictures
global CookieRating
global CookieWebsite
global Texture


def SearchRecipe():
    print("""
""" + "-------------------------------------------------")
    print("What Cookie Are You Looking For?")
    print("Cookies: ChocolateChipCookies, OatmealRaisinCookies, ButterCookies, etc...")
    print("Search Format: ____Cookies. MAKE SURE THERE IS NO SPACE BETWEEN WORDS!")
    Cookie = input("What Cookie Recipe Do You Want To Search For?").casefold()

    try:
        for i in range(len(Name)):
            if Cookie in Name[i]:
                x = i
                y = CookiePictures[x]

                print("""
""" + CookieName[x] + """
""" + "-------------------")
                time.sleep(1)
                print("""
Cookie Texture: """ + str(CookieTexture[x]))
                print("Bake Time (mins): " + str(CookieBakeTime[x]))
                print("Cookie Ingredients: " + str(CookieIngredient[x]))
                print("Cookie Picture: ")
                open_image(y)
                print("Cookie Recipe Rating: " + str(CookieRating[x]))
                print("Cookie Website Name: " + str(CookieWebsite[x]))
                print("Cookie Recipe Link: " + str(CookieLinks[x]))

                print("""
""" + "Selected Cookie: " + str(CookieName[x]))

    except:
        if Cookie not in Name:
            print("ERROR! THIS COOKIE IS NOT LISTED! TRY ANOTHER!")


#-----------------------------------------------------------------


# Menu

global filteredIngredient

def CookieMenu():
    print("""
------------------------
""" + "THIS IS THE COOKIE MENU!")
    time.sleep(1)
    print("WE HELP YOU FIND YOUR PERFECT COOKIE RECIPE ACCORDING TO YOUR PREFERENCES!")
    time.sleep(1)
    print("""
HERE ARE THE OPTIONS:
1. COOKIE TEXTURE PREFERENCES
2. COOKIE INGREDIENT PREFERENCES
3. RANDOM COOKIE GENERATOR
4. SEARCH COOKIE RECIPE
5. QUIT""")
    print("""
WHAT'S YOUR CHOICE?""")
    while True:
        choice = int(input("WHAT'S YOUR CHOICE?"))
        time.sleep(1)
        if choice == 1:
            print("""
""" + "Choice: "+ str(choice))
            TextureOP()

        if choice == 2:
            print("""
""" + "Choice: "+ str(choice))
            IngredientOP(filteredIngredient)

        if choice == 3:
            print("""
""" + "Choice: "+ str(choice))
            randomCookie()

        if choice == 4:
            print("""
""" + "Choice: "+ str(choice))
            SearchRecipe()

        if choice == 5:
            print("""
""" + "Choice: "+ str(choice))
            print("""
""" + "----------------------------------" +
"""
""" + "Here Are The Cookie Recipe Credits:")
            print("""
""" +
"""Food.Com: Bev I Am, Sally's Baking Addiction: Sally, Joy Food Sunshine: Laura, Modern Honey: Melissa Stadler, AllRecipes: P Weiss, SugarSpunRun: Sam,
AllRecipes: Ceil Wallace, Preppy Kitchen: John Kanell, AllRecipes: Marie Ayers, King Arthur Baking: PJ Hamel, AllRecipes: C Keith, AllRecipes: BABYCAKES291,
BettyCrocker: N.A., Delish: Makinze Gore, Taste Of Home: Kelli Acciardo, Food.com: gingerkitten D, GoodTo: Jessica Dady""" )
            print("""
Bye! Visit Again Next Time!""")

            break

CookieMenu()
