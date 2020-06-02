import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys

from models import setup_db, Question, Category, rollback, close_connection

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app, migrate=True)
  
  def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    return selection[start:end]

  def get_all_categories():
    categories = {}
    for category in Category.query.all():
      categories[str(category.id)] = category.type
    return categories
  
  '''
  @TODO==: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app, resources={r'/*': {'origins': '*'}})

  '''
  @TODO==: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authentication')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE, PATCH, OPTIONS')
    return response

  '''
  @TODO==: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories', methods=['GET'])
  def retrieve_all_categories():
    categories = get_all_categories()
    return jsonify({
      'success': True,
      'categories': categories,
      'total_categories': len(categories)
    })


  '''
  @TODO==: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions', methods=['GET'])
  def retrieve_all_questions():
    questions = Question.query.all()
    selection = [question.format() for question in questions]
    current_questions = paginate_questions(request, selection)
    
    if not current_questions:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(selection),
      'categories': get_all_categories(),
      'current_category': None
    })

  '''
  @TODO==: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.get(question_id)
    if question is None:
      abort(422)

    try:
      question.delete()
      selection = [question.format() for question in Question.query.all()]
      current_questions = paginate_questions(request, selection)
      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': current_questions,
        'total_questions': len(selection)
      })
    except:
      rollback()
      print(sys.exc_info())
      abort(422)
    finally:
      close_connection()


  '''
  @TODO==: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_or_search_question():
    body = request.get_json()

    if not body:
      abort(400)
    
    question = body.get('question', None)
    answer = body.get('answer', None)
    category = body.get('category', None)
    difficulty = body.get('difficulty', None)
    search_term = body.get('searchTerm', None)

    # if not questions search case, any missing args in the body will be considered bad request
    if search_term is None:
      for arg in ['question', 'answer', 'category', 'difficulty']:
        if arg not in body:
          abort(400)

    try:
      if search_term is not None:
        questions = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
        selection = [question.format() for question in questions]
        current_questions = paginate_questions(request, selection)
        return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(selection),
          'current_category': None
        })

      else: 
        for arg in [question, answer, category, difficulty]:
          if not arg:
            abort(422)
        if not Category.query.get(category):
          abort(422)
        question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
        question.insert()
        question_id = question.id
        selection = [question.format() for question in Question.query.all()]
        current_questions = paginate_questions(request, selection)
        return jsonify({
          'success': True,
          'created': question_id,
          'questions': current_questions,
          'total_questions': len(selection),
          'current_category': None
        })
    except:
      rollback()
      print(sys.exc_info())
      abort(422)
    finally:
      close_connection()



  '''
  @TODO==: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO==: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def retrieve_questions_for_sepcific_catgeory(category_id):
    questions = Question.query.filter(Question.category == category_id).all()
    if not questions:
      abort(422)
    selection = [question.format() for question in questions]
    current_questions = paginate_questions(request, selection)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(questions),
      'current_category': category_id
    })


  '''
  @TODO==: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def retrieve_questions_for_quiz():
    try:
      body = request.get_json()
      previous_questions = body.get('previous_questions', None)
      quiz_category = body.get('quiz_category', None)

      if previous_questions is None:
        abort(400)
      
      # check quiz_category if not listed in all_categories will be set to None
      all_categories = get_all_categories()
      if quiz_category and str(quiz_category['id']) not in all_categories:
        quiz_category = None

      # getting all questions based on quiz category
      questions = Question.query.filter(Question.category == quiz_category['id']).all() if quiz_category else Question.query.all()
      formatted_questions = [question.format() for question in questions]
      
      # get next question to be sent for the quiz
      if len(previous_questions) == len(formatted_questions):
        next_question = None
      else:
        random.shuffle(formatted_questions)
        for question in formatted_questions:
          if question['id'] not in previous_questions:
            next_question = question
            break
      
      return jsonify({
        'success': True,
        'question': next_question,
        'current_category': quiz_category,
        'total_questions': len(formatted_questions)
      })
    except:
      print(sys.exc_info())
      abort(400)

  '''
  @TODO==: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'Resource Not Found'
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'Not Processable'
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'Bad Request'
    }), 400

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': 'Method Not Allowed'
    }), 405
  
  return app

    