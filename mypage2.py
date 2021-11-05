from flask import Flask, render_template, jsonify, abort, request,\
    redirect, url_for
from model import db, save_data

app = Flask(__name__)

#httt://IP: PORT/

@app.route("/")
def welcome():
    product= db[1]
    return render_template("product.html",product=product)


@app.route("/api/products")
def product_api():
    return jsonify(db)

@app.route("/api/products/<int:index>")
def product_api_byIndex(index):
    try:
        product=db[index]
        return jsonify(product)
    except IndexError:
        abort(404)

#POST JSON DATA

@app.route("/api/products/form",methods=["GET","POST"])
def add_new_product():
    if request.method=='POST':
        try:
            product= {"productId": request.form['productId'],
                  "productName": request.form['productName'],
                  "price": request.form['price'],
                  "rating": request.form['rating']}

            db.append(product)
            save_data()

        except IndexError:
            abort(404)
        return redirect(url_for('product_api_byIndex', index=len(db) - 1))
    else:
        return render_template("add_product.html")

#launch development server
if __name__=='__main__':
    app.run(port=4002)