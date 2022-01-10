import ply.lex as lex

class TokenRules(object) :

    input: str

    # Keywords for create token
    Keywords = {

        'int'   : 'INT' ,
        'char'  : 'CHAR',

        'if'    : 'IF',
        'else'  : 'ELSE',
        'while' : 'WHILE',
        'do'    : 'DO',
        'for'   : 'FOR',

    }

    # Operators, Identifiers + literals, Delimiters for create token
    tokens = [

        # Literals(identifier , integer)
        'IDENTIFIER', 'NUMBER',

        # Operators (+,-,*,/,%,|,&,~,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
        'TIMES', 'DIVIDE', 'PLUS', 'MINUS', 'EQ', 'NOT_EQ', 'LE', 'LT',
        'GE', 'GT', 

        # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, |=)
        'PLUSASSIGN', 'ASSIGN',

        # Delimeters ( ) [ ] , ; :
        'COMMA', 'SEMICOLON',
        'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',

    ] + list(Keywords.values())

    # Regular expression rules for Operators
    t_PLUSASSIGN = r'\+='

    t_TIMES  = r'\*'

    t_DIVIDE = r'/'

    t_PLUS   = r'\+' 

    t_MINUS  = r'-'
    
    t_NOT_EQ = r'!='
    t_EQ     = r'=='
    t_ASSIGN = r'='

    t_LE = r'<='
    t_GE = r'>='

    t_LT = r'<'
    t_GT = r'>'

    # Regular expression rules for Delimiters
    t_COMMA     = r','
    t_SEMICOLON = r';'

    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    t_LBRACE = r'{'
    t_RBRACE = r'}'

    # Tabs
    t_ignore = ' \t' 
    
    # comment
    t_ignore_COMMENT1 = r'//.*'
    t_ignore_COMMENT2 = r'/\*(.|\n)*?\*/'

    """ Constructor ! """
    def __init__(self, input: str, **kwargs) -> None:
        super().__init__()
        self.lexer = lex.lex(module=self, **kwargs)
        self.input = input     

    """ Check if the strings read are in the keywords """
    def t_IDENTIFIER(self, t: tokens) -> str :
        r'[a-zA-Z_][a-zA-Z_0-9]*' # zero char or more 
        t.type = self.Keywords.get(t.value, 'IDENTIFIER')    # Check for reserved words 
        return t

    """ If the given string is a number, we cast it and return it """
    def t_NUMBER(self, t: tokens) -> int:
        r'\d+' # One Number or more 
        t.value = int(t.value)
        return t

    """ Cross the blank lines and note that you have to add to the number of lines """
    def t_newline(self, t: tokens) -> None:
        r'\n+'
        t.lexer.lineno += len(t.value)

    """ input is the input text string and token is a token instance """
    def find_column(self, input: str, token) -> int:
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start)  + 1

    """ If the compiler does not recognize a token : """
    def t_error(self, t: tokens) -> None:
        print('ILLEGAL %s' % t.value[0])
        t.lexer.skip(1)

    """ Give the lexer some input and Tokenize """
    def print_token(self) -> None:
        self.lexer.input(self.input)   
        for tok in self.lexer :  
            print(tok)
