from faker import Faker
import json

from application.config.paths import FILES_OUTPUT_PATH

faker = Faker()

file_name: str = "users_with_emails.json"


def generic_users_to_json_file():
    file_to_path = FILES_OUTPUT_PATH.joinpath(file_name)
    data = []
    with open(file_to_path, mode="w") as file:
        for _ in range(10):
            dict_ = {"name": f"{faker.name()}", "email": f"{faker.email()}"}
            data.append(dict_)
        json.dump(data, file, indent=4)
        file.close()
        return file_to_path


def load_json_file_and_read(file_to_path=generic_users_to_json_file()):
    with open(file_to_path) as json_file:
        json_data = json.load(json_file)
        return json_data
