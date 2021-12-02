from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Start(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes'


class Period1(Page):
    form_model = 'player'
    form_fields = ['spend1', 'check_spend1', 'reward1']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes'

    def error_message(self, values):
        if not values['check_spend1']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}

    def before_next_page(self):
        self.participant.vars['balance_trial2'] = round(11.92 - self.player.spend1, 2)
        self.participant.vars['spend_trial1'] = self.player.spend1
        self.participant.vars['reward_trial1'] = self.player.reward1
        self.player.total_reward = round(self.player.reward1, 2)


class Period2(Page):
    form_model = 'player'
    form_fields = ['spend2', 'check_spend2', 'reward2']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes'

    def error_message(self, values):
        if not values['check_spend2']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        remove1 = self.participant.vars['remove1_trial']
        balance2 = self.participant.vars['balance_trial2']
        spend1 = self.participant.vars['spend_trial1']
        reward1 = self.participant.vars['reward_trial1']
        return {
            'lang': lang,
            'remove1': remove1,
            'balance2': balance2,
            'spend1': spend1,
            'reward1': reward1
        }

    def before_next_page(self):
        self.participant.vars['balance_trial3'] = round(self.participant.vars['balance_trial2'] - self.player.spend2, 2)
        self.participant.vars['spend_trial2'] = self.player.spend2
        self.participant.vars['reward_trial2'] = self.player.reward2
        self.player.total_reward = round(self.player.reward2 + self.player.reward1, 2)


