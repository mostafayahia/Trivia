# Trivia App
It's is [Udacity full stack api final project](https://github.com/udacity/FSND/tree/master/projects/02_trivia_api/starter). 
The app enables you to play a fun game in many categories (Art, Science, Sports,...) and you can also add question & answer in any category. The task is to implement api endpoints and unit tests.

### Getting Started
#### Backend
You can first install all packages needed to run the app `pip3 install -r requirements.txt`
<br />
To run the application, you can run the following commands:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
The default url is `http://localhost:5000/`
#### Frontend
After running the backend part, you can run the frontend part using the following commands:
```
npm install // run only once for loading the packages needed in node_modules
npm start
```
Note: In `package.json` the `proxy` property is set to `http://localhost:5000/` so it should be connected well with the backend.

#### Tests
To run the unit tests, you can run the following commands:
```
dropdb trivia_test // only if trivia_test already exist
createdb trivia_test
psql trivia_test < trivia.psql // you should be in backend directory
python3 test_flaskr.py
```

### API Reference
#### Getting Started
- Base URL: At this point the app can only be run locally. The default url `http://localhost:5000/`
- Authentication: At this point, the app doesn't require any authentication or API keys.

#### Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "success": false,
  "error": 404,
  "message": "Resource Not Found"
}
```
types of errors:
- 404: Resource Not Found
- 400: Bad Request
- 405: Method Not Allowed
- 422: Not Processable

### Endpoints
#### GET /categories
- ##### General:
  - Retrun a list of category objects, success value, and total number of categories
- `curl 'http://localhost:5000/categories'`
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true, 
  "total_categories": 6
}
```
#### GET /questions
- ##### General:
  - Return a list of questions, categories, success value, and total number of questions.
  - Result are paginated in groups of 10. Include a request argument to set the page number, starting from 1.
- `curl 'http://localhost:5000/questions?page=1'`
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 22
}
```
#### DELETE /questions/{id}
- ##### General:
  - Return a list of question objects, success value, total number of questions, and deleted id
- `curl -X DELETE 'http://localhost:5000/questions/23?page=2'`
```
{
  "deleted": 23, 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "success": true, 
  "total_questions": 18
}
```
#### POST /questions
- ##### General:
  - if `searchTerm` provided it will return a search result, otherwise will create a question in a certain category
  - request body should include `searchTerm` or `question, answer, category & difficulty`
  - Return success value, total number of questions, questions, current category and created id (incase of creation only)
- `curl -X POST -H 'content-type: application/json' -d '{"searchTerm": "title"}' 'http://localhost:5000/questions'`
```
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}
```
- `curl -X POST -H 'content-type: application/json' -d '{"question": "tq?", "answer": "ta", "difficulty": 3, "category": 6}' 'http://localhost:5000/questions?page=2'`
```
{
  "created": 24, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "ta", 
      "category": 6, 
      "difficulty": 3, 
      "id": 24, 
      "question": "tq?"
    }
  ], 
  "success": true, 
  "total_questions": 19
}
```

#### GET /categories/{category_id}/questions
- ##### General:
  - Return a list of questions objects for a certain category, success value, total number of questions, and current category
- `curl 'http://localhost:5000/categories/6/questions'`
```
{
  "current_category": 6, 
  "questions": [
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "ta", 
      "category": 6, 
      "difficulty": 3, 
      "id": 24, 
      "question": "tq?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

#### POST /quizzes
- ##### General:
  - request body should contain `previous_questions` represents array of questions' ids & `quiz_category`
  - Return a random question for the quiz not in the previous questions given in the request body, total number of questions, success value, and the current category
- `curl -X POST -H 'content-type: application/json' -d '{"previous_questions": [24, 10], "quiz_category": {"id": 6, "type": "Sports"}}' 'http://localhost:5000/quizzes'`
```
{
  "current_category": {
    "id": 6, 
    "type": "Sports"
  }, 
  "question": {
    "answer": "Uruguay", 
    "category": 6, 
    "difficulty": 4, 
    "id": 11, 
    "question": "Which country won the first ever soccer World Cup in 1930?"
  }, 
  "success": true, 
  "total_questions": 3
}
```

