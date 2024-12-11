

def tokenize(s: str) -> list[str]:
    " Convert a string into a list of tokens. "
    return s.replace('(', ' ( ').replace(')', ' ) ').split()