from string import ascii_lowercase


def caesarshiftcipher(message, shift):
    """
    This implementation close follows the (faulty) java 
    example from the MOOC and should fail.
    """
    sb = []
    current_char = []
    length = len(message)
    letters = list(ascii_lowercase)

    shift = shift % 26

    for i in range(0, length):
        current_char = [
            j for j in range(len(list(ascii_lowercase)))
            if list(ascii_lowercase)[j] == message[i]][0]

        if (letters[current_char] > 'z' or letters[current_char] < 'a'):
            return 'invalid'
        elif (letters[current_char + shift] > 'z'):
            current_char = current_char - 26
        elif (letters[current_char + shift] < 'a'):
            current_char = current_char + 26

        sb.append(letters[current_char + shift])

    return "".join(sb)


# FOr debugging
# caesarshiftcipher("nop", -3)


def caesarshiftcipher_fixed(message, shift):
    """
    This should work. 
    """
    sb = []
    current_char = []
    # make message lower case
    length = len(message)
    letters = list(ascii_lowercase)

    shift = shift % 26

    for i in range(0, length):
        current_char = [
            j for j in range(len(list(ascii_lowercase)))
            if list(ascii_lowercase)[j] == message[i]][0]

        if (current_char > 25 or current_char < 0):
            return 'invalid'
        elif (current_char + shift > 25):
            current_char = current_char - 26
        elif (current_char + shift < 0):
            current_char = current_char + 26

        sb.append(letters[current_char + shift])

    return "".join(sb)


# caesarshiftcipher_fixed("nop", -3)
