from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'multiply_app'
    players_per_group = None
    num_rounds = 1
    factor = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.FloatField()


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = ["number_entered"]


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        result = player.number_entered*Constants.factor
        return{
            "result": result,
        }


page_sequence = [MyPage, Results]
