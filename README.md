# voicebot_unity
union of rasa chatbot plus multicharacter unity project
The idea is simple, we take open-source chatbot platform rasa, train it with simple conversation and inject in unity. 
in NLU.md file we insert possible questions and replies of user(player), where topic of speech is intent, for example:


intent:greet

  hey</n>
  hello
  hi  
  holla 
  howdy
  good morning
  good evenin 
  What's up 
  Good afternoon
  hey there


Then we write all possible stories in stories.md file. In my case I want super simple conversation, and for bot to be able to distinct who is he. This problem is solved ny using custom actions for everything, as every actions we will access json file of given by unity character and access second json file, with name of character. 

https://medium.com/analytics-vidhya/integrating-rasa-open-source-chatbot-into-unity-part-1-the-connection-9ba582c804cd
 this article was used in order to coonect unity to rasa server. 
 
 then,in Unity, with Windwows Speech Dictation library we will listen our sentences, convert them into text and pass to Rasa server. after getting reply, we check whether we have audio with the text, which we get, and if we have we play it. 
