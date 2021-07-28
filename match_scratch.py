import match

from enum import Enum
class Command(Enum):
    QUIT = 0
    RESET = 1

original_text = 'now is the time for all good men to come to the aid of their party.'
match.match(original_text, ['-LRB-', 'and', 'do', 'weird', 'stuff', 'with', 'punctuation', '-RRB-'])
match.match("") command:
    case Command.QUIT:
        quit()
    case Command.RESET:
        reset()