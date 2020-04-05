## happy path
* greet
  - action_hello
* mood_great
  - utter_happy

## sad path 1
* greet
  - action_hello
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - action_hello
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - action_bye

## say goodbye
* goodbye
  - action_bye

## asking hello + mood
* greet
  - action_hello
* self
  - utter_mood
## asking mood
* self
  - utter_mood

## asking mood+bye
* self
  - utter_mood
* goodbye
  - action_bye  
## hi+ asking mood+bye
* greet
  - action_hello
* self
  - utter_mood
* goodbye
  - action_bye  
## what aboutt bob
* opinion{"name":"Bob"}
  - action_bob_opinion
  
  
## what abou Tom
* opinion{"name":"Tom"}
  - utter_tom_opinion
  
  
## what  Kenny
* opinion{"name":"Kenny"}
  - action_bob_opinion
  
## hi what aboutt bob
* greet
  - action_hello
* opinion{"name":"Bob"}
  - action_bob_opinion
  
  
## hi  what abou Tom
* greet
  - action_hello
* opinion{"name":"Tom"}
  - action_bob_opinion
  
  
## hi what  Kenny
* greet
  - action_hello
* opinion{"name":"Kenny"}
  - action_bob_opinion
## hi what aboutt bob bye
* greet
  - action_hello
* opinion{"name":"Bob"}
  - action_bob_opinion
* goodbye
  - action_bye  
  
## hi  what abou Tom bye
* greet
  - action_hello
* opinion{"name":"Tom"}
  - action_bob_opinion
* goodbye
  - action_bye  
  
## hi what  Kenny bye
* greet
  - action_hello
* opinion{"name":"Kenny"}
  - action_bob_opinion
* goodbye
  - action_bye

##  what aboutt bob bye
* greet
  - action_hello
* opinion{"name":"Bob"}
  - action_bob_opinion
* goodbye
  - action_bye  
  
##   what abou Tom bye
* greet
  - action_hello
* opinion{"name":"Tom"}
  - action_bob_opinion
* goodbye
  - action_bye  
  
##  what  Kenny bye
* greet
  - action_hello
* opinion{"name":"Kenny"}
  - action_bob_opinion
* goodbye
  - action_bye