from string import ascii_lowercase


def caesarshiftcipher(message, shift):
    sb = []
    current_char = []
    length = len(message)
    letters = list(ascii_lowercase)

    shift = shift % 26

    for i in range(0, length):
        current_char = [
            j for j in range(len(list(ascii_lowercase)))
            if list(ascii_lowercase)[j] == message[i]][0]
        # sb.append(current_char)

        if (letters[current_char] > 'z' or letters[current_char] < 'a'):
            return 'invalid'
        elif (letters[current_char + shift] > 'z'):
            current_char = current_char - 26
        elif (letters[current_char + shift] < 'a'):
            current_char = current_char + 26

        sb.append(letters[current_char + shift])

    return "".join(sb)
