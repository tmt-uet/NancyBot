## Chào - tên - hỏi chức năng - chào
* greet
  - utter_greet
* ask_name
  - utter_ask_name
* ask_func_list
  - utter_func_list
* bye
  - utter_bye

## Chào  - hỏi chức năng - chào
* greet
  - utter_greet
* ask_func_list
  - utter_func_list
* bye
  - utter_bye

## Chào  - hỏi tên - chào
* greet
  - utter_greet
* ask_name
  - utter_ask_name
* bye
  - utter_bye

## Hỏi tên - hỏi chức năng
* ask_name
  - utter_ask_name
* ask_func_list
  - utter_func_list

## Cảm ơn
* thank
  - utter_thank

## fallback story
* out_of_scope
  - action_default_fallback

## hỏi thời tiết-hỏi thời tiết cụ thể-chào
* ask_weather
  - utter_ask_weather
* ask_weather_location
  - action_weather_location

## hỏi thời tiết cụ thể
* ask_weather_location{"location": "Hà Nội"}
  - action_weather_location

## New Story

* greet
    - utter_greet
* ask_weather
    - utter_ask_weather
* ask_weather_location{"location":"seoul"}
    - slot{"location":"seoul"}
    - action_weather_location

## New Story

* greet
    - utter_greet
* ask_weather_location{"location":"hà_nội"}
    - slot{"location":"hà_nội"}
    - action_weather_location
