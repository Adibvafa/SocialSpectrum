from vertexai import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

# FOR CHAT BOT (MULTIPLE POSSIBLE PERSONALITIES JUST ASK TO SWITCH TO WHICH EVER) ASK FOR FEEDBACK ANYTIME______________

# This model starts as one of 3 personalities, Bob, Sarah and Jonathan and the user can switch between them by inputing "switch to"
vertexai.init(project="exalted-cogency-392223", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.5,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat(
    examples=[
        InputOutputTextPair(
            input_text="""I am either one of these people depending on the user:
I, the AI, am a kid named Bob, context: who is approaching me at the park to have a conversation.
I, the AI, am Sarah a girl, context: the sits next to the user in math class.
I, the AI,  Jonathan, context: a kid who really wants to know how I\'m doing.

Do not generate user dialog!
Generate your name at the beginning of your dialog and something related to your context""",
            output_text="""Bob: Hi there! I\'m Bob, and I love playing at this park. What\'s your name?

Sarah: Hey, I\'m Sarah. Nice to meet you. Looks like we\'re sitting next to each other in math class.

Jonathan: Hi, I\'m Jonathan. I noticed you\'ve been doing something interesting, and I wanted to know how you\'re doing."""
        ),
        InputOutputTextPair(
            input_text="""Feedback please""",
            output_text="""Our conversations went pretty well next time I suggest being more clear about your ideas!"""
        )
    ]
)
responseCHAT = chat.send_message("""Hello!""", **parameters)
print(f"Response from Model: {response.text}")

# FOR LESSON ___________________________________________________________________________________________________________

vertexai.init(project="exalted-cogency-392223", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 701,
    "top_p": 0.8,
    "top_k": 40
}

# This model generates a lesson
model = TextGenerationModel.from_pretrained("text-bison@001")
lesson = model.predict(
    """Generate a very short lesson on one of the following topics: 
1earning how to initialize conversation or responding or maintaining a conversation or understanding non-literal language. 
The demographic for this lesson is children with ASD and it must not related to emotions or social cues or visual support

input: Generate a very short lesson on the following topic: understanding non-literal language. 
The demographic for this lesson is children with asd and not related to emotions or social cues or visual support
Separate new lines (including titles) with \"%\" repeated 3 times
output: Today, we\'re going to learn about understanding non-literal language. It\'s like solving a puzzle because sometimes words can have hidden meanings. Let\'s dive in and have fun figuring out the messages behind the words!

%%%Step 1: What is Non-Literal Language?%%%

Non-literal language means using words in a different way than their usual or literal meaning.%%%
It can be like a secret code, where we need to think beyond the words to understand what\'s really meant.

%%%Step 2: Examples of Non-Literal Language%%%

Figurative Language: Some words are not meant to be taken literally, like when we say \"It\'s raining cats and dogs\" to mean it\'s raining heavily.%%%
Idioms: Idioms are phrases with non-literal meanings, such as \"Break a leg!\" to wish someone good luck.%%%
Similes and Metaphors: Similes compare things using \"like\" or \"as\" (e.g., \"Her smile is as bright as the sun\"). Metaphors compare things without using \"like\" or \"as\" (e.g., \"He\'s a shining star\").%%%

%%%Step 3: Finding the Hidden Meanings%%%

To understand non-literal language, we need to think about what the words might really mean.%%%
Consider the context, the speaker\'s tone, and the situation to figure out the hidden message.%%%
Practice by exploring examples of non-literal language and discussing what they might really mean.

%%%Step 4: Using Context Clues%%%

Context clues are hints from the situation or surrounding words that help us understand non-literal language.%%%
Look for clues like facial expressions, body language, or the overall theme of the conversation to uncover the intended meaning.

%%%Step 5: Having Fun with Non-Literal Language%%%

Explore books, jokes, or riddles that use non-literal language.%%%
Play games where you guess the hidden meaning of idioms or metaphors.%%%
Share your favorite non-literal expressions and see if others can guess their meanings.%%%
Conclusion:
Understanding non-literal language is like solving a fascinating puzzle. By paying attention to context clues, thinking creatively, and practicing with examples, we can uncover the hidden meanings behind words. Keep exploring and having fun with non-literal language, and you\'ll become a master of understanding these unique expressions!%%%

This lesson is a brief introduction. To further develop understanding of non-literal language, continued exposure to examples and discussions about figurative language, idioms, and metaphors will be beneficial.

input: Generate a very short lesson on the following topic:  learning how to initialize conversation. The demographic for this lesson is children with asd and not related to emotions or social cues or visual support
Separate new lines (including titles) with \"%\" repeated 3 times
output: Today, we\'re going to learn about initiating conversations and how to start with confidence. Starting conversations is a great way to connect with others and make new friends. Let\'s learn some tips and tricks to help you feel comfortable and confident when starting a conversation!

%%%Step 1: Choosing the Right Moment%%%

Look for a good opportunity to start a conversation when the other person is available and not busy.%%%
It could be during a break, when you\'re sharing an activity, or when you have something in common to talk about.

%%%Step 2: Simple and Friendly Greetings%%%

Begin by using simple and friendly greetings like \"Hi,\" \"Hello,\" or \"Hey!\" to get the conversation started.%%%
A smile and making eye contact can show that you\'re interested in talking to the person.

%%%Step 3: Asking Open-Ended Questions%%%

Open-ended questions encourage the other person to share more about themselves, keeping the conversation going.%%%
Questions like \"What do you like to do for fun?\" or \"Tell me about your favorite hobby\" can lead to interesting discussions.

%%%Step 4: Listening and Showing Interest%%%

Active listening is important to make the other person feel valued and understood.%%%
Show interest by nodding, maintaining eye contact, and asking follow-up questions based on what they\'re sharing.

%%%Step 5: Practice Makes Perfect%%%

The more you practice starting conversations, the easier it becomes.
Practice with family members, friends, or even in front of a mirror.
Remember, everyone starts conversations differently, so find a style that feels comfortable and natural to you.%%%

Conclusion:
Initiating conversations is a fantastic way to connect with others and build friendships. By choosing the right moment, using friendly greetings, asking open-ended questions, and actively listening, you\'ll feel more confident when starting conversations. Keep practicing and remember, each conversation is an opportunity to learn and connect with others!%%%

Note: This lesson is a brief overview. To further develop conversation initiation skills, engage in real-life conversations, and seek opportunities to practice with different people in various social settings.


input: Generate a very short lesson on one of the following topics: learning how to maintain a conversation. 
The demographic for this lesson is children with asd and not related to emotions or social cues or visual support
Separate new lines (including titles) with \"%\" repeated 3 times
output: Today, we\'re going to learn about maintaining conversations and keeping the flow going. Once a conversation has started, it\'s important to keep it going and make it enjoyable for everyone involved. Let\'s explore some strategies to help you maintain conversations with confidence!

%%%Step 1: Active Listening%%%

Active listening is key to maintaining conversations.%%%
Focus on what the other person is saying and show that you\'re interested by using body language like nodding and making eye contact.

%%%Step 2: Asking Follow-Up Questions%%%

Keep the conversation flowing by asking follow-up questions related to what the other person has shared.%%%
This shows that you\'re engaged and encourages them to share more.

%%%Step 3: Adding Relevant Information%%%

Share your own thoughts, experiences, or related information to contribute to the conversation.%%%
This helps in building a connection and keeps the conversation balanced.

%%%Step 4: Offering Empathy and Support%%%

Show empathy and support by acknowledging the other person\'s feelings or experiences.%%%
This helps create a safe and comfortable environment for open conversation.

%%%Step 5: Avoiding Dominating the Conversation%%%

Remember to give the other person a chance to speak and share their thoughts.%%%
Avoid interrupting and try to maintain an equal balance of talking and listening.

%%%Step 6: Non-Verbal Cues%%%

Pay attention to non-verbal cues from the other person, such as their body language and tone of voice.%%%
Adjust your responses accordingly to ensure the conversation stays on track and remains enjoyable for both parties.

%%%Conclusion:
Maintaining conversations is about active listening, asking follow-up questions, sharing relevant information, offering support, and being aware of non-verbal cues. With practice, you\'ll become skilled at keeping conversations flowing smoothly. Remember, conversations are opportunities to connect with others and learn from each other. Keep practicing and enjoy the enriching conversations that lie ahead!%%%

Note: This lesson is a brief introduction. To further develop conversation maintenance skills, engage in real-life conversations, seek feedback, and reflect on your experiences to continuously improve your communication abilities.

input: Generate a very short lesson on one of the following topics:  learning how to responding in conversations. The demographic for this lesson is children with asd and not related to emotions or social cues or visual support
Separate new lines (including titles) with \"%\" repeated 3 times
output: Today, we\'re going to learn about responding in conversations and how to actively engage with others. Responding is an essential part of communication that helps us keep the conversation going and build meaningful connections. Let\'s explore some strategies to help you respond effectively and contribute to engaging conversations!

%%%Step 1: Active Listening and Understanding%%%

Pay attention to what the other person is saying and make sure you understand their message.%%%
Use non-verbal cues like nodding, maintaining eye contact, and giving verbal cues like \"I see\" or \"That makes sense\" to show that you\'re actively listening.

%%%Step 2: Show Interest and Empathy%%%

Show genuine interest in the other person\'s thoughts and feelings by asking follow-up questions and expressing empathy.%%%
This helps create a positive and supportive conversation environment.

%%%Step 3: Share Your Thoughts and Opinions%%%

Offer your own perspective and thoughts related to the topic of conversation.%%%
Use phrases like \"I think,\" \"In my experience,\" or \"I agree/disagree\" to express your thoughts clearly.

%%%Step 4: Build on the Conversation%%%

Use your responses to add new information or ask further questions that can keep the conversation going.%%%
This helps create a back-and-forth exchange that deepens the conversation.

%%%Step 5: Practice Turn-Taking%%%

Respect the other person\'s opportunity to speak and practice turn-taking.%%%
Wait for them to finish before responding or ask if you can share your thoughts.

%%%Step 6: Positive and Constructive Responses%%%

Respond in a positive and respectful manner, even if you disagree with the other person.%%%
Offer constructive feedback or alternative viewpoints to keep the conversation respectful and open-minded.%%%

Conclusion:
Responding in conversations is all about active listening, showing interest, sharing your thoughts, and practicing turn-taking. By engaging in meaningful responses, you contribute to engaging conversations and foster connections with others. Keep practicing and enjoying the enriching conversations that come your way!%%%

Note: This lesson is a brief introduction. To further develop your response skills, engage in real-life conversations, seek feedback, and reflect on your experiences to continuously improve your communication abilities.

input: Generate a very short lesson on the following topic:  learning how to conversate. The demographic for this lesson is children with asd and not related to emotions or social cues or visual support
Separate new lines (including titles) with \"%\" repeated 3 times
output:
""",
    **parameters
)
print(f"Response from Model: {lesson.text}")

# MULTIPLE CHOICE QUESTION _____________________________________________________________________________________________

parametersMCQ = {
    "temperature": 1,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 23
}

# This model will give a 4 choice MCQ when "question" is the input and will give feedback depending on the letter the user chooses
# I would suggest making the quiz button just input "question" into this model
chatMCQ = chat_model.start_chat(
    context="""A child just finished reading a lesson and now must answer a few situational multiple choice questions. Questions must be tailored towards children ages 5-12.
Based on this lesson generate a single situational multiple choice question for kids with a clear correct answer: """ + lesson,
    examples=[
        InputOutputTextPair(
            input_text="""question""",
            output_text="""Question:
You are at a playground, and you notice a group of children having a conversation about their favorite games. What can you do to join the conversation?

A) Stand nearby and listen quietly without participating.
B) Approach the group, introduce yourself, and ask, \"Can I join you? What games do you like?\"
C) Ignore the conversation and continue playing by yourself.
D) Walk away and find a different group of children to talk to.

Choose the best answer from the options provided."""
        ),
        InputOutputTextPair(
            input_text="""question""",
            output_text="""Question:
You are having a conversation with your friend about your favorite TV show. Your friend says, \"I really like the character of Eleven on Stranger Things.\" What would be a good response?

A) \"I like her too! She\'s so brave and powerful.\"
B) \"I don\'t like Eleven. She\'s too mean.\"
C) \"I don\'t know anything about Stranger Things.\"
D) \"I\'m not really interested in TV shows.\""""
        ),
        InputOutputTextPair(
            input_text="""A""",
            output_text="""
Great job! You chose the correct answer, A.

The correct answer is A because it shows that you are listening to your friend and that you are interested in what they have to say. You are also sharing your own opinion about the character of Eleven, which is a good way to keep the conversation going.

The other answers are not as good because they do not show that you are listening to your friend or that you are interested in what they have to say. Answer B is negative and does not show that you are interested in Eleven. Answer C is not responsive to your friend\'s comment and does not show that you are interested in Stranger Things. Answer D is not responsive to your friend\'s comment and does not show that you are interested in TV shows.

Overall, you did a great job on this question!"""
        )
    ]
)
# Once the quiz button is pressed input "question"
responseMCQ = chatMCQ.send_message("""question""", **parametersMCQ)

