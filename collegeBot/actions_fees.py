from rasa_core.actions import Action
from rasa_core.events import SlotSet


class Fees(Action):
    def name(self):
        return "action_fees"

    def run(self, dispatcher, tracker, domain):
        year = tracker.get_slot('fees_structure')
        fees_structure  = {'first': '$60,000', 'second': '$75,000', 'third': '$90,000', 'fourth': '$1,10,000'}
        result = fees_structure[year]
        response = """Your college fees for {} year is {}.""".format(year, result)
        dispatcher.utter_message(response)
        return[SlotSet('fees_structure', year)]