# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# zfrom rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests


class ActionWeather(Action):
    def name(self):
        return "action_weather_location"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        if "_" in location:
            print("yes")
        location = location.replace("_", " ")
        print(location)
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=d0481c916f3aa50de69335bf7648db4f&units=metric".format(
            location
        )
        res = requests.get(url)
        data = res.json()
        if len(data) > 2:
            # JSON data works just similar to python dictionary and you can access the value using [].
            current_temperature = data["main"]["temp"]
            wind = data["wind"]["speed"]
            desc = data["weather"][0]["description"]
            weather, remind = self.translate_weather(desc)
            response = """ Thời tiết ở {} hôm nay: trời {}. Nhiệt độ {} °C, tốc độ gió: {} m/s. {}""".format(
                location, weather, current_temperature, wind, remind
            )
            dispatcher.utter_message(response)
        else:
            dispatcher.utter_message("City Not Found ")

    def translate_weather(self, weather):
        weather_translated = weather
        remind = "Bạn nên mang theo ô, áo mưa khi ra đường nhé !"
        if "clouds" in weather:
            weather_translated = "nhiều mây"
            remind = "Bạn nên mang theo ô, áo mưa khi ra đường nhé !"
        if "windy" in weather:
            weather_translated = "có gió nhẹ"
            remind = "Bạn nên đeo kính và dùng khẩu trang nhé !"
        if "stormy" in weather:
            weather_translated = "bão"
            remind = "Nghỉ làm 1 hôm ở nhà cho an toàn bạn nhé !"
        if "sunny" in weather:
            weather_translated = "nắng"
            remind = "Bạn nhớ mang mũ hoặc ô đi nhé"
        if "clear" in weather:
            weather_translated = "quang"
            remind = "Nếu bạn có lịch dã ngoại vào hôm nay thì rất tuyệt vời đấy !"
        if "rain" in weather:
            weather_translated = "mưa"
            remind = "Bạn nên mang theo ô, áo mưa khi ra đường nhé !"
        if "drizzle" in weather:
            weather_translated = "mưa phùn"
            remind = "Bạn nên mang theo ô, áo mưa khi ra đường nhé !"
        if "fog" in weather:
            weather_translated = "sương mù"
            remind = "Bạn nên mang theo mũ và lái xe cẩn thận nhé !"
        return weather_translated, remind
