import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'nim_reads'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
print(os.getenv('MONGO_URI'))

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())


@app.route('/add_review')
def add_review():
    return render_template('addreview.html')


@app.route('/insert_review', methods=['POST'])
def insert_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))


@app.route('/edit_review/<book_id>')
def edit_review(book_id):
    the_book = mongo.db.reviews.find_one({"_id": ObjectId(book_id)})
    return render_template('editreview.html', book=the_book)


@app.route('/update_review/<book_id>', methods=["POST"])
def update_review(book_id):
    reviews = mongo.db.reviews
    reviews.update({'_id': ObjectId(book_id)},
                   {
        'book_name': request.form.get('book_name'),
        'book_author': request.form.get('book_author'),
        'book_genre': request.form.get('book_genre'),
        'book_review': request.form.get('book_review'),
        'book_image': request.form.get('book_image'),
        'book_link': request.form.get('book_link')
    })
    return redirect(url_for('get_reviews'))


@app.route('/delete_review/<book_id>')
def delete_review(book_id):
    mongo.db.reviews.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('get_reviews'))
    

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=(os.environ.get('PORT', '5000')),
            debug=True)
