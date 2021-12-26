import ply.lex as lex

class TokenRules(object) :

    # Keywords for create token
    Keywords = {

        'long'  : 'LONG',
        'int'   : 'INTEGER' ,
        'double': 'DOUBLE',
        'float' : 'FLOAT',
        'char'  : 'CHARACTER',
        'CONST' : 'CONST',

        'if'    : 'IF',
        'switch': 'SWITCH',
        'case'  : 'CASE',
        'else'  : 'ELSE',
        'while' : 'WHILE',
        'do'    : 'DO',
        'for'   : 'FOR',

        'print' : 'PRINT',
        'return': 'RETURN',

        'True'  : 'TRUE',
        'False' : 'FALSE',

        'break'    : 'BREAK',
        'continue' : 'CONTINUE',

    }

    # Operators, Identifiers + literals, Delimiters for create token
    tokens = [

        # Literals(identifier , integer)
        'IDENT', 'NUMBER',

        # Operators (+,-,*,/,%,|,&,~,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
        'MULTIPLICATION', 'DIVISION', 'REMAININ', 'PLUS', 'MINUS', 'EQUAL', 'UNEQUAL', 'NOT',
        'OR', 'AND', 'SMALLER_EQUALS', 'SMALLER',
        'LARGER_EQUALS', 'BIGGER', 

        # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, |=)
        'MULTIPLICATION_ABBREVIATION', 'DIVISION_ABBREVIATION', 'REMAININ_ABBREVIATION', 'PLURAL_ABBREVIATION',
        'DECREASE_ABBREVIATION', 'ASSIGN',

        # Increment/decrement (++,--)
        'PLUSPLUS', 'MINUSMINUS' ,

        # Delimeters ( ) [ ] , ; :
        'COMMA', 'SEMICOLON', 'COLON',
        'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET','LCURLYBRACKET', 'RCURLYBRACKET'

    ] + list(Keywords.values())

    # Regular expression rules for Operators
    t_MULTIPLICATION_ABBREVIATION = r'\*='
    t_MULTIPLICATION = r'\*'

    t_DIVISION_ABBREVIATION = r'/='
    t_DIVISION = r'/'

    t_REMAININ_ABBREVIATION = r'%='
    t_REMAININ = r'%'

    t_PLURAL_ABBREVIATION = r'\+='
    t_PLUSPLUS = r'\+\+'
    t_PLUS    = r'\+'

    t_DECREASE_ABBREVIATION = r'-='
    t_MINUSMINUS = r'--'
    t_MINUS    = r'-'

    t_EQUAL  = r'=='
    t_ASSIGN = r'='

    t_UNEQUAL = r'!='
    t_NOT    = r'!'

    t_OR  = r'\|\|'
    t_AND = r'&&'

    t_SMALLER_EQUALS = r'<='
    t_SMALLER        = r'<'

    t_LARGER_EQUALS = r'>='
    t_BIGGER        = r'>'

    # Regular expression rules for Delimiters
    t_COMMA     = r','
    t_SEMICOLON = r';'
    t_COLON = r':'

    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'

    t_LCURLYBRACKET = r'{'
    t_RCURLYBRACKET = r'}'

    # Tabs
    t_ignore = ' \t' 
    
    # comment
    t_ignore_COMMENT1 = r'//.*'
    t_ignore_COMMENT2 = r'/\*(.|\n)*?\*/'

    """ Check if the strings read are in the keywords """
    def t_IDENT(self, t: tokens) -> str :
        r'[a-zA-Z_][a-zA-Z_0-9]*' # zero char or more 
        t.type = self.Keywords.get(t.value, 'IDENT')    # Check for reserved words 
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
        t.lexer.skip    (1)

    """ Build the lexer """
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    """ Give the lexer some input and Tokenize """
    def main(self, data: str) -> None:
        self.lexer.input(data)   
        for tok in self.lexer :  
            print(tok)
