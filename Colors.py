#this class will store various ANSI values to color code the text in the console
#Credit for idea: ChatGPT.
#
#Prompts given:
#1) I am working on my text-based python project and would like to update the text color. Is this possible?
#2) Where can I find all of the ANSI escape code values?
#3) Can you give me an ANSI value for a lime color?
#4) Can you give me a light blue ANSI color code?
class Colors:
    RESET = '\033[0m'       #back to default text
    GREEN = '\033[32m'
    LIME = '\033[92m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    RED = '\033[31m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'