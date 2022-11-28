import string as str


def count_letters(string):
    """Count number of words in a sentence that end with 's' or 'r'

    Args:
        string (_type_): string

    Returns:
        int: number of words that end with 'r' or 's'
    """
    words = 0
    last = " "
    for i in range(len(string)):
        if(
            not string[i].isalpha() and
            (last == "r" or last == "s")
        ):
            words += 1

        last = string[i]

    if (last == "r" or last == "s"):  # r was an x
        words += 1

    return words
