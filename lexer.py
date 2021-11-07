from Token import TypeToken, NewToken 

class Lexer :

    input: str
    current_position: int   # current position in input (points to current char)
    current_reading_position: int   # current reading position in input (after current char)
    current_char: str   # current char under examination


    def __init__(self, input: str) -> None:

        self.input = input
        self.current_position = 0 
        self.current_reading_position = 0
        self.current_char = ''

        self.read_char()


    """ The purpose of readChar is to give us the next character and advance our position in the input string."""
    def read_char(self) -> None :
        # it does is to check whether we have reached the end of input
        if self.current_reading_position >= len(self.input) :
            self.current_char = ""  # we haven’t read anything yet
        else :
            self.current_char = self.input[self.current_reading_position]   # next char

        self.position = self.current_reading_position
        self.current_reading_position += 1 


    """ We look at the current character under examination  and return a token depending on which character it is."""
    def NextToken(self) -> NewToken :

        next: NewToken

        self.eatWhitespace()

        if self.current_char == '*' :
            next = NewToken(TypeToken.MULTIPLICATION, self.current_char)
        elif self.current_char == '/' :
            next = NewToken(TypeToken.DIVISION, self.current_char)
        elif self.current_char == '%' :
            next = NewToken(TypeToken.REMAININ, self.current_char)
        elif self.current_char == '+' :
            next = NewToken(TypeToken.TOTAL, self.current_char)
        elif self.current_char == '-' :
            next = NewToken(TypeToken.SUBMISSION, self.current_char)
        elif self.current_char == '=' :
            next = NewToken(TypeToken.ASSIGN, self.current_char)
        elif self.current_char == '!' :
            next = NewToken(TypeToken.NOT, self.current_char)
        elif self.current_char == '!=' :
            next = NewToken(TypeToken.UNEQUAL, self.current_char)
        elif self.current_char == '==' :
            next = NewToken(TypeToken.EQUAL, self.current_char)
        elif self.current_char == '<' :
            next = NewToken(TypeToken.SMALLER, self.current_char)
        elif self.current_char == '>' :
            next = NewToken(TypeToken.BIGGER, self.current_char)
        elif self.current_char == ',' :
            next = NewToken(TypeToken.COMMA, self.current_char)
        elif self.current_char == ';' :
            next = NewToken(TypeToken.SEMICOLON, self.current_char)
        elif self.current_char == '(' :
            next = NewToken(TypeToken.LPAREN, self.current_char)
        elif self.current_char == ')' :
            next = NewToken(TypeToken.RPAREN, self.current_char)
        elif self.current_char == '{' :
            next = NewToken(TypeToken.LBRACE, self.current_char)
        elif self.current_char == '}' :
            next = NewToken(TypeToken.RBRACE, self.current_char)
        else :
            if self.isLetter(self.current_char) :
                Id = self.readIdentifier()  # we call readChar() repeatedly and advance our readPosition .
                next = NewToken(NewToken.LookupIdent(Id), Id)
                return next     # we don’t need the call to readChar() after the switch statement again.
            elif self.isDigit(self.current_char) :
                Id = self.readNumber()
                next = NewToken(TypeToken.INT, self.readNumber())
                return next 
            else :
                next = NewToken(TypeToken.ILLEGAL, self.current_char)


        self.read_char()
        return next


    def eatWhitespace(self) -> None :
        while self.current_char == ' ' or self.current_char == '\t' or self.current_char == '\n' or self.current_char == '\r' :
            self.read_char()


    """ it reads in an identifier and advances our lexer’s positions until it encounters a non-letter-character."""
    def readIdentifier(self) -> str :
        current_position = self.current_position
        while self.isLetter(self.current_char) :
            self.read_char()

        return self.input[current_position: self.current_position]


    def readNumber(self) -> str :
        current_position = self.current_position
        while self.isDigit(self.current_char) :
            self.read_char()


    """ just checks whether the given argument is a letter."""
    def isLetter(self, currentChar: str) -> bool :
        return 'a' <= currentChar and currentChar <= 'z' or 'A' <= currentChar and currentChar <='Z' or currentChar == '_'


    def isDigit(self, currentChar: str) -> bool :
        return currentChar >= '0' and currentChar <= '9'
