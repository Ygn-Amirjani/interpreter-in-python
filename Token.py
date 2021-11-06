class TypeToken:

    ILLEGAL = 'ILLEGAL' #signifiles a character we don't know about
    EOF     = 'EOF'     # End of file


    # Identifiers + literals
    IDENT = 'IDENT' # add, foobar, x, y, ...
    INT   = 'INT'   # 1343456


    # Operators
    MULTIPLICATION = '*'

    DIVISION = '/'
    REMAININ = '%'

    TOTAL       = '+'
    SUBMISSION  = '-'

    ASSIGN = '='
    NOT    = '!'

    UNEQUAL = '!='
    EQUAL   = '=='

    SMALLER = '<'
    BIGGER  = '>'


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

    tokenType: TypeToken
    character: str

    keywords = {
        'int': TypeToken.INTEGER, 'double': TypeToken.DOUBLE, 'float': TypeToken.FLOAT, 'char': TypeToken.CHARACTER,
        'if': TypeToken.IF, 'else': TypeToken.ELSE, 'while': TypeToken.WHILE, 'for': TypeToken.FOR,
        'printf': TypeToken.PRINT, 'return':TypeToken.RETURN,
        'true': TypeToken.TRUE, 'false': TypeToken.FALSE
    }

    def __init__(self, tokenType: TypeToken, character: str) -> None:
        self.tokenType = tokenType
        self.character = character


    """ checks the keywords table to see whether the given identifier is in fact a keyword ."""
    def LookupIdent(self, Identification: str) -> TypeToken :
        if Identification in self.keywords:
            return self.keywords[Identification]
        
        return TypeToken.IDENT
    