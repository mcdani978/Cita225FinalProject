# ANSI color codes
class colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Print colored text
print(colors.RED + "This text is red." + colors.RESET)
print(colors.GREEN + "This text is green." + colors.RESET)
print(colors.BLUE + "This text is blue." + colors.RESET)

print(f"{colors.BOLD}BOLD TEXT{colors.RESET}\n{colors.BLUE}BLUE TEXT{colors.RESET}")