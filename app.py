from flask import Flask
from application.astrounats.reqst_and_save__astrounats import save_i_astronauts_to_file
from application.googledrive.reqst_and_calc__google_drive import calculate_data
from application.read_txt_file.read_file import save_file_with_content
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
    )


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


if __name__ == "__main__":
    app.run()
