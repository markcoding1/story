#renpy script

init python: 
    class MainChar:
        def __init__(self, character, name, speed):
            self.c = character
            self.name = name
            self.speed = speed

        def increase_speed (self):
            self.speed += 1

label start:

    $ t = MainChar(Character("Thomas"), "Thomas", 20)
    $ c = OtherChar(Character("Chloe"), "Chloe", 7)

    scene bg room
    show eileen happy
    t.c "You've created a new Ren'Py game."
    t.c "Once you add a story, pictures, and music, you can release it to the world!"
    t.c "Do you like this post?"

    $ t.c("My speed is "  + str(t.speed))

    t.c "i'll now add some speed"
    $ t.increase_speed()
    $ t.c("My speed is "  + str(t.speed))

    t.c "i'll now add MORE speed"
    $ t.increase_speed()
    $ t.c("My speed is now "  + str(t.speed))

    c.c "hi, i'm Chloe"
    $ c.c("I like Thomas " + str(c.like) + " out of ten")
    c.c "Now I like him more!"
    $ c.increase_like()
    $ c.c("I like Thomas " + str(c.like) + " out of ten")

    #test time periods
    c.c "The current time is [time_period] on [weekdays[weekday_index]], [day] [month_names[month]] Year:[year]."
    c.c "lets advance time"
    $ next_time_period()
    c.c "The current time is [time_period] on [weekdays[weekday_index]], [day] [month] Year:[year]."

    return
