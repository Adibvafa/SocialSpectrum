"""
Chat.py
-----------------
Answers users question in the chat
"""

import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.language_models import ChatModel, InputOutputTextPair


def Create_Model():
    parametersCHAT = {
        "temperature": 0.5,
        "max_output_tokens": 128,
        "top_p": 0.8,
        "top_k": 40}

    chat_model = ChatModel.from_pretrained("chat-bison@001")
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
    return chat, parametersCHAT


def Answer_Question(chat_model, parametersCHAT, prompt, user_question):
    """
    Answer to questions in the chatbox
    :param user_question: Question of user in the chat
    """
    responseCHAT = chat_model.send_message(user_question.strip(), **parametersCHAT)
    print(responseCHAT.text)
    return responseCHAT.text
