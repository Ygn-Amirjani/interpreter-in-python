from Token import TokenType, NewToken, LookupIdent

class Lexer :

    input: str  # Source Code
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
            self.current_char = ''  # we haven’t read anything yet
        else :
            self.current_char = self.input[self.current_reading_position]   # next char

        self.current_position = self.current_reading_position
        self.current_reading_position += 1 


    """ We look at the current character under examination  and return a token depending on which character it is."""
    def NextToken(self) -> str :

        next: str

        self.eatWhitespace()
        if self.current_char == '':
            next = NewToken(TokenType.EOF, self.current_char)
        elif self.current_char == '*' :
            if self.peekChar() == '=' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.MULTIPLICATION_ABBREVIATION, sum_string) 
            else :
                next = NewToken(TokenType.MULTIPLICATION, self.current_char)
        elif self.current_char == '/' :
            if self.peekChar() == '=' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.DIVISION_ABBREVIATION, sum_string) 
            else :
                next = NewToken(TokenType.DIVISION, self.current_char)
        elif self.current_char == '%' :
            if self.peekChar() == '=' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.REMAININ_ABBREVIATION, sum_string) 
            else :
                next = NewToken(TokenType.REMAININ, self.current_char)
        elif self.current_char == '+' :
            if self.peekChar() == '+' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.ADDITIVE, sum_string)
            elif self.peekChar() == '=' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.PLURAL_ABBREVIATION, sum_string) 
            else :
                next = NewToken(TokenType.TOTAL, self.current_char)
        elif self.current_char == '-' :
            if self.peekChar() == '-' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.DECREASE, sum_string) 
            elif self.peekChar() == '=' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.SUBTRACTION_ABBREVIATION, sum_string) 
            else :
                next = NewToken(TokenType.SUBMISSION, self.current_char)
        elif self.current_char == '=' :
            if self.peekChar() == '=' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.EQUAL, sum_string)
            else :
                next = NewToken(TokenType.ASSIGN, self.current_char)
        elif self.current_char == '!' :
            if self.peekChar() == '=' :
                current_char = self.current_char
                self.read_char()
                sum_string = str(current_char) + str(self.current_char)
                next = NewToken(TokenType.UNEQUAL, sum_string)
            else :
                next = NewToken(TokenType.NOT, self.current_char)
        elif self.current_char == '<' :
            next = NewToken(TokenType.SMALLER, self.current_char)
        elif self.current_char == '>' :
            next = NewToken(TokenType.BIGGER, self.current_char)
        elif self.current_char == ',' :
            next = NewToken(TokenType.COMMA, self.current_char)
        elif self.current_char == ';' :
            next = NewToken(TokenType.SEMICOLON, self.current_char)
        elif self.current_char == '(' :
            next = NewToken(TokenType.LPAREN, self.current_char)
        elif self.current_char == ')' :
            next = NewToken(TokenType.RPAREN, self.current_char)
        elif self.current_char == '{' :
            next = NewToken(TokenType.LBRACE, self.current_char)
        elif self.current_char == '}' :
            next = NewToken(TokenType.RBRACE, self.current_char)
        else :
            if self.isLetter(self.current_char) :
                Id = self.readIdentifier()  # we call readChar() repeatedly and advance our readPosition .
                next = NewToken(LookupIdent(Id), Id)
                return next     # we don’t need the call to readChar() after the switch statement again.
            elif self.isDigit(self.current_char) :
                next = NewToken(TokenType.INT, self.readNumber())
                return next 
            else :
                next = NewToken(TokenType.ILLEGAL, self.current_char)


        self.read_char()
        return next


    """ Go through empty spaces ."""
    def eatWhitespace(self) -> None :
        while self.current_char == ' ' or self.current_char == '\t' or self.current_char == '\n' or self.current_char == '\r' :
            self.read_char()

    """ Read the next character. for -> (*= or ++ or == or != and ect)"""
    def peekChar(self) -> str :
        if self.current_reading_position >= len(self.input) :
            return ''
        else :
            return self.input[self.current_reading_position]


    """ just checks whether the given argument is a letter."""
    def isLetter(self, currentChar: str) -> bool :
        # we accept 'YEGANE', 'amirjani', 'Yegane_Amirjani'
        return 'a' <= currentChar and currentChar <= 'z' or 'A' <= currentChar and currentChar <='Z' or currentChar == '_'


    """ it reads in an identifier and advances our lexer’s positions until it encounters a non-letter-character."""
    def readIdentifier(self) -> str :
        current_position = self.current_position
        
        while self.isLetter(self.current_char) :
            self.read_char()

        return self.input[current_position: self.current_position]

    """ just checks whether the given argument is a Digit """
    def isDigit(self, currentChar: str) -> bool :
        return currentChar >= '0' and currentChar <= '9'

    """ it reads in an identifier and advances our lexer’s positions until it encounters a non-Digit-character."""
    def readNumber(self) -> str :
        current_position = self.current_position
        while self.isDigit(self.current_char) :
            self.read_char()

        return self.input[current_position: self.current_position]



