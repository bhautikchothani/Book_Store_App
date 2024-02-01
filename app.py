from flask import Flask,request,jsonify,render_template
from flask import *

app = Flask(__name__)

books= [
       {        
            "id": 1,
            "title": "The Silent Symphony",
            "author": "Emily Harper",
            "price": 20,
            "year_published": 2018
         },
         {
            "id": 2,
            "title": "Echoes of Eternity",
            "author": "Daniel Mitchell",
            "price": 19.95,
            "year_published": 2020
         },
         {
            "id": 3,
            "title": "Whispers in the Wind",
            "author": "Sarah Anderson",
            "price": 30.50,
            "year_published": 2017
         },
         {
            "id": 4,
            "title": "The Enigma Code",
            "author": "James Johnson",
            "price": 22.99,
            "year_published": 2019
         },
         {
            "id": 5,
            "title": "Mystic Moonlight",
            "author": "Jennifer Davis",
            "price": 18.75,
            "year_published": 2021
         },
         {
            "id": 6,
            "title": "Beyond the Horizon",
            "author": "Michael Roberts",
            "price": 27.50,
            "year_published": 2016
         },
         {
            "id": 7,
            "title": "Infinite Imagination",
            "author": "Emma Turner",
            "price": 23.45,
            "year_published": 2022
         },
         {
            "id": 8,
            "title": "Eternal Embrace",
            "author": "Christopher Walker",
            "price": 21.99,
            "year_published": 2015
         },
         {
            "id": 9,
            "title": "Serenade of Shadows",
            "author": "Melissa White",
            "price": 28.75,
            "year_published": 2023
         },
         {
            "id": 10,
            "title": "Whirlwind of Wonders",
            "author": "Robert Green",
            "price": 24.50,
            "year_published": 2014
         },
         {
            "id": 11,
            "title": "You Can",
            "author": "pritish",
            "price": 50,
            "year_published": 2026
         },
         ]
#html form link #
# fornt page #
@app.route('/',methods=['GET'])
def index():
   return render_template("index.html",books=books)

#newform data#  
@app.route('/addnewform',methods=['GET'])
def addnewform():
   return render_template("form.html")



@app.route('/addbook',methods=["POST","GET"])
def add_books(): 
   global books
   
   
   try:
      id = int(request.form["id"])
      title = str(request.form["title"])
      author = str(request.form["author"])
      price = float(request.form["price"])
      year_published = int(request.form["year"])

      new_book = {
            "id":id,
            "title": title,
            "author":author,
            "price": price,
            "year_published": year_published,
         }
      books.append(new_book)
      return redirect("/")
      
   except  Exception as e :
      return jsonify({"error":str(e)})

  
       
# GET method Uses#

@app.route('/books', methods=["GET"])  #http://127.0.0.1:5000/get-book
def get_all_book():
    return jsonify(list(books))

# Post method uses

@app.route("/books", methods=["POST"])
def add_book():
    new_title = request.form["title"]
    new_author = request.form["author"]
    new_price = request.form["price"]
    new_year_published = request.form["year_published"]
    iD = books[-1]["id"] + 1

    new_obj = {
        "id": iD,
        "title": new_title,
        "author": new_author,
        "price": new_price,
        "year_published": new_year_published,
    }
    books.append(new_obj)
    return jsonify(books)

# Put methods uses

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    if request.method == "PUT":
        for book in books:
            if book["id"] == book_id:
                book["author"] = request.form["author"]
                book["price"] = request.form["price"]
                book["title"] = request.form["title"]
                book["year_published"] = request.form["year_published"]
                updated_book = {
                    "author": book["author"],
                    "price": book["price"],
                    "title": book["title"],
                    "year_published": book["year_published"],
                }
                return jsonify(updated_book)
        return {"message": "Books Not Found.. In List"}

# Delete (DELETE): Remove a book by id

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book["id"] == book_id:
           books.pop(index)
           return jsonify(books)

if __name__=='__main__':
    app.run(debug=True)