import tkinter as tk
from tkinter import messagebox

questions = [
    "What is Autism Spectrum Disorder (ASD)?",
    "Why is understanding and recognizing emotions important for individuals with ASD?",
    "How do individuals with ASD struggle with perceiving and interpreting emotions?",
    "What are some ways to help ASD individuals learn about their emotions?",
    "Can you provide examples of relaxation exercises for managing emotions?",
    "How can visual tools like ladder pictures or thermometers help individuals with ASD?",
    "What are the calming down steps to help autistic individuals?",
    "How can sensory stimulation assist in managing emotions?",
    "What are some suggested break time activities for ASD individuals?",
    "What is the significance of recognizing emotions in media for individuals with ASD?",
    "What are some strategies for supporting emotional understanding in ASD individuals?",
    "How does promoting emotional understanding contribute to a more inclusive society?",
    "Can you explain the benefits of recognizing emotional needs in caregivers, educators, and professionals?",
    "Why is it important to value diverse emotions and support every individual regardless of neurodiversity?",
    "How can encouraging physical activity be helpful for ASD individuals?",
    "What are some examples of change of activity to take a brain break?",
    "How can sensation description be used to help ASD individuals recognize their emotions?",
    "Can you elaborate on the significance of recognizing emotions in oneself and others for individuals with ASD?",
    "What are some visual tools besides ladder pictures that can be used to gauge emotional intensity?",
    "What are the potential effects of improved emotional recognition in individuals with ASD?"
]

answers = [
    "Autism Spectrum Disorder (ASD) is a condition that affects a significant portion of the population. It is crucial to understand and recognize emotions in individuals with ASD for their well-being and the creation of inclusive communities.",
    "Individuals with ASD struggle with perceiving and interpreting emotions, which can lead to social isolation. Improved emotional recognition enhances their social skills and connections.",
    "Autistic individuals often have difficulty recognizing and understanding emotions in themselves and others, particularly when upset.",
    "Some ways to help ASD individuals learn about their emotions include emotion pointing, sensation description, emotional recognition in media, and visual tools like ladder pictures or thermometers.",
    "Relaxation exercises can be helpful, such as counting, deep breathing, or focusing on something that brings happiness and calmness. Tracing around the hand with fingers while focusing on breathing can also be effective.",
    "Visual tools like ladder pictures or thermometers provide a visual representation of emotional intensity, helping individuals with ASD gauge and communicate their emotions.",
    "The calming down steps for autistic individuals include noticing the emotion, naming it, pausing, providing support, and addressing the underlying issue.",
    "Sensory stimulation, such as clapping hands, using sensory toys, or engaging in stimming behaviors, can help manage emotions. If sensory-seeking behavior is inappropriate, alternative behaviors that meet the sensory needs can be explored.",
    "Taking breaks by going for a walk, getting a drink of water, or finding a quiet place to sit can be helpful for ASD individuals.",
    "Recognizing emotions in media, like movies or shows, helps individuals with ASD learn to recognize emotions in others by connecting them to specific expressions or actions.",
    "Strategies for supporting emotional understanding in ASD individuals include emotion pointing, sensation description, emotional recognition in media, and using visual tools like ladder pictures or thermometers.",
    "Promoting emotional understanding creates a society that values neurodiversity, embraces differences, and celebrates the unique emotional experiences of individuals with ASD.",
    "Recognizing emotional needs benefits caregivers, educators, and professionals by improving their understanding of individuals with ASD and enabling tailored support and interventions.",
    "Valuing diverse emotions and supporting every individual, regardless of neurodiversity, promotes inclusivity and ensures that everyone's emotional experiences are respected and acknowledged.",
    "Encouraging physical activity can be helpful for ASD individuals as it provides an outlet for energy, promotes well-being, and can serve as a coping mechanism for managing emotions.",
    "Taking a brain break can involve activities like listening to favorite music, reading a book, or listening to a podcast about special interests.",
    "Sensation description involves encouraging ASD individuals to describe the physical sensations that accompany their emotions, aiding in the recognition and understanding of emotions.",
    "Recognizing emotions in oneself and others is crucial for individuals with ASD to improve their social interactions, communication skills, and overall well-being.",
    "Besides ladder pictures, other visual tools like thermometers, emojis, or facial expression charts can be used to gauge and communicate emotional intensity.",
    "Improved emotional recognition in individuals with ASD can lead to enhanced social interactions, improved communication, and better overall well-being."
]

def show_answer(question_index):
    messagebox.showinfo("Answer", answers[question_index])

def ask_question(question_index):
    response = messagebox.askyesno("Question", questions[question_index])
    if response:
        show_answer(question_index)
        ask_another_question()
    else:
        ask_another_question()

def ask_another_question():
    response = messagebox.askyesno("Another Question", "Do you have another question?")
    if response:
        ask_question(select_question())
    else:
        messagebox.showinfo("Goodbye", "Thank you for your participation!")

def select_question():
    question_index = messagebox.askquestion("Select Question", "Please select a question:")
    return questions.index(question_index)

def start_conversation():
    messagebox.showinfo("Conversation Start", "Let's have a conversation about Autism Spectrum Disorder (ASD) and emotions!")
    ask_question(select_question())

start_conversation()
