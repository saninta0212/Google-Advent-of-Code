
def read_input(path):
    """
    Opens a file and returns an iterator that reads lines one by one.
    Args:
        path (str): Absolute path to the input file
    Output:
        iterator (file object): An iterator over the lines of the file
    """
    try:
        file_object = open(path, 'r')
        return file_object
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        raise
    