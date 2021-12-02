from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'sum'
    players_per_group = None
    num_rounds = 6

    deck_seq = [['A', 'B', 'C'], ['A', 'C', 'B'], ['C', 'A', 'B'], ['C', 'B', 'A'], ['B', 'A', 'C'], ['B', 'C', 'A']]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            desk_list = Constants.deck_seq.copy()
            random.shuffle(desk_list)

            for i in range(0, 6):
                p.in_round(i+1).remove1 = desk_list[i][0]
                p.in_round(i+1).remove2 = desk_list[i][1]
                p.in_round(i+1).deck_left = desk_list[i][2]

                if desk_list[i][2] == 'A':
                    card_left = ['green', 'green', 'green', 'red', 'red', 'red']
                    random.shuffle(card_left)
                    for j in range(0, 3):
                        card_str = 'card%s' % (j+1)
                        setattr(p.in_round(i+1), card_str, card_left[j])

                if desk_list[i][2] == 'B':
                    card_left = ['green', 'green', 'green', 'green', 'red', 'red']
                    random.shuffle(card_left)
                    for j in range(0, 3):
                        card_str = 'card%s' % (j+1)
                        setattr(p.in_round(i+1), card_str, card_left[j])

                if desk_list[i][2] == 'C':
                    card_left = ['green', 'green', 'green', 'green', 'green', 'red']
                    random.shuffle(card_left)
                    for j in range(0, 3):
                        card_str = 'card%s' % (j+1)
                        setattr(p.in_round(i+1), card_str, card_left[j])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    remove1 = models.StringField(blank=True)
    remove2 = models.StringField(blank=True)
    deck_left = models.StringField(blank=True)

    card1 = models.StringField(blank=True)
    card2 = models.StringField(blank=True)
    card3 = models.StringField(blank=True)

    spend1 = models.FloatField(blank=True)
    check_spend1 = models.IntegerField(blank=True)
    reward1 = models.FloatField(blank=True)

    spend2 = models.FloatField(blank=True)
    check_spend2 = models.IntegerField(blank=True)
    reward2 = models.FloatField(blank=True)

    spend3 = models.FloatField(blank=True)
    check_spend3 = models.IntegerField(blank=True)
    reward3 = models.FloatField(blank=True)

    spend4 = models.FloatField(blank=True)
    check_spend4 = models.IntegerField(blank=True)
    reward4 = models.FloatField(blank=True)

    spend5 = models.FloatField(blank=True)
    check_spend5 = models.IntegerField(blank=True)
    reward5 = models.FloatField(blank=True)

    spend6 = models.FloatField(blank=True)
    check_spend6 = models.IntegerField(blank=True)
    reward6 = models.FloatField(blank=True)

    total_reward = models.FloatField(blank=True)
