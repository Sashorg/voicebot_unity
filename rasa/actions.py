# custom Python code.
# This files contains your custom actions which can be used to run
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
#
#
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# print(bot_name['name'])
# print(distros_dict[bot_name['name']]['action_hello'])
print('__________________________________')
# print(bot_name['bot'])

class ActionHello(Action):

    def name(self) -> Text:
        return "action_hello"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('info_char.json', 'r') as f:
            distros_dict = json.load(f)
        with open('who_is_bot.json', 'r') as f:
            bot_name = json.load(f)
        reply=distros_dict[bot_name['name']]['action_hello']
        dispatcher.utter_message(text=reply)

        return []
class ActionBye(Action):

    def name(self) -> Text:
        return "action_bye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('info_char.json', 'r') as f:
            distros_dict = json.load(f)
        with open('who_is_bot.json', 'r') as f:
            bot_name = json.load(f)
        reply = distros_dict[bot_name['name']]['action_bye']
        dispatcher.utter_message(text=reply)

        return []

class ActionOpinion(Action):

    def name(self) -> Text:
        return "action_bob_opinion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('info_char.json', 'r') as f:
            distros_dict = json.load(f)
        with open('who_is_bot.json', 'r') as f:
            bot_name = json.load(f)
        try:
            if(len(tracker.latest_message['entities'])!=0):
                print(tracker.latest_message['entities'][0]['value'])
                whom = str(tracker.latest_message['entities'][0]['value']).lower()
            else:
               reply="Who?"
               return
            print(bot_name['name'])
# if you want to use different answers, just use random nubber here, and add the aswers to json
            reply = distros_dict[bot_name['name']]['action_opinion'][whom]
            print(distros_dict[bot_name['name']]['action_opinion'][whom])
        except KeyError:
            reply="I do not know about whom you are speaking"
            print("KIKIKIKIK")
        dispatcher.utter_message(text=reply)

        return []

