import kivy
import random
from libdw import sm
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.checkbox import CheckBox
from kivy.core.audio import SoundLoader

#global variable so that it is easily referenced by each class
# and so that a new obj wont be created each the time
g_player = None

sound = SoundLoader.load('Forgoten_tombs.wav')

if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)
    sound.play()

#restart function in order to reset all the class variables

def restart(self):
    global g_player
    self.manager.screens[2].dates = []
    self.manager.screens[3].points = str("0")
    self.manager.screens[2].symptoms = str("No Symptoms")
    self.manager.screens[2].week = str("1")
    g_player.points = 0
    print(g_player.points)
    print("all reset")

class StoryWindow(Screen):
    pass

class InsWindow(Screen):
    pass

class CalWindow(Screen):
    week = StringProperty('1')
    '''An object property allows us to create a reference to widgets from 
    within a .kv file from our python script. Also since it sets a 
    get and set method for the attribute it allows the obj to be changed. 
    Eg week is not a static string anymore, the value can be changed as the week go by.'''
    mon = ObjectProperty(None)
    tue = ObjectProperty(None)
    wed = ObjectProperty(None)
    thur = ObjectProperty(None)
    fri = ObjectProperty(None)
    sat = ObjectProperty(None)
    sun = ObjectProperty(None)
    mon_doc = ObjectProperty(None)
    tue_doc = ObjectProperty(None)
    wed_doc = ObjectProperty(None)
    thur_doc = ObjectProperty(None)
    fri_doc = ObjectProperty(None)
    sat_doc = ObjectProperty(None)
    sun_doc = ObjectProperty(None)
    mons = ObjectProperty(None)
    tues = ObjectProperty(None)
    weds = ObjectProperty(None)
    thurs = ObjectProperty(None)
    fris = ObjectProperty(None)
    sats = ObjectProperty(None)
    suns = ObjectProperty(None)

    def week_counter(self):
        self.week = str(int(self.week)+1)

    def week_minus(self):
        self.week = str(int(self.week) - 1)

    def weekk(self):
        print(self.week)
        return int(self.week)

    def checkbox_click(self, checkbox, value):
        day = [self.mon, self.tue, self.wed, self.thur, self.fri, self.sat, self.sun]
        dey = [self.mon_doc, self.tue_doc, self.wed_doc, self.thur_doc, self.fri_doc, self.sat_doc, self.sun_doc]
        dai = [self.mons, self.tues, self.weds, self.thurs, self.fris, self.sats, self.suns]
        #object variable
        self.dates = []
        for x in day:
            if x.active:
                self.dates.append(1)
        for y in dey:
            if y.active:
                self.dates.append(2)
        for z in dai:
            if z.active:
                self.dates.append(0)
        print("date",self.dates)
        return self.dates

class Player(sm.SM):
    start_state = 0
    start_points = 0
    def __init__(self):
        self.points = self.start_points
        self.state = self.start_state

    def get_next_values(self, state, inp):
        print(state)
        try:
            print("i tried")
            for i in inp:
                #not sick
                if state == 0:
                    print("state0")
                    #stay home or see doctor
                    if i == 0 or i == 2:
                        state = state
                        if i == 0:
                            output = str(self.points)
                        elif i == 2:
                            self.points -= 2
                            output = str(self.points)

                    #go out
                    elif i == 1:

                        y = random.randrange(1, 11, 1)
                        self.points += 1
                        output = str(self.points)
                        # 20 percent chance of sick
                        if y <= 2:
                            x = random.randrange(1, 11, 1)
                            # 20 percent chance of no symp
                            if x <= 2:
                                state = 1
                            # 80 percent chance of symp
                            elif x > 2:
                                state = 2
                        #80 percent change of not sick
                        elif y > 2:
                            state = state
                #sick wo symp
                elif state == 1:
                    print("state1")
                    #stay home
                    if i == 0:
                        output = str(self.points)
                        state = state
                    #go out
                    elif i == 1:
                        self.points += 1
                        output = str(self.points)
                        y = random.randrange(1, 11, 1)
                        # 20 percent chance of sick
                        if y <= 2:
                            #death
                            state = 3
                        # 80 percent change of not sick
                        elif y > 2:
                            state = state
                    #doc cure
                    elif i == 2:
                        self.points -= 2
                        output = str(self.points)
                        state = 0

                #sick w symp
                elif state == 2:
                    print("state2")
                    if i == 0:
                        state = state
                        output = str(self.points)
                    elif i == 1:
                        self.points += 1
                        output = str(self.points)
                        y = random.randrange(1, 11, 1)
                        # 20 percent chance of sick
                        if y <= 2:
                            #death
                            state = 3
                        # 80 percent change of not sick
                        elif y > 2:
                            state = state
                    #doc cure
                    elif i == 2:
                        self.points -= 2
                        output = str(self.points)
                        state = 0

                elif state == 3:
                    print("state3")
                    output = str(self.points)
                    state = state
            return (state, output)

        except UnboundLocalError:
            print("ULE")
            state = state
            output = str(self.points)
            return (state,output)

class StatsWindow(Screen):
    points = StringProperty('0')
    symptoms = StringProperty("No Symptoms")

    def Process(self):
        try:
            print("trying")
            global g_player

            self.player = g_player

            print('State:', self.player.state)
            print('Points:', self.points)
            inp = self.manager.screens[2].dates
            self.points = self.player.step(inp)
            print('Pointsssss:', self.points)
            if int(self.points) <= 0:
                self.manager.current = "end_starve"
                self.manager.transition.direction = "left"
                return None

            if self.player.state == 3:
                self.manager.current = "end_virus"
                self.manager.transition.direction = "left"
                return None

            if self.player.state == 2:
                self.symptoms = "Infected"

            if self.manager.screens[2].weekk() == 5:
                print('week 5')
                if self.player.state == 1:
                    self.manager.current = "end_asymp"
                    self.manager.transition.direction = "left"
                    return None
                elif self.player.state == 2:
                    self.manager.current = "end_virus"
                    self.manager.transition.direction = "left"
                    return None
                else:
                    '''call the tt function'''
                    self.manager.screens[4].tt()
                    self.manager.current = "end_win"
                    self.manager.transition.direction = "left"
                    return None
            if self.player.state == 0:
                self.symptoms = "Not Infected"
            if self.player.state == 1:
                self.symptoms = "Not Infected"
            self.manager.current = "stats"
            self.manager.transition.direction = "left"

        except AttributeError:
            print("AE")
            self.manager.current = "cal"
            self.manager.screens[2].week_minus()

    def Button_Press(self):
        self.manager.current = "cal"
        self.manager.transition.direction = "left"

class EndWWindow(Screen):
    t = StringProperty('')
    def tt(self):
        self.t = "Points: {}".format(self.manager.screens[3].points)
    again = restart

class EndVWindow(Screen):
    again = restart

class EndSWindow(Screen):
    again = restart

class EndAWindow(Screen):
    again = restart

class Windmanager(ScreenManager):
    pass

kv = Builder.load_file("c19survive.kv")

class MyApp(App):

    '''This class will inherit from the App class that we imported above.
    This means it will take all functionally from App.
        From this app class there exist a method called the build method that
        will tell kivy what to put on the screen'''

    def build(self):
        '''Initializes the application; it will be called only once.
                Since my method returns a kv file, my root widget is Windmanager.'''
        return kv


'''its for importing into other code'''
if __name__ == "__main__":
    game = MyApp()
    g_player = Player()
    game.run()