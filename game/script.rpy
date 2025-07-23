# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define harry = Character("Harry", color="#ffd700")

define ron = Character("Ron", color="#fc6603")

define hermione = Character("Hermione", color="#9e6f4f")

define ginny = Character("Ginny", color="#fc6603")

define luna = Character("Luna", color="#ce42f5")

define neville = Character("Neville", color="#ffc26e")

define sirius = Character("Sirius", color="#57826d")

define draco = Character("Draco", color="#42f59e")

define fred = Character("Fred", color="#fc6603")

define george = Character("George", color="#fc6603")

define fred_and_george = Character("{color=#fc6603}Fred{/color} {color=#fc6603}and{/color} {color=#fc6603}George{/color}")

define mcgonagall = Character("Prof. Mcgonagall", color="#639942")

define hagrid = Character("Hagrid", color="#a35a00")

define umbridge = Character("Prof. Umbridge", color="#f065b1")

define pravati = Character("Pravati", color="#f5426f")

define harry_and_pravati = Character("{color=#ffd700}Harry{/color} {color=#ffffff}and{/color} {color=#f5426f}Pravati{/color}")

define padma = Character("Padma", color="#42f5d1")

define filch = Character("Argus Filch", color="#768c50")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "image.png" to the images
    # directory.

    # These display lines of dialogue.

    # "You've created a new Ren'Py game."

    # "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    python:
        show_title = True

    jump book_moments_menu

    return