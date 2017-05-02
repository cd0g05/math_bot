
from __future__ import print_function
import random

# --------------- Helpers that build all of the responses ----------------------

def get_question_and_answer(level=1):    #This function generates the random math questions
    #finds level
    #depending on level, asks a question
    #if correct, repeats
    if level == 1:
        #reandom number from 1 - 20 + rn from 1-20
        n1 = random.randint(1,20)
        n2 = random.randint(1,20)
        answer = n1 + n2
        return "{0} plus {1}".format(n1,n2), answer
    elif level == 2:
        n1 = random.randint(1,20)
        n2 = random.randint(1,20)
        if n1 > n2:
            answer = n1 - n2
            return "{0} minus {1}".format(n1,n2), answer
        else:
            answer = n2 - n1
            return "{0} minus {1}".format(n2,n1), answer
    elif level == 3:
        n1 = random.randint(1,10)                                                       
        n2 = random.randint(1,10)
        if n1 > n2:
            answer = n1 * n2
            return "{0} times {1}".format(n1,n2), answer
        else:
            answer = n2 * n1
            return "{0} times {1}".format(n2,n1), answer
    elif level == 4:
        n1 = random.randint(1,10)
        answer = random.randint(1,10)
        return "{0} divided by {1}".format(n1*answer,n1), answer
    elif level == 5:
        #reandom number from 1 - 20 + rn from 1-20
        n1 = random.randint(1,40)
        n2 = random.randint(1,100)
        answer = n1 + n2
        return "{0} plus {1}".format(n1,n2), answer
    elif level == 6:
        n1 = random.randint(1,40)
        n2 = random.randint(1,40)
        if n1 > n2:
            answer = n1 - n2
            return "{0} minus {1}".format(n1,n2), answer
        else:
            answer = n2 - n1
            return "{0} minus {1}".format(n2,n1), answer
    elif level == 7:
        n1 = random.randint(1,20)
        n2 = random.randint(1,20)
        answer = n1 * n2
        return "{0} times {1}".format(n1,n2), answer
    elif level == 8:
        n1 = random.randint(1,20)
        answer = random.randint(1,6)
        return "{0} divided by {1}".format(n1*answer,n1), answer
    elif level == 9:
        #reandom number from 1 - 20 + rn from 1-20
        n1 = random.randint(1,40)
        n2 = random.randint(1,100)
        n3 = random.randint(1,40)
        answer = n1 + n2 + n3
        return "{0} plus {1} plus {2}".format(n1,n2,n3), answer
    elif level == 10:
        n1 = random.randint(1,40)
        n2 = random.randint(1,40)
        n3 = random.randint(1,40)
        if n1 > n2:
            answer = n1 - n2 - n3
            return "{0} minus {1} minus {2}".format(n1,n2,n3), answer
        else:
            answer = n2 - n1
            return "{0} minus {1} minus {2}".format(n2,n1,n3), answer
    elif level == 11:
        n1 = random.randint(1,20)
        n2 = random.randint(1,20)
        n3 = random.randint(1,20)
        answer = n1 * n2 * n3
        return "{0} times {1} times {2}".format(n1,n2,n3), answer
    elif level == 12:
        n1 = random.randint(1,10)
        n2 = random.randint(1,30)
        na = random.randint(1,6)
        answer = (n1*na) / n1 + n2
        return "{0} divided by {1} plus {2}".format(n1*na,n1,n2), answer
    elif level == 13:
        #reandom number from 1 - 20 + rn from 1-20
        n1 = random.randint(1,70)
        n2 = random.randint(1,100)
        n3 = random.randint(1,70)
        answer = n1 + n2 + n3
        return "{0} plus {1} plus {2}".format(n1,n2,n3), answer
    elif level == 14:
        n1 = random.randint(1,60)
        n2 = random.randint(1,60)
        n3 = random.randint(1,60)
        if n1 > n2:
            answer = n1 - n2 - n3
            return "{0} minus {1} minus {2}".format(n1,n2,n3), answer
        else:
            answer = n2 - n1
            return "{0} minus {1} minus {2}".format(n2,n1,n3), answer
    elif level == 15:
        n1 = random.randint(1,40)
        n2 = random.randint(1,40)
        n3 = random.randint(1,40)
        answer = n1 * n2 * n3
        return "{0} times {1} times {2}".format(n1,n2,n3), answer
    elif level == 16:
        n1 = random.randint(1,20)
        n2 = random.randint(1,50)
        na = random.randint(1,10)
        answer = (n1*na) / n1 + n2
        return "{0} divided by {1} plus {2}".format(n1*na,n1,n2), answer
    elif level == 17:
        n1 = random.randint(1,20)
        n2 = random.randint(19,99999999)
        na = random.randint(70,99999999)
        nt = random.randint(12475,99999999999)
        answer = (n1*na) / n1 + n2 * nt
        return "{0} divided by {1} plus {2} times {3}".format(n1*na,n1,n2,nt), answer
    else:

        return None,None





def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to MathBot. " \
                    "I will ask you a question and you will answer it. You will have 30 seconds to answer. If you get it right, then you will move on to the next question. " \
                    "When you are ready say start. "
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "When you are ready say start "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_question(intent, session):            #This fetches the question from the get_question_and_answer()
    question,answer = get_question_and_answer(1)

    session_attributes = {"answer": answer, "level": 1, "score": 0}
    reprompt_text = None
    speech_output = "Here is your math question: What is {0}".format(question)
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


def verify_answer(intent, session):     #this tells the alexa to ask the question, checks if the answer is correct, tracks points and levels, and ends the game when it is over.
    print(session)
    actual = session["attributes"]["answer"]
    guess = intent["slots"]["answer"]['value']
    print ("actual = {0}, guess = {1}".format(actual,guess))
    if int(guess) == int(actual):
        level = session["attributes"]["level"]
        question,answer = get_question_and_answer(level + 1)
        if question is None: # game is over
            score = session["attributes"]["score"] + level
            speech_output = "Congratulations, you win! Your score was {1}".format(actual, score)
            session_attributes = {}
            should_end_session = True
            reprompt_text = None
            return build_response(session_attributes, build_speechlet_response(
                intent['name'], speech_output, reprompt_text, should_end_session))
        else: # next question
            score = session["attributes"]["score"] + level
            speech_output = "Good! Next question: What is {0}".format(question)
            session_attributes = {"answer": answer, "level": level + 1, "score": score}
            reprompt_text = None
            should_end_session = False
            return build_response(session_attributes, build_speechlet_response(
                intent['name'], speech_output, reprompt_text, should_end_session))
    else:
        score = session["attributes"]["score"]
        speech_output = "Your answer is wrong. The correct answer was: {0}. The game is over, and your score was {1}".format(actual, score)
        session_attributes = {}
        should_end_session = True
        reprompt_text = None
        return build_response(session_attributes, build_speechlet_response(
            intent['name'], speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "NewQuestion":
        return get_question(intent, session)
    elif intent_name == "AnswerQuestion":
        return verify_answer(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
