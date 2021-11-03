from Token import NewToken, TypeToken

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
        
        self.read_char()
        return next