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
    name_in_url = 'trial_sum'
    players_per_group = None
    num_rounds = 1

    deck_seq = ['A', 'B', 'C']


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            deck_list = Constants.deck_seq.copy()

            remove1_trial = random.choice(deck_list)
            deck_list.remove(remove1_trial)
            p.participant.vars['remove1_trial'] = remove1_trial
            p.remove1_trial = remove1_trial

            remove2_trial = random.choice(deck_list)
            deck_list.remove(remove2_trial)
            p.participant.vars['remove2_trial'] = remove2_trial
            p.remove2_trial = remove2_trial

            deck_left = deck_list[0]
            p.participant.vars['deck_left_trial'] = deck_left
            p.deck_left = deck_left

            if deck_left == 'A':
                card_left = ['green', 'green', 'green', 'red', 'red', 'red']
                random.shuffle(card_left)
                for i in range(0, 3):
                    card_str = 'card_trial%s' % (i+1)
                    p.participant.vars[card_str] = card_left[i]
                    setattr(p, card_str, card_left[i])

            if deck_left == 'B':
                card_left = ['green', 'green', 'green', 'green', 'red', 'red']
                random.shuffle(card_left)
                for i in range(0, 3):
                    card_str = 'card_trial%s' % (i+1)
                    p.participant.vars[card_str] = card_left[i]
                    setattr(p, card_str, card_left[i])

            if deck_left == 'C':
                card_left = ['green', 'green', 'green', 'green', 'green', 'red']
                random.shuffle(card_left)
                for i in range(0, 3):
                    card_str = 'card_trial%s' % (i+1)
                    p.participant.vars[card_str] = card_left[i]
                    setattr(p, card_str, card_left[i])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    remove1_trial = models.StringField(blank=True)
    remove2_trial = models.StringField(blank=True)
    deck_left = models.StringField(blank=True)

    card_trial1 = models.StringField(blank=True)
    card_trial2 = models.StringField(blank=True)
    card_trial3 = models.StringField(blank=True)

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
