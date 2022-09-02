from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.order import Order
from flask_app.models.cookie import Cookie

@app.route('/orders')
def orders():
    # call the get all classmethod to get all
    orders = Order.get_all_orders()
    return render_template("orders.html", orders=orders)

@app.route('/')
def index():
    return redirect('/orders')

@app.route('/orders/add')
def order_add():
    cookies = Cookie.get_types()
    return render_template("add_order.html", cookies = cookies)


@app.route('/order/create', methods=["POST"])
def order_create():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    if not Order.validate_order(request.form):
        return redirect('/orders/add')

    data = {
        "name": request.form["name"],
        "cookie_id": request.form["cookie_id"],
        "box_count": request.form["box_count"]
    }
    # We pass the data dictionary into the save method from the user class.
    Order.create_order(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/order/edit/<int:id>')
def order_show_one(id):
    data = {
        "id": id
    }
    cookies = Cookie.get_types()
    order = Order.get_one_order(data)
    return render_template("edit_order.html", order = order, cookies = cookies)


@app.route('/order/update', methods=['POST'])
def order_update():
    print("A")
    print(request.form)
    order_id = request.form["id"]
    if not Order.validate_order(request.form):
        return redirect(f"/order/edit/{order_id}")
    Order.update(request.form)
    return redirect('/')

