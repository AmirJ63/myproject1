


from otree.api import *
from otree.models import participant
import random
import json

doc = """
Dictator Game
"""



class Constants(BaseConstants):
    name_in_url = 'Dictator'
    players_per_group = 2
    num_rounds = 1
    endoment = cu(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    decision = models.CurrencyField(label='How much do you want to allocate?', min=0, max=100)

    def set_payoffs(group):
        dictator = group.get_player_by_id(1)
        receiver = group.get_player_by_id(2)
        dictator.payoff = Constants.endoment - group.decision
        receiver.payoff = group.decision


class Player(BasePlayer):
    pass

class Instructions(Page):
    pass


class Decision(Page):
    def is_displayed(player: Player):
        return player.id_in_group ==1

    form_model = 'group'
    form_fields = ['decision']

    def before_next_page(player: Player, timeout_happened):
        timeout_seconds = 120



class WaitToPlay(WaitPage):
    def after_all_players_arrive(group: Group):
        after_all_players_arrive = group.set_payoffs()


class Results(Page):
    pass
    def vars_for_template(player: Player):
        others = player.get_others_in_group()
        return dict(
            other_payoff=others[0].payoff
        )


page_sequence = [Instructions, Decision, WaitToPlay, Results]

