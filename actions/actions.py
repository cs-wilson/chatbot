# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,AllSlotsReset, Restarted
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []



class ActionFoodMenu(Action):

    def name(self):
        # action的名字
        return "action_foodmenu"

    def run(
        self,
        dispatcher,  # type: CollectingDispatcher
        tracker,  # type: Tracker
        domain,  # type:  Dict[Text, Any]
    ):

        # 获取实体menu_name的值
        menu_name = tracker.get_slot("food_menu")
        print(tracker)
        print("知道{}了".format(menu_name))
        # 若是菜名存在
        if menu_name:
            dispatcher.utter_template("{}的做法如下".format(menu_name))
            return []
        else:
            dispatcher.utter_message("我没听清，您需要重新点一下啊")
            return []
