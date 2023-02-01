import requests
from application.config.paths import FILES_OUTPUT_PATH

url: str = "http://api.open-notify.org/astros.json"
file_name: str = "output_astronauts.txt"


def request_i_astronauts():
    with requests.Session() as session:
        response = session.get(url)
        response_json = response.json()

        return response_json


def save_i_astronauts_to_file(content=request_i_astronauts()):
    path_to_file = FILES_OUTPUT_PATH.joinpath(file_name)

    with open(path_to_file, mode="w") as file:
        file.write(f"<p>Total astronauts is: {content['number']}</p>")

        for full_name in content["people"]:
            file.write(f"<li>{full_name['name']}</li>\n")

        return path_to_file
