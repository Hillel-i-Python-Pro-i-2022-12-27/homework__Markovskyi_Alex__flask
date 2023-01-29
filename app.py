from flask import Flask
from application.astrounats.reqst_and_save__astrounats import save_i_astronauts_to_file
from application.googledrive.reqst_and_calc__google_drive import calculate_data
from application.users_generator.generate_users import open_json_file

app = Flask(__name__)


@app.route("/")
def page__index():  # put application's code here
    return "<h1>INDEX PAGE</h1>"


@app.route("/generate-users")
def page__gen_usrs(data=open_json_file):
    decode_to_lst = []
    for idx, odj in enumerate(data):
        decode_to_lst.append("".join(odj["name"] + " | " + odj["email"]))
    return print(f"{decode_to_lst}")


@app.route("/space")
def page__space(path_to_file=save_i_astronauts_to_file()):
    file = path_to_file
    text_file = open(file)
    content = text_file.read()
    return f"{content}"


@app.route("/mean")
def page__mean():
    height, weight = calculate_data()
    return f"<p>Average HEIGHT is: {height} cm.</p><p>Average WEIGHT is: {weight} kg.</p>"


if __name__ == "__main__":
    app.run()
