from flask import Flask, Response
from webargs import fields
from webargs.flaskparser import use_args

from application.astrounats.reqst_and_save__astrounats import save_i_astronauts_to_file
from application.googledrive.reqst_and_calc__google_drive import calculate_data
from application.read_txt_file.read_file import save_file_with_content
from application.services.create_table import create_table
from application.services.db_connection import DBConnection
from application.users_generator.generate_users import load_json_file_and_read

app = Flask(__name__)


@app.route("/")
def page__index():  # put application's code here
    return (
        "<h1>INDEX PAGE</h1>"
        "<p><a href='./get_content'>GET CONTENT</p>"
        "<p><a href='./generate-users'>GENERATE USERS</p>"
        "<p><a href='./space'>SPACE</p>"
        "<p><a href='./mean'>MEAN</p>"
        "<br><h1>URL REQUESTS:</h1>"
        "<li>/phone-book/read-all - show all phone book data</li>"
        "<li>/phone-book/read/<int> - show phone book by Primary Key</li>"
        "<li>/phone-book/update/<int>?contact_name=*****&phone=***** - update phone book row by Primary Key</li>"
        "<li>/phone-book/delete/<int> - delete phone book row by Primary Key</li>"
    )


@app.route("/phone-book/create")
@use_args({"contact_name": fields.Str(required=True), "phone": fields.Str(required=True)}, location="query")
def users__create(args):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO phones (contact_name, phone) VALUES (:contact_name, :phone);",
                {"contact_name": args["contact_name"], "phone": args["phone"]},
            )
    return "Ok"


@app.route("/phone-book/read-all")
def users__read_all():
    with DBConnection() as connection:
        table_ = connection.execute("SELECT * FROM phones;").fetchall()
    return "<br>".join([f'{row_["pk"]}. {row_["contact_name"]} - {row_["phone"]}' for row_ in table_])


@app.route("/phone-book/read/<int:pk>")
def users__read(pk: int):
    with DBConnection() as connection:
        table_ = connection.execute(
            "SELECT * " "FROM phones " "WHERE (pk=:pk);",
            {
                "pk": pk,
            },
        ).fetchone()

    return f'{table_["pk"]}. {table_["contact_name"]} - {table_["phone"]}'


@app.route("/phone-book/update/<int:pk>")
@use_args({"contact_name": fields.Str(), "phone": fields.Str()}, location="query")
def users__update(args, pk: int):
    with DBConnection() as connection:
        with connection:
            contact_name = args.get("contact_name")
            phone = args.get("phone")

            if contact_name is None and phone is None:
                return Response("Need to provide at least one argument", status=400)

            args_for_request = []
            if contact_name is not None:
                args_for_request.append("contact_name=:contact_name")

            if phone is not None:
                args_for_request.append("phone:=phone")

            answer = ", ".join(args_for_request)

            connection.execute(
                "UPDATE phones " f"SET {answer} " "WHERE pk=:pk;",
                {
                    "pk": pk,
                    "contact_name": contact_name,
                    "phone": phone,
                },
            )
    return "Ok"


@app.route("/phone-book/delete/<int:pk>")
def users__delete(pk: int):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE " "FROM phones " "WHERE (pk=:pk);",
                {
                    "pk": pk,
                },
            )

    return "Ok"


@app.route("/get_content")
def page__gen_content(file=save_file_with_content()):
    with open(file) as data:
        content = data.read()
    return f"<h1>GET CONTENT</h1>" f"{content}" f"<br><a href='/'>←BACK</a>"


@app.route("/generate-users")
def page__gen_users(data=load_json_file_and_read()):
    content: str = ""
    for users in data:
        content += f"<p>{users['name']}  :  {users['email']}</p>"
    return f"<h1>GENERATE USERS</h1>" f"{content}" f"<a href='/'>←BACK</a>"


@app.route("/space")
def page__space(path_to_file=save_i_astronauts_to_file()):
    file = path_to_file
    text_file = open(file)
    content = text_file.read()
    return f"<h1>SPACE</h1>" f"{content}" f"<br><a href='/'>←BACK</a>"


@app.route("/mean")
def page__mean():
    height, weight = calculate_data()
    return (
        f"<h1>MEAN</h1>"
        f"<p>Average HEIGHT is: {height} cm.</p><p>Average WEIGHT is: {weight} kg.</p>"
        f"<a href='/'>←BACK</a>"
    )


create_table()
if __name__ == "__main__":
    app.run()
