from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _
import random, time


def get_timeout_seconds(player):
    return player.participant.vars['expiry'] - time.time()


class Start(Page):
    form_model = 'player'
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.player.round_number == 1 and \
               self.participant.vars['end'] == 0 and self.participant.vars['consent'] == 'yes' and \
               get_timeout_seconds(self.player) > 3


class Period1(Page):
    form_model = 'player'
    form_fields = ['spend1', 'check_spend1', 'reward1']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and \
               self.participant.vars['consent'] == 'yes' and self.participant.vars['end'] == 0 \
               and get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['check_spend1']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 29 + 11*(self.player.round_number - 1)
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar
        }

    def before_next_page(self):
        self.participant.vars['balance2'] = round(11.92 - self.player.spend1, 2)
        self.participant.vars['spend1'] = self.player.spend1
        self.participant.vars['reward1'] = self.player.reward1
        self.player.total_reward = round(self.player.reward1, 2)
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward1, 2)


class Period2(Page):
    form_model = 'player'
    form_fields = ['spend2', 'check_spend2', 'reward2']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['end'] == 0 and get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['check_spend2']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 30 + 11*(self.player.round_number - 1)
        remove1 = self.player.in_round(round_num).remove1
        balance2 = self.participant.vars['balance2']
        spend1 = self.participant.vars['spend1']
        reward1 = self.participant.vars['reward1']
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'remove1': remove1,
            'balance2': balance2,
            'spend1': spend1,
            'reward1': reward1
        }

    def before_next_page(self):
        self.participant.vars['balance3'] = round(self.participant.vars['balance2'] - self.player.spend2, 2)
        self.participant.vars['spend2'] = self.player.spend2
        self.participant.vars['reward2'] = self.player.reward2
        self.player.total_reward = round(self.player.reward2 + self.player.reward1, 2)
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward2 + self.player.reward1, 2)


class Period3(Page):
    form_model = 'player'
    form_fields = ['spend3', 'check_spend3', 'reward3']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['end'] == 0 and get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['check_spend3']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 31 + 11*(self.player.round_number - 1)
        remove1 = self.player.in_round(round_num).remove1
        remove2 = self.player.in_round(round_num).remove2
        balance2 = self.participant.vars['balance2']
        balance3 = self.participant.vars['balance3']
        spend1 = self.participant.vars['spend1']
        reward1 = self.participant.vars['reward1']
        spend2 = self.participant.vars['spend2']
        reward2 = self.participant.vars['reward2']
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'remove1': remove1,
            'remove2': remove2,
            'balance2': balance2,
            'balance3': balance3,
            'spend1': spend1,
            'reward1': reward1,
            'spend2': spend2,
            'reward2': reward2
        }

    def before_next_page(self):
        self.participant.vars['balance4'] = round(self.participant.vars['balance3'] - self.player.spend3, 2)
        self.participant.vars['spend3'] = self.player.spend3
        self.participant.vars['reward3'] = self.player.reward3
        self.player.total_reward = round(self.player.reward3 + self.player.reward2 + self.player.reward1, 2)
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


class End4(Page):
    form_model = 'player'
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.player.card1 == 'red' and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 38 + 11*(self.player.round_number - 1)
        reward1 = self.participant.vars['reward1']
        reward2 = self.participant.vars['reward2']
        reward3 = self.participant.vars['reward3']
        total = round(reward1 + reward2 + reward3, 2)
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'reward1': reward1,
            'reward2': reward2,
            'reward3': reward3,
            'total': total
        }
    
    def before_next_page(self):
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


