import random
import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.language_models import ChatModel, InputOutputTextPair


def Get_Question(lesson_query, courseParagraphs):
    reference = random.randint(0, len(courseParagraphs) - 1)
    package = {"reference": reference+1, "question": ''}
    paragraph = courseParagraphs[reference]

    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parametersMCQ = {
        "temperature": 1,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 23
    }

    chatMCQ = chat_model.start_chat(
        context="""A child just finished reading a lesson and now must answer a few situational multiple choice 
        questions. Questions must be tailored towards children ages 5-12. Based on this lesson generate a single 
        situational multiple choice question for kids with a clear correct answer: """ + paragraph,
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

    responseMCQ = chatMCQ.send_message("""question""", **parametersMCQ).text
    q = responseMCQ[max(responseMCQ.find(':'), 0) + 1:]

    package["question"] = q[0:q.find('[')].strip()
    package["answer"] = chatMCQ.send_message("""What is the correct answer?""", **parametersMCQ).text.strip()

    return package