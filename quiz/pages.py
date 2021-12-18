from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils.translation import ugettext_lazy as _
import random
from .generic_pages import Page
import time


class Quiz_start(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes'


class Quiz(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes'

    def quiz1_choices(player):
        choices = [['wheel', _('Preferred deck of cards to use')],
                   ['invest', _('Investment (in Euro)')],
                   ['spending', _('Spending (in points)')]]
        random.shuffle(choices)
        return choices

    def quiz2_choices(player):
        choices = [['1', _('1 period')], ['3', _('3 periods')], ['6', _('6 periods')]]
        random.shuffle(choices)
        return choices

    def quiz3_choices(player):
        choices = [['1', _('1 period')], ['3', _('3 periods')], ['6', _('6 periods')]]
        random.shuffle(choices)
        return choices

    def quiz4_choices(player):
        choices = [['points_left', _('The amount left on the Account Balance at the start of the period')],
                   ['10.92', _('10.92 points')],
                   ['same_points', _('The same amount spent in the previous period or more')]]
        random.shuffle(choices)
        return choices

    def quiz5_choices(player):
        choices = [['lost', _('I lose these points.')],
                   ['spend', _('I can spend these points in the next round.')],
                   ['converted', _('These points are automatically converted into Euro Rewards.')]]
        random.shuffle(choices)
        return choices

    def quiz6_choices(player):
        choices = [['new_points', _('I am given new points to increase my Account Balance.')],
                   ['no_reward', _('There are no Rewards available regardless of my Spending decision.')],
                   ['remove_deck', _('One of the card decks is automatically removed by the computer.')]]
        random.shuffle(choices)
        return choices

    def error_message(self, values):
        if not values['quiz1'] or not values['quiz2'] or not values['quiz3'] or not values['quiz4'] \
                or not values['quiz5'] or not values['quiz6']:
            return _('Please answer all questions.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        return {
            'lang': lang,
            'treatment': treatment
        }

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60
        if self.player.quiz1 and self.player.quiz2 and self.player.quiz3 and self.player.quiz4 and self.player.quiz5 \
                and self.player.quiz6:
            if self.player.quiz1 != 'spending':
                self.participant.vars['mis_q1'] = 1
                self.player.quiz1 = ''
            if self.player.quiz2 != '3':
                self.participant.vars['mis_q2'] = 1
                self.player.quiz2 = ''
            if self.player.quiz3 != '6':
                self.participant.vars['mis_q3'] = 1
                self.player.quiz3 = ''
            if self.player.quiz4 != 'points_left':
                self.participant.vars['mis_q4'] = 1
                self.player.quiz4 = ''
            if self.player.quiz5 != 'lost':
                self.participant.vars['mis_q5'] = 1
                self.player.quiz5 = ''
            if self.player.quiz6 != 'remove_deck':
                self.participant.vars['mis_q6'] = 1
                self.player.quiz6 = ''


class End_attempt1(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3'] + \
                      self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake > 2 and self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes'

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73956&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_retry(Page):
    form_model = 'player'

    def get_form_fields(self):
        formfield_list = []
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
            + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        if sum_mistake < 3:
            if self.participant.vars['mis_q1'] == 1:
                formfield_list.append('quiz1')
            if self.participant.vars['mis_q2'] == 1:
                formfield_list.append('quiz2')
            if self.participant.vars['mis_q3'] == 1:
                formfield_list.append('quiz3')
            if self.participant.vars['mis_q4'] == 1:
                formfield_list.append('quiz4')
            if self.participant.vars['mis_q5'] == 1:
                formfield_list.append('quiz5')
            if self.participant.vars['mis_q6'] == 1:
                formfield_list.append('quiz6')
        return formfield_list

    def quiz1_choices(player):
        choices = [['wheel', _('Preferred deck of cards to use')],
                   ['invest', _('Investment (in Euro)')],
                   ['spending', _('Spending (in points)')]]
        random.shuffle(choices)
        return choices

    def quiz2_choices(player):
        choices = [['1', _('1 period')], ['3', _('3 periods')], ['6', _('6 periods')]]
        random.shuffle(choices)
        return choices

    def quiz3_choices(player):
        choices = [['1', _('1 period')], ['3', _('3 periods')], ['6', _('6 periods')]]
        random.shuffle(choices)
        return choices

    def quiz4_choices(player):
        choices = [['points_left', _('The amount left on the Account Balance at the start of the period')],
                   ['10.92', _('10.92 points')],
                   ['same_points', _('The same amount spent in the previous period or more')]]
        random.shuffle(choices)
        return choices

    def quiz5_choices(player):
        choices = [['lost', _('I lose these points.')],
                   ['spend', _('I can spend these points in the next round.')],
                   ['converted', _('These points are automatically converted into Euro Rewards.')]]
        random.shuffle(choices)
        return choices

    def quiz6_choices(player):
        choices = [['new_points', _('I am given new points to increase my Account Balance.')],
                   ['no_reward', _('There are no Rewards available regardless of my Spending decision.')],
                   ['remove_deck', _('One of the card decks is automatically removed by the computer.')]]
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
            + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake != 0 and sum_mistake < 3 and self.participant.vars['time_instruction'] >= 10 and \
               self.participant.vars['consent'] == 'yes'

    def error_message(self, values):
        if (self.participant.vars['mis_q1'] == 1 and not values['quiz1']) or \
                (self.participant.vars['mis_q2'] == 1 and not values['quiz2']) or \
                (self.participant.vars['mis_q3'] == 1 and not values['quiz3']) or \
                (self.participant.vars['mis_q4'] == 1 and not values['quiz4']) or \
                (self.participant.vars['mis_q5'] == 1 and not values['quiz5']) or \
                (self.participant.vars['mis_q6'] == 1 and not values['quiz6']):
            return _('Please answer the question.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        treatment = self.participant.vars['treatment']
        if self.participant.vars['mis_q1'] == 1:
            show1 = 1
        else:
            show1 = 0

        if self.participant.vars['mis_q2'] == 1:
            show2 = 1
        else:
            show2 = 0

        if self.participant.vars['mis_q3'] == 1:
            show3 = 1
        else:
            show3 = 0

        if self.participant.vars['mis_q4'] == 1:
            show4 = 1
        else:
            show4 = 0

        if self.participant.vars['mis_q5'] == 1:
            show5 = 1
        else:
            show5 = 0

        if self.participant.vars['mis_q6'] == 1:
            show6 = 1
        else:
            show6 = 0

        return {
            'lang': lang,
            'treatment': treatment,
            'show1': show1,
            'show2': show2,
            'show3': show3,
            'show4': show4,
            'show5': show5,
            'show6': show6
        }

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60
        if self.participant.vars['mis_q1'] == 1:
            if self.player.quiz1 == 'spending':
                self.participant.vars['mis_q1'] = 0

        if self.participant.vars['mis_q2'] == 1:
            if self.player.quiz2 == '3':
                self.participant.vars['mis_q2'] = 0

        if self.participant.vars['mis_q3'] == 1:
            if self.player.quiz3 == '6':
                self.participant.vars['mis_q3'] = 0

        if self.participant.vars['mis_q4'] == 1:
            if self.player.quiz4 == 'points_left':
                self.participant.vars['mis_q4'] = 0

        if self.participant.vars['mis_q5'] == 1:
            if self.player.quiz5 == 'lost':
                self.participant.vars['mis_q5'] = 0

        if self.participant.vars['mis_q6'] == 1:
            if self.player.quiz6 == 'remove_deck':
                self.participant.vars['mis_q6'] = 0


class End_attempt2(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake != 0 and self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes'

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73956&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


page_sequence = [Quiz_start, Quiz, End_attempt1, Quiz_retry, End_attempt2]
