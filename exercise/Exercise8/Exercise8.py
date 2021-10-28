import os


def soldier(folder_path, blacklist_file, file_ext):
    """
        soldier() -> prettifies your folder by capitalizing every file
        folder_path : path of the folder you want to prettify
        blacklist_file : a file that contains a newline seperated list of file names to ignore
        file_ext : if this parameter is specified then it will systematically rename every file of that extension to 0...N .{file_extension} where N is the number of files
    """

    folder_path = os.path.abspath(folder_path)

    # This will contain the filenames of the extension found
    ext_files = []

    # Check if the folder path is valid
    if not os.path.exists(folder_path):
        print("that path doesn't exist")
        exit(1)

    # validate file extension
    if not file_ext.startswith('.'):
        print("Incorrect file extension")
        exit(1)

    # File error checking
    try:
        with open(blacklist_file) as blacklist:
            ignore = blacklist.read().split('\n')
    except Exception as e:
        print("No blacklist file found, continuing to rename whole directory")
        ignore = []

    os.chdir(folder_path)

    for file in os.listdir('.'):
        # append to list of file extension
        if file.endswith(file_ext):
            ext_files.append(file)
            continue
        # capitalize the file
        if file[0].islower() and file not in ignore and os.path.isfile(file):
            os.rename(file, file.capitalize())


    ext_files_len = len(ext_files)
    if ext_files_len != 0:
        for i in range(ext_files_len):
            os.rename(ext_files[i], f"{i}{file_ext}")
    else:
        print(f"could not find the files with extension {file_ext}")


if __name__ == "__main__":
    folder_path = input("Enter folderPath: ")
    blacklist_file = input("Enter the filename of the blacklist file : ")
    file_ext = input(
        "Enter the file extension (starting with a dot ( . ) ) that you want to systematically rename:\n>> ")

    soldier(folder_path, blacklist_file, file_ext)
    print("\n\nYour folder was prettified")
