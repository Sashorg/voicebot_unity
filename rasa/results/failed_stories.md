## happy path 1
* greet: hello there!
    - utter_greet   <!-- predicted: action_hello -->
* mood_great: amazing
    - utter_happy


## happy path 2
* greet: hello there!
    - utter_greet   <!-- predicted: action_hello -->
* mood_great: amazing
    - utter_happy
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: action_bye -->


## sad path 1
* greet: hello
    - utter_greet   <!-- predicted: action_hello -->
* mood_unhappy: not good
    - utter_cheer_up
    - utter_did_that_help
* affirm: yes
    - utter_happy


## sad path 2
* greet: hello
    - utter_greet   <!-- predicted: action_hello -->
* mood_unhappy: not good
    - utter_cheer_up
    - utter_did_that_help
* deny: not really
    - utter_goodbye   <!-- predicted: action_bye -->


## sad path 3
* greet: hi
    - utter_greet   <!-- predicted: action_hello -->
* mood_unhappy: very terrible
    - utter_cheer_up
    - utter_did_that_help
* deny: no
    - utter_goodbye   <!-- predicted: action_bye -->


## say goodbye
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: action_bye -->


## bot challenge
* bot_challenge: are you a bot?   <!-- predicted: self: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_mood -->


