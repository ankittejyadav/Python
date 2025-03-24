import os


def remove_spacedhyphen_in_filename(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if " - " in filename:
                newfilename = filename.replace(" - ", "-")
                os.rename(
                    os.path.join(folder_path, filename),
                    os.path.join(folder_path, newfilename),
                )
                print(f"{newfilename}")
    except Exception as e:
        print(f"An error occured: {e}")


def replace_hyphen_with_underscore_in_filename(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if "-" in filename:
                newfilename = filename.replace("-", "_")
                os.rename(
                    os.path.join(folder_path, filename),
                    os.path.join(folder_path, newfilename),
                )
                print(f"{newfilename}")
    except Exception as e:
        print(f"An Error occured: {e}")


def replace_space_with_underscore_in_filename(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if " " in filename:
                newfilename = filename.replace(" ", "_")
                os.rename(
                    os.path.join(folder_path, filename),
                    os.path.join(folder_path, newfilename),
                )
                print(f"{newfilename}")
    except Exception as e:
        print(f"An exception occurred {e}")


folder_path = "C:\\Users\\ankit.yadav2\\OneDrive - S&P Global\\Documents\\sql_spgi"
# remove_spacedhyphen_in_filename(folder_path)
# replace_hyphen_with_underscore_in_filename(folder_path)
# replace_space_with_underscore_in_filename(folder_path)
