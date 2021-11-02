class TypeToken:

    ILLEGAL = "ILLEGAL" #signifiles a character we don't know about
    EOF     = "EOF"     # End of file


    # Identifiers + literals
    IDENT = "IDENT" # add, foobar, x, y, ...
    INT   = "INT"   # 1343456


    # Operators
    MULTIPLICATION = "*"

    DIVISION = "/"
    REMAININ = "%"

    TOTAL       = "+"
    SUBMISSION  = "-"

    ASSIGN = "="
    NOT    = "!"

    UNEQUAL = "!="
    EQUAL   = "=="

    SMALLER = "<"
    BIGGER  = ">"


    # Delimiters
    COMMA     = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"


    # Keywords
    INTEGER   = "INTEGER"
    DOUBLE    = "DOUBLE"
    FLOAT     = "FLOAT"
    CHARACTER = "CHARACTER"

    TRUE  = "TRUE"
    FALSE = "FALSE"

    IF    = "IF"
    ELSE  = "ELSE"
    WHILE = "WHILE"
    FOR   = "FOR"
    PRINT = "PRINT"

