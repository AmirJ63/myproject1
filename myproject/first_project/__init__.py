from otree.api import *
from otree.models import participant



doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'first_project'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass



class Player(BasePlayer):
    sum_klee_paintings = models.IntegerField()
    sum_kandinsky_paintings = models.IntegerField()
    difference_klee = models.IntegerField()

    klee1_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )

    kandinsky1_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )

    klee2_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    klee3_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    klee4_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    klee5_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )

    kandinsky2_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    kandinsky3_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    kandinsky4_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    kandinsky5_paintings = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )


# PAGES


class Page1(Page):
    form_model = 'player'
    form_fields = [ 'klee1_paintings', 'kandinsky1_paintings' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee1_paintings' ] + values[ 'kandinsky1_paintings' ] != 5:
            return 'The numbers must add up to 5'


class Page2(Page):
    form_model = 'player'
    form_fields = [ 'klee2_paintings', 'kandinsky2_paintings' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee2_paintings' ] + values[ 'kandinsky2_paintings' ] != 5:
            return 'The numbers must add up to 5'


class Page3(Page):
    form_model = 'player'
    form_fields = [ 'kandinsky3_paintings', 'klee3_paintings' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee3_paintings' ] + values[ 'kandinsky3_paintings' ] != 5:
            return 'The numbers must add up to 5'


class Page4(Page):
    form_model = 'player'
    form_fields = [ 'klee4_paintings', 'kandinsky4_paintings' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee4_paintings' ] + values[ 'kandinsky4_paintings' ] != 5:
            return 'The numbers must add up to 5'


class Page5(Page):
    form_model = 'player'
    form_fields = [ 'kandinsky5_paintings', 'klee5_paintings' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee5_paintings' ] + values[ 'kandinsky5_paintings' ] != 5:
            return 'The numbers must add up to 5'


class Results(Page):
    def vars_for_template(player: Player):
        player.sum_klee_paintings = player.klee1_paintings + player.klee2_paintings + player.klee3_paintings + player.klee4_paintings + player.kandinsky5_paintings
        player.sum_kandinsky_paintings = player.kandinsky1_paintings + player.kandinsky2_paintings + player.kandinsky3_paintings + player.kandinsky4_paintings + player.kandinsky5_paintings
        player.difference_klee = player.sum_klee_paintings - player.sum_kandinsky_paintings
        participant = player.participant
        participant.result = player.difference_klee




class ResultsWaitPage(WaitPage):
    pass

class Resultscombine(Page):
    pass



            #participant.result.insert(p,player.id_in_group(p))


      # if player.id_in_group !=1:
          # for pp in player.get_others_in_group():
            #   participant = player.participant
             #  participant.result = [pp.participant.result, participant.result]



page_sequence = [Page1, Page2, Results, ResultsWaitPage, Resultscombine]

##
##class Combinedresults(Page):
## @staticmethod
##def vars_for_template(group: Group):
##  all_difference_klee = [1:5]
## print(all_difference_klee)
## for pp in group.get_players():
## print(pp)


##for p in player.get_others_in_subsession():
##    participant = p.participant
##  session = p.session
## all_difference_klee.append(p.difference_klee)
