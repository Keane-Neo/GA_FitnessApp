from flask import Flask, jsonify
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://bkrfitapp:wfKgeS0Vav8oaTFG@fit-app.hkvtlye.mongodb.net/fitness-app'
    mongo = PyMongo(app)
    posts = mongo.db.posts
    userdetails = mongo.db.userdetails

    @app.route('/')
    # def index():
    #     saved_todos = []
    #     cursor = todos.find()
    #     for i in cursor:
    #         saved_todos.append({
    #             'id': str(i['_id']),
    #             'todo': i['todo']
    #         })
    #     print("testing",saved_todos)
    #     return jsonify({'todos': saved_todos})
    def greeting():
        return jsonify({'message':"this is fitness app data API"})
    
    @app.route('/posts_count', methods=['GET'])
    def get_posts_count():
        count = posts.count_documents({})
        return jsonify({'posts_count': count}), 200
        
    @app.route('/accounts_count', methods=['GET'])
    def get_accounts_count():
        count = userdetails.count_documents({})
        return jsonify({'accounts_count': count}), 200

    @app.route('/trainers_count', methods=['GET'])
    def get_trainers_count():
        count = userdetails.count_documents({"userType":"trainer"})
        return jsonify({'trainers_count': count}), 200

    @app.route('/avg_age', methods=['GET'])
    def get_avg_age():
        pipeline = [
            {"$group":{
                '_id':None, 
                'avg_age': {
                    "$avg":"$age"
                    }
                }
            }
        ]
        result=list(userdetails.aggregate(pipeline))
        return jsonify({'avg_age': result[0]['avg_age']}), 200

    return app