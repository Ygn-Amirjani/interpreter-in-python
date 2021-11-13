class TokenType:

    ILLEGAL = 'ILLEGAL' #signifiles a character we don't know about
    EOF     = 'EOF'     # End of file


    # Identifiers + literals
    IDENT = 'IDENT' # add, foobar, x, y, ...
    INT   = 'INT'   # 1343456


    # Operators
    MULTIPLICATION = '*'

    MULTIPLICATION_ABBREVIATION = '*='

    DIVISION = '/'
    REMAININ = '%'

    DIVISION_ABBREVIATION = '/='
    REMAININ_ABBREVIATION = '%='

    TOTAL       = '+'
    SUBMISSION  = '-'

    ADDITIVE = '++'
    DECREASE = '--'

    PLURAL_ABBREVIATION      = '+='
    SUBTRACTION_ABBREVIATION = '-='

    ASSIGN = '='
    NOT    = '!'    

    EQUAL   = '=='
    UNEQUAL = '!='

    SMALLER = '<'
    BIGGER  = '>'

    SMALLER_EQUALS = '<='
    LARGER_EQUALS = '>='


    # Delimiters
    COMMA     = ','
    SEMICOLON = ';'

    LPAREN = '('
    RPAREN = ')'
    LBRACE = '{'
    RBRACE = '}'


    # Keywords
    INTEGER   = 'INTEGER'
    DOUBLE    = 'DOUBLE'
    FLOAT     = 'FLOAT'
    CHARACTER = 'CHARACTER'

    IF    = 'IF'
    ELSE  = 'ELSE'
    WHILE = 'WHILE'
    FOR   = 'FOR'

    PRINT  = 'PRINT'
    RETURN = 'RETURN'

    TRUE  = 'TRUE'
    FALSE = 'FALSE'

    

class NewToken :

    tokenType: TokenType
    character: str

    def __init__(self, tokenType: TokenType, character: str) -> None:
        self.tokenType = tokenType
        self.character = character

    def __repr__(self) -> str :
        return f"( '{self.tokenType}' , '{self.character}' )"
    
# is a dictionary for find token type :)
keywords = {
    'int': TokenType.INTEGER, 'double': TokenType.DOUBLE, 'float': TokenType.FLOAT, 'char': TokenType.CHARACTER,
    'if': TokenType.IF, 'else': TokenType.ELSE, 'while': TokenType.WHILE, 'for': TokenType.FOR,
    'printf': TokenType.PRINT, 'return':TokenType.RETURN,
    'true': TokenType.TRUE, 'false': TokenType.FALSE
}

""" checks the keywords table to see whether the given identifier is in fact a keyword ."""
def LookupIdent(Identification: str) -> str :
    if Identification in keywords:
        return keywords[Identification]
        
    return TokenType.IDENT
