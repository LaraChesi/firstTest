from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'complex_form_layout'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField()
    gender = models.StringField(choices=["female","male","diverse", "other"])
    preference = models.StringField(widget=widgets.RadioSelect, choices=[["wrp","Wrap"], ["brt","Burrito"], ["flf","Falafel"] ])
    

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'preference']

    
page_sequence = [MyPage]
