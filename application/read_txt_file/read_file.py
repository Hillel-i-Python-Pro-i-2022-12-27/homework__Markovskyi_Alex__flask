from application.config.paths import FILES_OUTPUT_PATH

content = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
    "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
    "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
    "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
    "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
)

file_name: str = "content_txt_file.txt"


def save_file_with_content():
    file_to_path = FILES_OUTPUT_PATH.joinpath(file_name)
    with open(file_to_path, mode="w") as txt_file:
        txt_file.write(content)
        txt_file.close()
        return file_to_path
