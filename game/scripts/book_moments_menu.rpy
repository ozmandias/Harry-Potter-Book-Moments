image hogwarts_map_2014:
    "hogwarts_map_2014.jpeg",
    zoom 1

image map_of_hogwarts:
    "map_of_hogwarts.jpg",
    zoom 1

label book_moments_menu:
    scene black_background

    show map_of_hogwarts_resize at truecenter

    if show_title:
        "Harry Potter Book Moments"
        python:
            show_title = False

    menu:
        "Select any book..."

        "Harry Potter and the Philosopher's Stone":
            "None at the moment..."
            jump book_moments_menu
        "Harry Potter and the Chamber of Secrets":
            "None at the moment..."
            jump book_moments_menu
        "Harry Potter and the Prisoner of Azkaban":
            "None at the moment..."
            jump book_moments_menu
        "Harry Potter and the Goblet of Fire":
            "None at the moment..."
            jump book_moments_menu
        "Harry Potter and the Order of the Phoenix":
            # "None at the moment..."
            # jump book_moments_menu
            jump order_of_the_phoenix_menu
        "Harry Potter and the Half-Blood Prince":
            jump half_blood_prince_menu
        "Harry Potter and the Deathly Hallows":
            "None at the moment..."
            jump book_moments_menu