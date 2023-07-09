from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
import json
import string

from .Creator import Create_Course_Social, Create_Course_Emotion, Create_Course_Communication, Create_Images
from .Get_Question import Get_Question
from .Chat import Create_Model, Answer_Question
from .Summarize import Create_Summary
import random


prompt = "default"
courseParagraphs = []
courseImages = []
courseHeaders = []

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        global lesson_query
        query = request.form.get('query')
        print(query)
        lesson_query = query

        if len(query) < 1:
            flash('Query is too short!', category="error")
        else:
            global prompt, courseParagraphs, courseImages, courseHeaders, chat, parametersCHAT
            prompt = string.capwords(query, sep=None)

            if query == 'social':
                temp, courseImages = Create_Course_Social(query)

            elif query == 'emotions':
                temp, courseImages = Create_Course_Emotion(query)

            elif query == 'communication':
                temp, courseImages = Create_Course_Communication(query)

            else:
                print("ERROR!")

            chat, parametersCHAT = Create_Model()

            for i in range(len(temp)):
                courseHeaders.append(temp[i][:temp[i].find(':') + 1])
                courseParagraphs.append(temp[i][temp[i].find(':') + 1:])

            return redirect(url_for('views.query'))

    return render_template("home.html")


@views.route('/query', methods=['GET', 'POST'])
def query():
    return render_template('query.html', prompt=prompt, courseParagraphs=courseParagraphs, courseImages=courseImages, courseHeaders=courseHeaders)


@views.route('/generate-response', methods=['POST'])
def generate_response():
    prompt = json.loads(request.data)
    promptText = prompt['text']
    print(promptText)
    return jsonify({"resp": Answer_Question(chat, parametersCHAT, lesson_query, promptText)})


@views.route('/generate-summary', methods=['POST'])
def generate_summary():
    # prompt = json.loads(request.data)
    # promptText = prompt['text']
    # print(promptText)
    return jsonify({"resp": Create_Summary(courseParagraphs)})


@views.route('/generate-quiz', methods=['POST'])
def generate_quiz():
    # prompt = json.loads(request.data)
    # promptText = prompt['text']
    # print(promptText)

    # return jsonify({"question": "What are the first 10 digits of pi?", "answer": "3.141592653", "reference": 3})
    question = Get_Question(lesson_query, courseParagraphs)
    print(question)
    return jsonify({"question": question["question"], "reference": question["reference"], "answer": question["answer"]})