class Period4(Page):
    form_model = 'player'
    form_fields = ['spend4', 'check_spend4', 'reward4']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.player.card1 == 'green' and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['check_spend4']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 32 + 11*(self.player.round_number - 1)
        remove1 = self.player.in_round(round_num).remove1
        remove2 = self.player.in_round(round_num).remove2
        deck_left = self.player.in_round(round_num).deck_left
        balance2 = self.participant.vars['balance2']
        balance3 = self.participant.vars['balance3']
        balance4 = self.participant.vars['balance4']
        spend1 = self.participant.vars['spend1']
        reward1 = self.participant.vars['reward1']
        spend2 = self.participant.vars['spend2']
        reward2 = self.participant.vars['reward2']
        spend3 = self.participant.vars['spend3']
        reward3 = self.participant.vars['reward3']
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'remove1': remove1,
            'remove2': remove2,
            'deck_left': deck_left,
            'balance2': balance2,
            'balance3': balance3,
            'balance4': balance4,
            'spend1': spend1,
            'reward1': reward1,
            'spend2': spend2,
            'reward2': reward2,
            'spend3': spend3,
            'reward3': reward3
        }

    def before_next_page(self):
        self.participant.vars['balance5'] = round(self.participant.vars['balance4'] - self.player.spend4, 2)
        self.participant.vars['spend4'] = self.player.spend4
        self.participant.vars['reward4'] = self.player.reward4
        self.player.total_reward = round(self.player.reward4 + self.player.reward3 + self.player.reward2 + self.player.reward1, 2)
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward4 + self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


class End5(Page):
    form_model = 'player'
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.player.card1 == 'green' and self.player.card2 == 'red' and \
               self.participant.vars['end'] == 0 and get_timeout_seconds(self.player) > 3

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 38 + 11*(self.player.round_number - 1)
        reward1 = self.participant.vars['reward1']
        reward2 = self.participant.vars['reward2']
        reward3 = self.participant.vars['reward3']
        reward4 = self.participant.vars['reward4']
        total = round(reward1 + reward2 + reward3 + reward4, 2)
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'reward1': reward1,
            'reward2': reward2,
            'reward3': reward3,
            'reward4': reward4,
            'total': total
        }

    def before_next_page(self):
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward4 + self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


class Period5(Page):
    form_model = 'player'
    form_fields = ['spend5', 'check_spend5', 'reward5']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.player.card1 == 'green' and self.player.card2 == 'green' and \
               self.participant.vars['end'] == 0 and get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['check_spend5']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 33 + 11*(self.player.round_number - 1)
        remove1 = self.player.in_round(round_num).remove1
        remove2 = self.player.in_round(round_num).remove2
        deck_left = self.player.in_round(round_num).deck_left
        balance2 = self.participant.vars['balance2']
        balance3 = self.participant.vars['balance3']
        balance4 = self.participant.vars['balance4']
        balance5 = self.participant.vars['balance5']
        spend1 = self.participant.vars['spend1']
        reward1 = self.participant.vars['reward1']
        spend2 = self.participant.vars['spend2']
        reward2 = self.participant.vars['reward2']
        spend3 = self.participant.vars['spend3']
        reward3 = self.participant.vars['reward3']
        spend4 = self.participant.vars['spend4']
        reward4 = self.participant.vars['reward4']
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'remove1': remove1,
            'remove2': remove2,
            'deck_left': deck_left,
            'balance2': balance2,
            'balance3': balance3,
            'balance4': balance4,
            'balance5': balance5,
            'spend1': spend1,
            'reward1': reward1,
            'spend2': spend2,
            'reward2': reward2,
            'spend3': spend3,
            'reward3': reward3,
            'spend4': spend4,
            'reward4': reward4
        }

    def before_next_page(self):
        self.participant.vars['balance6'] = round(self.participant.vars['balance5'] - self.player.spend5, 2)
        self.participant.vars['spend5'] = self.player.spend5
        self.participant.vars['reward5'] = self.player.reward5
        self.player.total_reward = round(self.player.reward5 + self.player.reward4 + self.player.reward3 +
                                         self.player.reward2 + self.player.reward1, 2)
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward5 + self.player.reward4 + self.player.reward3 +
                                                      self.player.reward2 + self.player.reward1, 2)


