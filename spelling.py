import names
from gtts import gTTS
import tempfile
import os


def spellApco(word):
    alphabet = {
        'A': "Adam",
        'B': "Boy",
        'C': "Charles",
        'D': "David",
        'E': "Edward",
        'F': "Frank",
        'G': "George",
        'H': "Henry",
        'I': "Ida",
        'J': "John",
        'K': "King",
        'L': "Lincoln",
        'M': "Mary",
        'N': "Nora",
        'O': "Ocean",
        'P': "Paul",
        'Q': "Queen",
        'R': "Robert",
        'S': "Sam",
        'T': "Tom",
        'U': "Union",
        'V': "Victor",
        'W': "William",
        'X': "X-Ray",
        'Y': "Young",
        'Z': "Zebra",
    }

    # Say the word at the beginning
    spelling = word + ". "

    # Spell out each letter of the word
    for letter in word:
        if letter == " ":
            spelling += "... "
        else:
            spelling += letter.upper() + " as in " + alphabet.get(letter.upper(), "Umm, I don't know this one.") + ". "

    # Say the word again at the end
    spelling += word + "."

    return spelling


if __name__ == '__main__':
    # Get a random name
    print("Selecting random name...")
    name = names.get_full_name()

    # Spell out name
    spelling = spellApco(name)

    # Get MP3 of phrase
    print("Converting text to speech...")
    tts = gTTS(text=spelling)

    # Write MP3 to a temporary file
    f = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.write_to_fp(f)
    f.close()

    # Play MP3 in temporary file
    print("Speaking...")
    response = "R"
    while response.upper() == "R":
        os.system("start " + f.name)

        # Ask user to repeat or continue
        response = input("(R)epeat or (C)ontinue? ")

    # Close and delete temporary file
    os.remove(f.name)

    # Check is name is correct
    response = input("What was the name? ")
    if response.upper() == name.upper():
        print("Correct! Well done!")
    else:
        print("The correct answer was '%s'." % name)
