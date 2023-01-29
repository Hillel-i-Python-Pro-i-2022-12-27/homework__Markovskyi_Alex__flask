import math
import pandas as pd
import requests
from application.config.paths import FILES_OUTPUT_PATH

url: str = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
file_name: str = "download_file.csv"


def requests__file_from_google_drive():
    path_to_file = FILES_OUTPUT_PATH.joinpath(file_name)
    with requests.Session() as session:
        response = session.get(url)

        csv_file = open(path_to_file, "wb")
        csv_file.write(response.content)
        csv_file.close()
        return path_to_file


def calculate_data(path_to_file=requests__file_from_google_drive()):
    df = pd.read_csv(path_to_file)

    inches_to_cm: float = 2.54
    pounds_to_kg: float = 0.45359237

    height_count: int = df["Height(Inches)"].count()
    height_sum: int = df["Height(Inches)"].sum()
    average_height = (height_sum * inches_to_cm) / height_count
    average_height = math.ceil(average_height)

    weight_count: int = df["Weight(Pounds)"].count()
    weight_sum: int = df["Weight(Pounds)"].sum()
    average_weight = (weight_sum * pounds_to_kg) / weight_count
    average_weight = math.ceil(average_weight)

    return average_height, average_weight