class End6(Page):
    form_model = 'player'
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.player.card1 == 'green' and self.player.card2 == 'green' and \
               self.player.card3 == 'red' and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 38 + 11*(self.player.round_number - 1)
        reward1 = self.participant.vars['reward1']
        reward2 = self.participant.vars['reward2']
        reward3 = self.participant.vars['reward3']
        reward4 = self.participant.vars['reward4']
        reward5 = self.participant.vars['reward5']
        total = round(reward1 + reward2 + reward3 + reward4 + reward5, 2)
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'reward1': reward1,
            'reward2': reward2,
            'reward3': reward3,
            'reward4': reward4,
            'reward5': reward5,
            'total': total
        }

    def before_next_page(self):
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward5 + self.player.reward4 + self.player.reward3 +
                                                      self.player.reward2 + self.player.reward1, 2)


class Period6(Page):
    form_model = 'player'
    form_fields = ['spend6', 'check_spend6', 'reward6']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.player.card1 == 'green' and self.player.card2 == 'green' and \
               self.player.card3 == 'green' and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['check_spend6']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 34 + 11*(self.player.round_number - 1)
        remove1 = self.player.in_round(round_num).remove1
        remove2 = self.player.in_round(round_num).remove2
        deck_left = self.player.in_round(round_num).deck_left
        balance2 = self.participant.vars['balance2']
        balance3 = self.participant.vars['balance3']
        balance4 = self.participant.vars['balance4']
        balance5 = self.participant.vars['balance5']
        balance6 = self.participant.vars['balance6']
        spend1 = self.participant.vars['spend1']
        reward1 = self.participant.vars['reward1']
        spend2 = self.participant.vars['spend2']
        reward2 = self.participant.vars['reward2']
        spend3 = self.participant.vars['spend3']
        reward3 = self.participant.vars['reward3']
        spend4 = self.participant.vars['spend4']
        reward4 = self.participant.vars['reward4']
        spend5 = self.participant.vars['spend5']
        reward5 = self.participant.vars['reward5']
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'remove1': remove1,
            'remove2': remove2,
            'deck_left': deck_left,
            'balance2': balance2,
            'balance3': balance3,
            'balance4': balance4,
            'balance5': balance5,
            'balance6': balance6,
            'spend1': spend1,
            'reward1': reward1,
            'spend2': spend2,
            'reward2': reward2,
            'spend3': spend3,
            'reward3': reward3,
            'spend4': spend4,
            'reward4': reward4,
            'spend5': spend5,
            'reward5': reward5
        }

    def before_next_page(self):
        self.participant.vars['reward6'] = self.player.reward6
        self.player.total_reward = round(self.player.reward6 + self.player.reward5 + self.player.reward4 +
                                         self.player.reward3 + self.player.reward2 + self.player.reward1, 2)
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward6 + self.player.reward5 + self.player.reward4 +
                                                      self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


class End(Page):
    form_model = 'player'
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.player.card1 == 'green' and self.player.card2 == 'green' and \
               self.player.card3 == 'green' and self.participant.vars['end'] == 0 and \
               get_timeout_seconds(self.player) > 3

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        round_num = self.player.round_number
        round_num_bar = 38 + 11*(self.player.round_number - 1)
        reward1 = self.participant.vars['reward1']
        reward2 = self.participant.vars['reward2']
        reward3 = self.participant.vars['reward3']
        reward4 = self.participant.vars['reward4']
        reward5 = self.participant.vars['reward5']
        reward6 = self.participant.vars['reward6']
        total = round(reward1 + reward2 + reward3 + reward4 + reward5 + reward6, 2)
        return {
            'lang': lang,
            'round_num': round_num,
            'round_num_bar': round_num_bar,
            'reward1': reward1,
            'reward2': reward2,
            'reward3': reward3,
            'reward4': reward4,
            'reward5': reward5,
            'reward6': reward6,
            'total': total
        }

    def before_next_page(self):
        reward_str = 'total_reward' + str(self.player.round_number)
        self.participant.vars[reward_str] = round(self.player.reward6 + self.player.reward5 + self.player.reward4 +
                                                  self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


page_sequence = [Start, Period1, Period2, Period3, End4, Period4, End5, Period5, End6, Period6, End]
