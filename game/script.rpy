# The script of the game goes in this file. hell

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Yuki")
define b = Character("???")
define y = Character("You")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene sun:
       "images/sunSky.png"
       zoom 1.51
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    image sprite1 :
      "images/sprite1.jpg"

    image sprite2 :
       "images/yukiNormal.png" 
    image yukiHappy :
       "images/yukiHappy.png"
    image yukiStare :
       "images/yukiStare.png"
    image yukiBlink :
       "images/yukiBlink.png"


    # Add the yuki images to different spots, finish endings, also add all images to here as sprites.
    image sUmbrella :
        "images/sUmbrella.jpg"
    image iTruck :
        "images/iTruck.png"
        zoom 0.6

    show sprite2 at center:
        zoom 0.8

    # These display lines of dialogue.

    e "its a sunny day,"
    hide sprite2
    show yukiBlink at center:
        zoom 0.8

    e "however, I don't like sun. It's too bright,"

    e "Too warm."

    hide yukiBlink
    show sprite2 at center:
        zoom 0.8
    e "I can never enjoy the sun like how others describe it."

    e "I never understand how sun can be joyful."
  
    hide sprite2
    show yukiBlink at center:
        zoom 0.8
    e "Oh.. "

    e "I'm really sorry about that. I lost myself a little"

    e "Can you please help me with something?"

    hide yukiBlink
    show sprite2 at center:
        zoom 0.8
    e "I promise it's nothing weird!"
    menu: 
        "Will you help Yuki?"
        "Sure, why not?":
             jump umbrella
        "No I just met you.":
             jump end1
    return

    label end1:
    hide sprite2
    show yukiBlink at center:
        zoom 0.8
    e "Oh, that's okay..."

    e "I'm really sorry!"

    e "That was a stupid request."
    hide yukiBlink
    show yukiStare at center:
        zoom 0.8
    e "Well, have a nice day?"
    hide yukiStare
    b "BAD ENDING(No interest)"
    return
    

    label umbrella:
    hide sprite2
    show yukiStare at center:
        zoom 0.8

    e "Oh,"

    e "Really?"
    hide yukiStare
    show yukiHappy at center: 
        zoom 0.8

    e "That's... really nice of you!"

    e "Not many people help someone that they don't know..."
    hide yukiHappy
    show sprite2 at center:
        zoom 0.8
    e "Anyways! As I was saying,"
    hide sprite2
    show yukiBlink at center:
        zoom 0.8
    e "I'm not feeling very well."

    e "The sun is feeling a bit hot today."
    hide yukiBlink
    show sprite2 at center:
       zoom 0.8
    e "What do you think I should do?"
 
    menu:
       "What will you tell Yuki in order to stay cool?"
       "How about eating/drinking something cold?":
            jump cTreat
       "I think you should go somewhere cold.":
            jump place
       "Maybe buy a hand fan?":
            jump fan 
       "I'm not really sure":
            jump hesitant
       "Figure it out.":
            jump problem




    label cTreat:
    
    y "How about eating something cold?"
    hide sprite2
    show yukiStare at center:
        zoom 0.8
    e "Oh,"
    hide yukiStare
    show yukiHappy at center: 
        zoom 0.8
    e "That's actually not a bad idea!"
    hide yukiHappy
    show sprite2 at center:
        zoom 0.8
    e "But what could we..."

    e "Oh look!"

    menu:
       "Oh look!"
       "Where?":
          jump icecream
       "I don't see anything.":
          jump icecream
       "Uhhh...":
          jump icecream

    label icecream: 

    e "Right there!"
   
    show iTruck:
        xpos 50
        ypos 520
       
    e "See?"

    e "There's an ice cream truck!"
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "Let's go buy ice cream!" 
    hide yukiHappy
    show sprite2 at center:
        zoom 0.8
    e "What ice cream flavour do you like?"     

    menu:
      "Choose an icecream flavour:"  
      "Chocolate":
          jump iChocolate
      "Vanilla":
          jump iVanilla
      "Strawberry":
          jump iStrawberry
      "Banana ice cream with dark chocolate chips and mint whipped cream frosting as well as caramel dressing and a kiwi piece on top":
          jump iLong

    label iChocolate:
    y "I want chocolate ice cream."
    hide sprite2
    show yukiHappy at center:
       zoom 0.8
    e "Ooo, so you're a chocolate person"

    e "That's awesome!"
    hide yukiHappy
    show sprite2 at center:
        zoom 0.8
    e "Chocolate is a pretty famous flavour."
    hide sprite2
    show yukiHappy at center:
        zoom 0.8
    e "I'm gonna get vanilla ice cream then!"
    
    jump talk1
    
    label iVanilla:
    y "I want vanilla ice cream."
    hide sprite2
    show yukiStare at center:
     zoom 0.8
    e "Woah, vanilla?"
    hide yukiStare
    show yukiHappy at center:
      zoom 0.8
    e "I like vanilla too!"

    e "I'm so happy to find another vanilla lover."

    jump talk1

    label iStrawberry:
    y "I want strawberry ice cream."

    e "Strawberry?"
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "That's a good choice!"
    hide yukiHappy
    show yukiBlink at center:
      zoom 0.8
    e "I barely see anyone with a strawberry taste,"
    hide yukiBlink
    show yukiHappy at center:
      zoom 0.8
    e "I'm gonna get vanilla."
    jump talk1

    label iLong:
    y "I want banana ice cream with dark chocolate chips and mint whipped cream frosting as well as caramel dressing."
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "..."

    y "And a kiwi on top."

    e "... That's..."
    
    e "I love how specific you are...?"
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    e "I mean uh.."

    e "Sure you do you!"
    hide yukiBlink
    show yukiStare at center:
     zoom 0.8
    e "I should..."

    e "Definitely give that a try!"
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    e "Another time..."
    hide yukiBlink
    show yukiStare at center:
      zoom 0.8
    e "I'll stick to vanilla for today." 
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    e "..."
    hide iTruck
    jump talk1
  


    label place:
    
    y "I think you should go somewhere cold."
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "I like that idea,"

    e "It makes me feel so cozy to think abouy not being in the sun!"

    e "No suffering, no burning, all cold and-"

    y "Are you okay...?"
    hide yukiHappy
    show yukiStare at center:
     zoom 0.8
    e "..."
    
    e "Oh yeah, sorry about that."
    hide yukiStare
    show yukiBlink at center:
     zoom 0.8
    e "Forget about that, okay?"
    hide yukiBlink
    show sprite2 at center:
     zoom 0.8
    e "I'm not sure where I can go though..."

    menu:
     "Where can Yuki go?"
     "Cafe nearby":
        jump pCafe
     "Lake":
        jump pLake
     "My house":
        jump pHouse
     
    label pCafe:
    
    y "Maybe you should go to that cafe over there!"

    e "That cafe?"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "You mean the quiet one?"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "We could go there, I don't think it should be bad."
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "Let's go!"
    

    #Cafe scene not done yet
    scene cafe:
     "images/Cafe.jpg"
     zoom 2.6
    
    show sprite2 at center:
     zoom 0.8

    e ""
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "We're here!"

    e "It's colder in here!"

    e "So cold..."

    e "Really cozy..."

    y "Ahem."
    hide yukiHappy
    show yukiStare at center:
      zoom 0.8
    e "Oh I'm sorry!"
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    e "Ignore... That."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "Okay! let's rest here for a while."
    jump talk3


    label pLake:
    y "Maybe you should jump in a lake or-"
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "What???"

    e "What do you-"
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    e "You know what it's okay..."

    e "At the end you're gonna be the one who burns."

    e "We all eventually burn."
    
    e "No one can escape that."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "But you..."

    e "..."

    y "What?"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "Have a good day."

    hide yukiBlink
    
    b "Well I don't think telling someone like her to jump in a lake was smart."

    b "Just don't let her see you again."

    b "BAD ENDING(Lake)."
    return


    label pHouse:
    
    y "Do you want to come to my-"
    
    e "House?"

    y "I mean-"
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "Ofcourse I want to come to your house!"

    e "I bet it's so cold,"

    e "So cozy,"

    e "With no sunlight, pure darkness,"
    hide yukiHappy
    show sprite2 at center:
      zoom 0.8
    y "Actually-"
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "That's wonderful! Let's get going now!"

    y "... If you want to...?"

    jump talk4



    label fan:
    
    y "Maybe you should buy a hand fan?"
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "A hand fan?"
    hide yukiStare
    show yukiBlink at center:
     zoom 0.8
    e "But where can I buy those from?"

    y "I'm not sure..."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "I'll go check the store nearby,"

    e "I'll be right back"
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "Don't go."

    y "Sure?"

    hide yukiStare
    
    y "..."

    y "How long will it take..."

    y "Should I lea-"

    show yukiHappy at center:
     zoom 0.8
 
    e "I'm back!"

    y "What took you so long?"
    hide yukiHappy
    show sprite2 at center:
     zoom 0.8
    e "I needed to make sure I was cooled down before coming out of the store!"
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "It's really warm out here after all."
    hide yukiStare
    show sprite2 at center:
      zoom 0.8
    y "I see."
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "Great! Thank you for your advice!"
    jump talk1



    label hesitant:
    
    y "I don't know..."
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "Why?"
  
    e "But you offered to help..."
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    y "Look, I'm really sorry."
    
    e "That's okay."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "I have an idea..."

    y "What is it?"
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "What if you cool me down?"
    hide yukiStare
    show sprite2 at center:
      zoom 0.8
    y "What??? I'm no-"
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "Yay! Can you please act as a fan?"
    hide yukiHappy
    show sprite2 at center:
      zoom 0.8
    y "A fan?"
    hide sprite2 
    show yukiHappy at center:
      zoom 0.8
    e "Yes! A fan!" 
    hide yukiHappy
    show sprite2 at center:
      zoom 0.8
    y "How am I supposed to do that?"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "With your hands!"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "You know how when you feel hot you shake your hands to feel cold?"

    y "I'm not gonna-"
    hide sprite2 
    show yukiHappy at center:
      zoom 0.8
    e "Thank you so much! I really appreciate it!"

    y "... Okay..."

    e "..."

    jump talk1

    label problem:
    
    y "Figure it out."
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "What?"

    e "Didn't you offer to help me?"

    y "Why would I help a stranger?"

    e "You-"

    e "..."
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    e "That's Okay..."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "You're the one that will burn."

    e "Not right now, but..."
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "Eventually."

    e "In the near future,"

    e "I will be able to see it,"

    e "And at that time,"
    
    e "Only thing left will be ashes."
    hide yukiStare 
    show yukiBlink at center:
      zoom 0.8
    e "Have a nice day."

    hide yukiBlink

    b "You really made her angry"

    b "Just watch out for her from now on."

    b "Don't let her see you for a while at least."

    b "Hopefully you'll be okay."

    b "BAD ENDING(Storm Off)."
    return


    label talk1:
     hide iTruck
    hide yukiHappy
    hide yukiBlink
    hide yukiStare
    # add the background right here!
    scene sunset:
      "images/sunset.png"
      zoom 1
    show sprite2 at center:
      zoom 0.8
    e "Hey..."

    e "Do you like the sun?" 

    menu:
      "Do you like the sun?"
      "Yes":
        jump sLike
      "No":
        jump sHate

    label sHate:
    y "No, I hate the sun."

    e "Really?"

    e "You do?"

    e "Wow,"
    hide sprite2
    show yukiHappy at center:
      zoom 0.8
    e "I never really thought I would find someone that hates it as well."
    hide yukiHappy
    show sprite2 at center:
      zoom 0.8
    e "Sun just feels way too warm."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "It's really bright, it burns my eyes."

    e "I don't think I ever really enjoyed it."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "Well, maybe when I was younger?"

    e "Things were different when I was younger,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "And I never really found out what in particular changed."
    hide yukiBlink
    show sprite2 at center:
     zoom 0.8
    e "Wait..."

    e "So if you don't like the sun,"

    e "What weather do you like?"

    menu:
     "What weather do you like?"
     "Rainy":
       jump rainy
     "Cloudy":
       jump cloudy
     "Snowy":
       jump snowy
     "Foggy":
       jump foggy
     "I just like the night.":
       jump lNight
     "I don't like any weather.":
       jump noWeather
     
    label rainy:
    y "I like rainy weather."

    e "You do?"
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "I agree with you."

    e "Rain feels really soothing"
    hide yukiHappy
    show yukiBlink at center:
      zoom 0.8
    e "The weather feels calm and cool when it rains,"

    e "It's like a blessing."
    hide yukiBlink
    show yukiHappy at center:
      zoom 0.8
    e "I really like snowy weather."

    e "It looks really beautiful to me,"
    hide yukiHappy
    show sprite2 at center:
      zoom 0.8
    e "Also, It is fun to play with!"
    
    e "I like rain as well,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "But snow is my favourite!"
    hide yukiBlink
    show yukiHappy at center:
      zoom 0.8
    e "Thinking about snow makes me really happy,"
    hide yukiHappy
    show sprite2 at center:
      zoom 0.8
    e "But it never snows here anyway, "
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "So there's not really anything to be excited for."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "Everytime people think it's going to snow,"
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "It never does."

    e "It's like a bad luck"
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    e "A curse."
    hide yukiBlink
    show yukiStare at center:
      zoom 0.8
    e "That's another reason on why I don't like sun."
    hide yukiStare
    show sprite2 at center:
      zoom 0.8
    e "It stops the beauty of snow,"

    e "It melts it away,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "It takes away that joy from me."

    e "And yet..."
    
    e "People still prefer sun."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "Every day,"

    e "All day,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "All year"

    e "They want sun,"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "And I am always the bad person,"

    e "Is it because I yearn for snow?"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "Am I selfish for not wanting sun?"

    e "Is it selfish to not want something that people get everyday, to want something precious to me for only one day?"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "How am i selfish?"
   
    e "Am I selfish?"

    e "..."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "I'm sorry, I lost myself again."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "I wish there was a way that it could snow,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "But I haven't seen snow in years now."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "All I wish for is to see snow for one last time."
    
    e "..."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "Anyways,"
    hide yukiBlink
    show sprite2 at center:
     zoom 0.8
    e "Thank you for talking to me,"

    e "It eases me to see that I am not alone and that there is someone else that does not like the sun."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "I'll see what waits for me tonight,"
    hide yukiBlink
    show sprite2 at center:
     zoom 0.8
    e "Maybe it finally snows, who knows?"
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "Maybe I can finally see my snow again."
    hide yukiHappy
    show sprite2 at center:
     zoom 0.8
    e "Or maybe I can become one with my snow tonight..."
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "That would be so beautiful."

    e "I hope you have a wonderful day!"
    jump snowNight


    label cloudy:
    y "I like cloudy weather."

    e "Cloudy?"
    hide sprite2
    show yukiBlink at center:
     zoom 0.8
    e "I see, so you just want sunlight to be gone."
    hide yukiBlink
    show sprite2 at center:
     zoom 0.8
    e "Cloudy weather is good as well!"
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "It is cool and feels comfortable."

    e "I really like snowy weather."

    e "It looks really beautiful to me,"
    hide yukiHappy
    show sprite2 at center:
      zoom 0.8
    e "Also, It is fun to play with!"
    
    e "I like cloudy weather as well,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "But snow is my favourite!"
    hide yukiBlink
    show yukiHappy at center:
      zoom 0.8
    e "Thinking about snow makes me really happy,"
    hide yukiHappy
    show sprite2 at center:
      zoom 0.8
    e "But it never snows here anyway, "
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "So there's not really anything to be excited for."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "Everytime people think it's going to snow,"
    hide sprite2
    show yukiStare at center:
      zoom 0.8
    e "It never does."

    e "It's like a bad luck"
    hide yukiStare
    show yukiBlink at center:
      zoom 0.8
    e "A curse."
    hide yukiBlink
    show yukiStare at center:
      zoom 0.8
    e "That's another reason on why I don't like sun."
    hide yukiStare
    show sprite2 at center:
      zoom 0.8
    e "It stops the beauty of snow,"

    e "It melts it away,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "It takes away that joy from me."

    e "And yet..."
    
    e "People still prefer sun."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "Every day,"

    e "All day,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "All year"

    e "They want sun,"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "And I am always the bad person,"

    e "Is it because I yearn for snow?"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "Am I selfish for not wanting sun?"

    e "Is it selfish to not want something that people get everyday, to want something precious to me for only one day?"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "How am i selfish?"
   
    e "Am I selfish?"

    e "..."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "I'm sorry, I lost myself again."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "I wish there was a way that it could snow,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "But I haven't seen snow in years now."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "All I wish for is to see snow for one last time."
    
    e "..."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "Anyways,"
    hide yukiBlink
    show sprite2 at center:
     zoom 0.8
    e "Thank you for talking to me,"

    e "It eases me to see that I am not alone and that there is someone else that does not like the sun."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "I'll see what waits for me tonight,"
    hide yukiBlink
    show sprite2 at center:
     zoom 0.8
    e "Maybe it finally snows, who knows?"
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "Maybe I can finally see my snow again."
    hide yukiHappy
    show sprite2 at center:
     zoom 0.8
    e "Or maybe I can become one with my snow tonight..."
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "That would be so beautiful."

    e "I hope you have a wonderful day!"
    jump snowNight

    

    label snowy:
    y "I like snowy weather."
    hide sprite2
    show yukiStare at center:
     zoom 0.8
    e "You do?"

    e "Actually?"
    hide yukiStare
    show sprite2 at center:
     zoom 0.8
    e "That's insane!"
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "I like snowy weather as well!"
    
    e "It is my favourite weather in the whole world!"
    hide yukiHappy
    show sprite2 at center:
     zoom 0.8
    e "My favourite... thing... in the whole world."
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "Thinking about snow makes me really happy,"
    hide yukiHappy
    show sprite2 at center:
     zoom 0.8
    e "But it never snows here anyway, "
    hide sprite2
    show yukiBlink at center:
     zoom 0.8
    e "So there's not really anything to be excited for."

    e "Everytime people think it's going to snow,"
    hide yukiBlink
    show sprite2 at center:
     zoom 0.8
    e "It never does."

    e "It's like a bad luck"
    hide sprite2
    show yukiBlink at center:
     zoom 0.8
    e "A curse."

    e "That's another reason on why I don't like sun."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8 
    e "It stops the beauty of snow,"

    e "It melts it away,"
    hide sprite2
    show yukiBlink at center:
     zoom 0.8
    e "It takes away that joy from me."

    e "And yet..."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "People still prefer sun."

    e "Every day,"

    e "All day,"

    e "All year"
    hide sprite2
    show yukiBlink at center:
     zoom 0.8
    e "They want sun,"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "And I am always the bad person,"
    hide sprite2 
    show yukiBlink at center:
     zoom 0.8
    e "People like us are always the bad people,"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "Is it because I yearn for snow?"

    e "Am I selfish for not wanting sun?"

    e "Is it selfish to not want something that people get everyday, to want something precious to me for only one day?"

    e "How am i selfish?"
   
    e "Am I selfish?"

    e "..."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "I'm sorry, I lost myself again."
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "I wish there was a way that it could snow,"
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "But I haven't seen snow in years now."
    hide yukiBlink
    show sprite2 at center: 
      zoom 0.8
    e "All I wish for is to see snow for one last time."

    e "..."
    hide sprite2
    show yukiBlink at center:
      zoom 0.8
    e "Anyways,"

    e "Thank you for talking to me,"
    hide yukiBlink
    show sprite2 at center:
      zoom 0.8
    e "I'm really glad that someone else feels like me."

    e "I'll see what waits for me tonight,"

    e "Maybe it finally snows, who knows?"
    hide sprite2
    show yukiHappy at center:
     zoom 0.8
    e "Maybe I can finally see my snow again."
    hide yukiHappy
    show sprite2 at center:
     zoom 0.8
    e "Or maybe I can become one with my snow tonight..."
    hide sprite2
    show yukiHappy at center: 
      zoom 0.8
    e "Or, maybe we can both become one with the snow!"

    e "Wouldn't that be amazing?"

    e "Wouldn't that be beautiful?"

    e "Or maybe pa-"
    hide yukiHappy
    show yukiStare at center:
      zoom 0.8
    e "Or maybe we can play in the snow!"
    hide yukiStare
    show yukiHappy at center:
     zoom 0.8
    e "Together!"

    e "All of us!"
 
    y "..."

    e "I hope you have a wonderful day."
    jump snowDark

    return

    label foggy:
    y "I like foggy weather."

    e "Foggy weather?"

    e "That's so pretty!"

    e "I sometimes feel really empty when the weather is foggy,"

    e "Emotionally. But in a beautiful way, It's calming in a way."
    return

    label lNight:
    e "Test night."
    return

    label noWeather:
    e "Test no weather"
    return

    label sLike:
    e "Test"
    return

    label talk3:
    e "Test"
    return

    label talk4:
    e "Test"
    return

    label snowNight:
    e "Test snow night"
    return

    label snowDark:
    e "Test snow dark"
    return