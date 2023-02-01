from pathlib import Path
from typing import Final

ROOT_PATH: Final[Path] = Path(__file__).parents[2]
FILES_INPUT_PATH: Final[Path] = ROOT_PATH.joinpath("files_input")
FILES_OUTPUT_PATH: Final[Path] = ROOT_PATH.joinpath("files_output")
FILES_SPECIAL_FOLDER: Final[Path] = ROOT_PATH.joinpath("special_folder")
