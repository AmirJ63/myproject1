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
    sum_klee= models.IntegerField()
    sum_kandinsky = models.IntegerField()
    klee_difference = models.IntegerField()

    klee1 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )

    kandinsky1 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )

    klee2 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    klee3 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    klee4 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    klee5 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )

    kandinsky2 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    kandinsky3 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    kandinsky4 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )
    kandinsky5 = models.IntegerField(
        initial=0,
        widget=widgets.RadioSelectHorizontal,
        choices=[ 0, 1, 2, 3, 4, 5 ],
        label="I like:"
    )

# Functions

def creating_session(subsession: Subsession):
    session = subsession.session
    session.scores = []

def set_score (player:Player):
    pass


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [ 'klee1', 'kandinsky1' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee1' ] + values[ 'kandinsky1' ] != 5:
            return 'The numbers must add up to 5'


class Page2(Page):
    form_model = 'player'
    form_fields = ['klee2', 'kandinsky2']

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values['klee2'] + values['kandinsky2'] != 5:
            return 'The numbers must add up to 5'


class Page3(Page):
    form_model = 'player'
    form_fields = [ 'kandinsky3', 'klee3' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee3' ] + values[ 'kandinsky3' ] != 5:
            return 'The numbers must add up to 5'


class Page4(Page):
    form_model = 'player'
    form_fields = [ 'klee4', 'kandinsky4' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee4' ] + values[ 'kandinsky4' ] != 5:
            return 'The numbers must add up to 5'


class Page5(Page):
    form_model = 'player'
    form_fields = [ 'kandinsky5', 'klee5' ]

    @staticmethod
    def error_message(player: Player, values):
        print('values is', values)
        if values[ 'klee5' ] + values[ 'kandinsky5' ] != 5:
            return 'The numbers must add up to 5'


class Results(Page):

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_score(player)
        session = player.session
        session.scores.append(player.klee_difference)

        player.participant.klee_difference = player.klee_difference


    def vars_for_template(player: Player):
        player.sum_klee = player.klee1 + player.klee2 + player.klee3 + player.klee4 + player.kandinsky5
        player.sum_kandinsky = player.kandinsky1 + player.kandinsky2 + player.kandinsky3 + player.kandinsky4 + player.kandinsky5
        player.klee_difference = player.sum_klee - player.sum_kandinsky


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


# new app
#class WaitForAll(WaitPage):
   # @staticmethod
    #def after_all_players_arrive(subsession: Subsession):

       ## this code has the same function but not suitable and the below code is more suitable. why?
       # for p in subsession.get_players():
           # p.participant.klee_difference

            #ps = subsession.get_players()
            #scores = [p.participant.klee_difference for p in ps]