class Period3(Page):
    form_model = 'player'
    form_fields = ['spend3', 'check_spend3', 'reward3']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes'

    def error_message(self, values):
        if not values['check_spend3']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        remove1 = self.participant.vars['remove1_trial']
        remove2 = self.participant.vars['remove2_trial']
        balance2 = self.participant.vars['balance_trial2']
        balance3 = self.participant.vars['balance_trial3']
        spend1 = self.participant.vars['spend_trial1']
        reward1 = self.participant.vars['reward_trial1']
        spend2 = self.participant.vars['spend_trial2']
        reward2 = self.participant.vars['reward_trial2']
        return {
            'lang': lang,
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
        self.participant.vars['balance_trial4'] = round(self.participant.vars['balance_trial3'] - self.player.spend3, 2)
        self.participant.vars['spend_trial3'] = self.player.spend3
        self.participant.vars['reward_trial3'] = self.player.reward3
        self.player.total_reward = round(self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


class End4(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['card_trial1'] == 'red'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        reward1 = self.participant.vars['reward_trial1']
        reward2 = self.participant.vars['reward_trial2']
        reward3 = self.participant.vars['reward_trial3']
        total = round(reward1 + reward2 + reward3, 2)
        return {
            'lang': lang,
            'reward1': reward1,
            'reward2': reward2,
            'reward3': reward3,
            'total': total
        }


class Period4(Page):
    form_model = 'player'
    form_fields = ['spend4', 'check_spend4', 'reward4']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['card_trial1'] == 'green'

    def error_message(self, values):
        if not values['check_spend4']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        remove1 = self.participant.vars['remove1_trial']
        remove2 = self.participant.vars['remove2_trial']
        deck_left = self.participant.vars['deck_left_trial']
        balance2 = self.participant.vars['balance_trial2']
        balance3 = self.participant.vars['balance_trial3']
        balance4 = self.participant.vars['balance_trial4']
        spend1 = self.participant.vars['spend_trial1']
        reward1 = self.participant.vars['reward_trial1']
        spend2 = self.participant.vars['spend_trial2']
        reward2 = self.participant.vars['reward_trial2']
        spend3 = self.participant.vars['spend_trial3']
        reward3 = self.participant.vars['reward_trial3']
        return {
            'lang': lang,
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
        self.participant.vars['balance_trial5'] = round(self.participant.vars['balance_trial4'] - self.player.spend4, 2)
        self.participant.vars['spend_trial4'] = self.player.spend4
        self.participant.vars['reward_trial4'] = self.player.reward4
        self.player.total_reward = round(self.player.reward4 + self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


class End5(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['card_trial1'] == 'green' and self.participant.vars['card_trial2'] == 'red'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        reward1 = self.participant.vars['reward_trial1']
        reward2 = self.participant.vars['reward_trial2']
        reward3 = self.participant.vars['reward_trial3']
        reward4 = self.participant.vars['reward_trial4']
        total = round(reward1 + reward2 + reward3 + reward4, 2)
        return {
            'lang': lang,
            'reward1': reward1,
            'reward2': reward2,
            'reward3': reward3,
            'reward4': reward4,
            'total': total
        }


class Period5(Page):
    form_model = 'player'
    form_fields = ['spend5', 'check_spend5', 'reward5']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['card_trial1'] == 'green' and self.participant.vars['card_trial2'] == 'green'

    def error_message(self, values):
        if not values['check_spend5']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        remove1 = self.participant.vars['remove1_trial']
        remove2 = self.participant.vars['remove2_trial']
        deck_left = self.participant.vars['deck_left_trial']
        balance2 = self.participant.vars['balance_trial2']
        balance3 = self.participant.vars['balance_trial3']
        balance4 = self.participant.vars['balance_trial4']
        balance5 = self.participant.vars['balance_trial5']
        spend1 = self.participant.vars['spend_trial1']
        reward1 = self.participant.vars['reward_trial1']
        spend2 = self.participant.vars['spend_trial2']
        reward2 = self.participant.vars['reward_trial2']
        spend3 = self.participant.vars['spend_trial3']
        reward3 = self.participant.vars['reward_trial3']
        spend4 = self.participant.vars['spend_trial4']
        reward4 = self.participant.vars['reward_trial4']
        return {
            'lang': lang,
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
        self.participant.vars['balance_trial6'] = round(self.participant.vars['balance_trial5'] - self.player.spend5, 2)
        self.participant.vars['spend_trial5'] = self.player.spend5
        self.participant.vars['reward_trial5'] = self.player.reward5
        self.player.total_reward = round(self.player.reward5 + self.player.reward4 + self.player.reward3 +
                                         self.player.reward2 + self.player.reward1, 2)


class End6(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['card_trial1'] == 'green' and self.participant.vars['card_trial2'] == 'green' and \
               self.participant.vars['card_trial3'] == 'red'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        reward1 = self.participant.vars['reward_trial1']
        reward2 = self.participant.vars['reward_trial2']
        reward3 = self.participant.vars['reward_trial3']
        reward4 = self.participant.vars['reward_trial4']
        reward5 = self.participant.vars['reward_trial5']
        total = round(reward1 + reward2 + reward3 + reward4 + reward5, 2)
        return {
            'lang': lang,
            'reward1': reward1,
            'reward2': reward2,
            'reward3': reward3,
            'reward4': reward4,
            'reward5': reward5,
            'total': total
        }


class Period6(Page):
    form_model = 'player'
    form_fields = ['spend6', 'check_spend6', 'reward6']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['card_trial1'] == 'green' and self.participant.vars['card_trial2'] == 'green' and \
               self.participant.vars['card_trial3'] == 'green'

    def error_message(self, values):
        if not values['check_spend6']:
            return _('Please decide how much you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        remove1 = self.participant.vars['remove1_trial']
        remove2 = self.participant.vars['remove2_trial']
        deck_left = self.participant.vars['deck_left_trial']
        balance2 = self.participant.vars['balance_trial2']
        balance3 = self.participant.vars['balance_trial3']
        balance4 = self.participant.vars['balance_trial4']
        balance5 = self.participant.vars['balance_trial5']
        balance6 = self.participant.vars['balance_trial6']
        spend1 = self.participant.vars['spend_trial1']
        reward1 = self.participant.vars['reward_trial1']
        spend2 = self.participant.vars['spend_trial2']
        reward2 = self.participant.vars['reward_trial2']
        spend3 = self.participant.vars['spend_trial3']
        reward3 = self.participant.vars['reward_trial3']
        spend4 = self.participant.vars['spend_trial4']
        reward4 = self.participant.vars['reward_trial4']
        spend5 = self.participant.vars['spend_trial5']
        reward5 = self.participant.vars['reward_trial5']
        return {
            'lang': lang,
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
        self.participant.vars['reward_trial6'] = self.player.reward6
        self.player.total_reward = round(self.player.reward6 + self.player.reward5 + self.player.reward4 +
                                         self.player.reward3 + self.player.reward2 + self.player.reward1, 2)


class End(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 10 and self.participant.vars['consent'] == 'yes' and \
               self.participant.vars['card_trial1'] == 'green' and self.participant.vars['card_trial2'] == 'green' and \
               self.participant.vars['card_trial3'] == 'green'

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        reward1 = self.participant.vars['reward_trial1']
        reward2 = self.participant.vars['reward_trial2']
        reward3 = self.participant.vars['reward_trial3']
        reward4 = self.participant.vars['reward_trial4']
        reward5 = self.participant.vars['reward_trial5']
        reward6 = self.participant.vars['reward_trial6']
        total = round(reward1 + reward2 + reward3 + reward4 + reward5 + reward6, 2)
        return {
            'lang': lang,
            'reward1': reward1,
            'reward2': reward2,
            'reward3': reward3,
            'reward4': reward4,
            'reward5': reward5,
            'reward6': reward6,
            'total': total
        }


page_sequence = [Start, Period1, Period2, Period3, End4, Period4, End5, Period5, End6, Period6, End]
