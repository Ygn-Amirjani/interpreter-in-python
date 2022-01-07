from ply.yacc import YaccProduction as YP
from lexer import TokenRules
import ply.yacc as yacc

tokens = TokenRules.tokens


def p_start(t: YP):
    """start : compound_statement
             | declaration"""
    pass


def p_statement_type(t: YP):
    """statement_type : type_specifier statement_type
                      | type_specifier"""
    pass


def p_type_specifier(t: YP):
    """type_specifier : CHAR
                      | INT"""
    pass


def p_init_declarator_compound(t: YP):
    """init_declarator_compound : init_declarator
                                | init_declarator_compound COMMA init_declarator"""
    pass


def p_init_declarator(t: YP):
    """init_declarator : simple_declarator
                       | simple_declarator ASSIGN initializer"""
    pass


def p_multi_specifier(t: YP):
    """multi_specifier : type_specifier multi_specifier
                       | type_specifier"""
    pass


def p_declaration(t: YP):
    """declaration : statement_type init_declarator_compound SEMICOLON
                   | statement_type SEMICOLON"""
    pass


def p_declaration_compound(t: YP):
    """declaration_compound : declaration
                            | declaration_compound declaration"""
    pass


def p_simple_declarator(t: YP):
    """simple_declarator : IDENTIFIER
                         | LPAREN simple_declarator RPAREN
                         | simple_declarator LPAREN parameter_list RPAREN
                         | simple_declarator LPAREN identifier_list RPAREN"""
    pass


def p_parameter_list(t: YP):
    """parameter_list : parameter_declaration
                      | parameter_list COMMA parameter_declaration"""
    pass


def p_parameter_declaration(t: YP):
    """parameter_declaration : statement_type simple_declarator
                             | statement_type declarator_type"""
    pass


def p_identifier_list(t: YP):
    """identifier_list : IDENTIFIER
                       | identifier_list COMMA IDENTIFIER"""
    pass


def p_initializer_1(t: YP):
    """initializer : assignment_expression
                   | LBRACE initializer_list RBRACE
                   | LBRACE initializer_list COMMA RBRACE"""
    pass


def p_initializer_list(t: YP):
    """initializer_list : initializer
                        | initializer_list COMMA initializer"""
    pass


def p_type_name(t: YP):
    """type_name : multi_specifier declarator_type"""
    pass


def p_declarator_type(t: YP):
    """declarator_type : empty
                       | direct_single_declarator"""
    pass


def p_direct_single_declarator(t: YP):
    """direct_single_declarator : LPAREN direct_single_declarator RPAREN
                                | direct_single_declarator LPAREN parameter_type_list RPAREN
                                | LPAREN parameter_type_list RPAREN"""
    pass


def p_statement(t: YP):
    '''statement : expression_statement
                 | compound_statement
                 | if_statement
                 | iteration_statement'''
    pass


def p_expression_statement(t: YP):
    """expression_statement : expression_type SEMICOLON"""
    pass


def p_compound_statement(t: YP):
    """compound_statement : LBRACE declaration_compound statement_list RBRACE
                          | LBRACE statement_list RBRACE
                          | LBRACE declaration_compound RBRACE
                          | LBRACE RBRACE"""
    pass


def p_statement_list(t: YP):
    """statement_list : statement
                      | statement_list statement"""
    pass


def p_parameter_type_list(t: YP):
    """parameter_type_list : empty
                           | parameter_list"""
    pass


def p_if_statement(t: YP):
    """if_statement : IF LPAREN expression RPAREN statement
                    | IF LPAREN expression RPAREN statement ELSE statement"""
    pass


def p_iteration_statement(t: YP):
    """iteration_statement : WHILE LPAREN expression RPAREN statement
                           | FOR LPAREN expression_type SEMICOLON expression_type SEMICOLON expression_type RPAREN statement
                           | DO statement WHILE LPAREN expression RPAREN SEMICOLON"""
    pass


def p_expression_type(t: YP):
    """expression_type : empty
                       | expression"""
    pass


def p_expression(t: YP):
    """expression : assignment_expression
                  | expression COMMA assignment_expression"""
    pass


def p_assignment_expression_1(t: YP):
    """assignment_expression : equality_expression
                             | unary_expression assignment_operator assignment_expression"""
    pass


def p_assignment_operator(t: YP):
    """assignment_operator : ASSIGN
                           | PLUSASSIGN"""
    pass


def p_equality_expression(t: YP):
    """equality_expression : relational_expression
                           | equality_expression EQ relational_expression
                           | equality_expression NOT_EQ relational_expression"""
    pass


def p_relational_expression(t: YP):
    """relational_expression : next_expression
                             | relational_expression LT next_expression
                             | relational_expression GT next_expression
                             | relational_expression LE next_expression
                             | relational_expression GE next_expression"""
    pass


def p_multiplicative_expression(t: YP):
    """multiplicative_expression : cast_expression
                                 | multiplicative_expression TIMES cast_expression
                                 | multiplicative_expression DIVIDE cast_expression"""
    pass


def p_cast_expression(t: YP):
    """cast_expression : unary_expression
                       | LPAREN type_name RPAREN cast_expression"""
    pass


def p_next_expression(t: YP):
    """next_expression : multiplicative_expression
                       | next_expression PLUS multiplicative_expression
                       | next_expression MINUS multiplicative_expression"""
    pass

def p_unary_expression(t: YP):
    """unary_expression : higher_expression
                        | unary_operator cast_expression"""
    pass


def p_unary_operator(t: YP):
    """unary_operator : TIMES
                      | PLUS
                      | MINUS"""
    pass


def p_higher_expression(t: YP):
    """higher_expression : primary_expression
                         | higher_expression LPAREN argument_expression_list RPAREN
                         | higher_expression LPAREN RPAREN"""
    pass


def p_primary_expression(t: YP):
    """primary_expression :  IDENTIFIER
                          |  constant
                          |  LPAREN expression RPAREN"""
    pass


def p_argument_expression_list(t: YP):
    """argument_expression_list :  assignment_expression
                                |  argument_expression_list COMMA assignment_expression"""
    pass


def p_constant(t: YP):
    """constant : NUMBER"""
    pass


def p_empty(t: YP):
    """empty : """
    pass


parser = yacc.yacc()

data = '''
{
    int temp = 0;

    while(tmp > 10)
    {
        temp = temp + 1;
    }
}
'''
lexer = TokenRules(data)
result = parser.parse(data)

