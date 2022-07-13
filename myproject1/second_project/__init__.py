


from otree.api import *

doc = """
Card Game (competition game)
"""



class Constants(BaseConstants):
    name_in_url = 'Making group'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
   pass




##Functions



# PAGES

class WaitForAll(WaitPage):
   @staticmethod
   def after_all_players_arrive(subsession: Subsession):
       players = subsession.get_players()
       scores = [p.participant.klee_difference for p in players]
       subsession.scores = scores
       rank = sorted(players, key=lambda x: x.participant.scores)
       subsession.rank = rank


class Page1(Page):

    @staticmethod
    def vars_for_template(subsession: Subsession):
        return subsession.scores, subsession.rank



page_sequence = [WaitForAll, Page1]

