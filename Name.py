# Sharon Mei
# name generator

print("Welcome to Fine Dining Generator!")
print("Answer the questions to find out the Dish You Will Eat!")

answer =  input("Meat or Vegetable?")
if answer == "meat":
    answer = input("Corn Oil or Baby Oil?")
    if answer == "baby oil":
        answer = input("Cherry or Grape?")
        if answer == "cherry":
            print("Your Dish is Unethical Cherry Meat Pie!")
        else:
            print("Your Dish is Unethical Steak With Grape Jam!");
    if answer == "corn oil":
        answer = input("Blueberry or Lemon?")
        if answer == "blueberry":
            print("Your Dish is Blueberry Corned Beef Muffin!")
        else:
            print("Your Dish is Corned Beef Lemon Tarts!")



if answer == "vegetable":
    answer = input("Gasoline or Olive?")
    if answer == "gasoline":
        answer = input("Orange or Kiwi?")
        if answer == "orange":
            print("Your Dish is Carcinogenic Orange Honey Glazed Asparagus!")
        else:
            print("Your Dish is Carcinogenic Kiwi Broccoli Smoothie!")

    if answer == "olive":
        answer = input("Banana or Apple?")
        if answer == "apple":
            print("Your Dish is Apple Curry!")
        else:
            print("Your Dish is Healthy Banana Smoothie!")
