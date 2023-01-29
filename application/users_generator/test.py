from faker import Faker
import json

from application.config.paths import FILES_OUTPUT_PATH

faker = Faker()

file_name: str = "users_with_emails.json"


def generic_users_to_json():
    file_to_path = FILES_OUTPUT_PATH.joinpath(file_name)
    data = []
    with open(file_to_path, mode="w") as file:
        for _ in range(10):
            dict_ = {"name": faker.name(), "email": faker.email()}
            data.append(dict_)
        json_object = json.dumps(data, indent=4)
        file.writelines(json_object)
        return file_to_path


# def open_json_file(file: str = generic_users_to_json()):
#     list_ = []
#     with open(file, "r") as file:
#         data = json.load(file)
#         for idx, odj in enumerate(data):
#             list_.append("".join(odj["name"] + " | " + odj["email"]))
#         return "\n".join(list_)
