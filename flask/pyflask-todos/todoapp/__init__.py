from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import bson

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
    
    # Example route: /user/num_posts?id=6516a8f31ed01206dde6382c
    @app.route("/user/num_posts", methods=["GET"])
    def get_user_postcount():
        user_id = request.args.get('id')
        username = userdetails.find_one({"_id": bson.objectid.ObjectId(user_id)})["username"] 
        count = posts.count_documents({"user": bson.objectid.ObjectId(user_id)})

        return jsonify({"username": username, "Number of post": count}), 200
    
    @app.route("/avg_post_per_user", methods=["GET"])
    def get_avg_post_per_user():
        user_count = userdetails.count_documents({})
        post_count = posts.count_documents({})

        return jsonify({"Posts per user": post_count/user_count}), 200


    return app