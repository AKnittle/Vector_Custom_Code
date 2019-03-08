"""
Have Vector quote random Shakespeare monologues from a text file
"""

import anki_vector
import random


# Selects a quote from Shakespeare from random
def get_quote():
    # Open file and read lines
    quote_file = open("Data\Shakespeare.txt", "r")
    quotes = quote_file.readlines()
    # Dynamically change the upper limit to random number selector
    num_quotes = len(quotes)
    rand_line = random.randint(0, num_quotes)
    quote_file.close()
    print(quotes[rand_line])
    return quotes[rand_line]


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        speech = get_quote()
        robot.say_text(speech)


if __name__ == "__main__":
    main()
