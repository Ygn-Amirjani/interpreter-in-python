import ply.lex as lex

Keywords = {

    'int'   : 'INTEGER' ,
    'double': 'DOUBLE',
    'float' : 'FLOAT',
    'char'  : 'CHARACTER',

    'if'    : 'IF',
    'else'  : 'ELSE',
    'while' : 'WHILE',
    'for'   : 'FOR',

    'print' : 'PRINT',
    'return': 'RETURN',

    'True'  : 'TRUE',
    'False' : 'FALSE',

}

tokens = [

    'IDENT', 'INT',
    'MULTIPLICATION_ABBREVIATION' , 'MULTIPLICATION',
    'DIVISION_ABBREVIATION', 'DIVISION',
    'REMAININ_ABBREVIATION', 'REMAININ',
    'PLURAL_ABBREVIATION', 'ADDITIVE', 'TOTAL',
    'DECREASE_ABBREVIATION','DECREASE', 'MINUS',
    'EQUAL', 'ASSIGN', 
    'UNEQUAL', 'NOT',
    'SMALLER_EQUALS', 'SMALLER',
    'LARGER_EQUALS', 'BIGGER',
    'COMMA', 'SEMICOLON',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',

] + list(Keywords.values())

# Regular expression rules for Operators
t_MULTIPLICATION_ABBREVIATION = r'\*='
t_MULTIPLICATION = r'\*'

t_DIVISION_ABBREVIATION = r'/='
t_DIVISION = r'/'

t_REMAININ_ABBREVIATION = r'%='
t_REMAININ = r'%'

t_PLURAL_ABBREVIATION = r'\+='
t_ADDITIVE = r'\++'
t_TOTAL    = r'\+'

t_DECREASE_ABBREVIATION = r'-='
t_DECREASE = r'--'
t_MINUS    = r'-'

t_EQUAL  = r'=='
t_ASSIGN = r'='

t_UNEQUAL = r'!='
t_NOT     = r'!'

t_SMALLER_EQUALS = r'<='
t_SMALLER        = r'<'

t_LARGER_EQUALS = r'>='
t_BIGGER        = r'>'

# Regular expression rules for Delimiters
t_COMMA     = r','
t_SEMICOLON = r';'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

""" Check if the strings read are in the keywords """
def t_IDENT(t: tokens) -> str :
    r'[a-zA-Z_][a-zA-Z_0-9]*' # zero char or more 
    t.type = Keywords.get(t.value,'IDENT')    # Check for reserved words
    return t

""" If the given string is a number, we cast it and return it """
def t_INT(t: tokens) -> int :
    r'\d+' # One Number or more 
    t.value = int(t.value)
    return t

""" Cross the blank lines and note that you have to add to the number of lines """
def t_newline(t: tokens) -> None :
    r'\n+'  # One line or more
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t' # Tabs

""" If the compiler does not recognize a token : """
def t_error(t: tokens) -> None :
    print('ILLEGAL %s' % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def main() -> None :
    data = '''
        for(int i=0; i<=10 ; i+=1){
            counter++;
            if(counter == i)
                i-- ;
        }   
    '''
    lexer.input(data)   # Give the lexer some input

    for tok in lexer :  # Tokenize
        print(tok)

if __name__ == '__main__' :
    main()
