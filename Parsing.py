from ply.yacc import YaccProduction 
from lexer import TokenRules
import ply.yacc

tokens = TokenRules.tokens

def p_start(token : YaccProduction) :
    """start : nested_stmnt
             | variable_starter"""
    pass

def p_variable_detector(token : YaccProduction):
    """variable_detector : CHAR variable_detector
                         | INT variable_detector
                         | CHAR
                         | INT"""
    pass

def p_assign_detector(token : YaccProduction):
    """assign_detector : identifier_punctuator
                       | identifier_punctuator ASSIGN starting_brace"""
    pass

def p_variable_starter(token : YaccProduction):
    """variable_starter : variable_detector assign_detector SEMICOLON
                        | variable_detector assign_detector COMMA assign_detector SEMICOLON
                        | variable_detector SEMICOLON"""
    pass

def p_variable_starter_chains(token : YaccProduction):
    """variable_starter_chains : variable_starter
                               | variable_starter_chains variable_starter"""
    pass

def p_identifier_punctuator(token : YaccProduction):
    """identifier_punctuator : IDENTIFIER
                             | LPAREN identifier_punctuator RPAREN
                             | identifier_punctuator LPAREN parameter_variable_starter RPAREN
                             | identifier_punctuator LPAREN parameter_variable_starter COMMA parameter_variable_starter RPAREN
                             | identifier_punctuator LPAREN IDENTIFIER RPAREN
                             | identifier_punctuator LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN"""
    pass

def p_parameter_variable_starter(token : YaccProduction):
    """parameter_variable_starter : variable_detector identifier_punctuator
                                  | variable_detector identifier_punctuator_2
                                  | variable_detector empty"""
    pass

def p_starting_brace(token : YaccProduction):
    """starting_brace : assigning
                      | LBRACE starting_brace RBRACE
                      | LBRACE starting_brace COMMA starting_brace RBRACE
                      | LBRACE starting_brace COMMA RBRACE
                      | LBRACE starting_brace COMMA starting_brace COMMA RBRACE"""
    pass

def p_variable_detector_2(token : YaccProduction):
    """variable_detector_2 : variable_detector identifier_punctuator_2
                           | variable_detector empty"""
    pass

def p_identifier_punctuator_2(token : YaccProduction):
    """identifier_punctuator_2 : LPAREN identifier_punctuator_2 RPAREN
                               | identifier_punctuator_2 LPAREN parameter_variable_starter RPAREN
                               | identifier_punctuator_2 LPAREN parameter_variable_starter COMMA parameter_variable_starter RPAREN
                               | identifier_punctuator_2 LPAREN empty RPAREN
                               | LPAREN parameter_variable_starter RPAREN
                               | LPAREN parameter_variable_starter COMMA parameter_variable_starter RPAREN
                               | LPAREN empty RPAREN"""
    pass

def p_stmnt(token : YaccProduction):
    '''stmnt :   expression_2 SEMICOLON
             | nested_stmnt
             | if
             | loops'''
    pass

def p_nested_stmnt(token : YaccProduction):
    """nested_stmnt : LBRACE variable_starter_chains stmnt_chains RBRACE
                    | LBRACE stmnt_chains RBRACE
                    | LBRACE variable_starter_chains RBRACE
                    | LBRACE RBRACE"""
    pass

def p_stmnt_chains(token : YaccProduction):
    """stmnt_chains : stmnt
                    | stmnt_chains stmnt"""
    pass

def p_if(token : YaccProduction):
    """if : IF LPAREN expression RPAREN stmnt
          | IF LPAREN expression RPAREN stmnt ELSE stmnt"""
    pass

def p_loops(token : YaccProduction):
    """loops : WHILE LPAREN expression RPAREN stmnt
             | FOR LPAREN expression_2 SEMICOLON expression_2 SEMICOLON expression_2 RPAREN stmnt
             | DO stmnt WHILE LPAREN expression RPAREN SEMICOLON"""
    pass

def p_expression_2(token : YaccProduction):
    """expression_2 : empty
                    | expression"""
    pass

def p_expression(token : YaccProduction):
    """expression : assigning
                  | expression COMMA assigning"""
    pass

def p_assigning(token : YaccProduction):
    """assigning : equal_unequal
                 | single_operand ASSIGN assigning
                 | single_operand PLUSASSIGN assigning"""
    pass

def p_equal_unequal(token : YaccProduction):
    """equal_unequal : comparison
                     | equal_unequal EQ comparison
                     | equal_unequal NOT_EQ comparison"""
    pass

def p_comparison(token : YaccProduction):
    """comparison : arithmetic_precedence
                  | comparison LT arithmetic_precedence
                  | comparison GT arithmetic_precedence
                  | comparison LE arithmetic_precedence
                  | comparison GE arithmetic_precedence"""
    pass

def p_multiply_division(token : YaccProduction):
    """multiply_division : cast
                         | multiply_division TIMES cast
                         | multiply_division DIVIDE cast"""
    pass

def p_cast(token : YaccProduction):
    """cast : single_operand
            | LPAREN variable_detector_2 RPAREN cast"""
    pass

def p_arithmetic_precedence(token : YaccProduction):
    """arithmetic_precedence : multiply_division
                             | arithmetic_precedence PLUS multiply_division
                             | arithmetic_precedence MINUS multiply_division"""
    pass

def p_single_operand(token : YaccProduction):
    """single_operand : expression_combination
                      | TIMES cast
                      | PLUS cast
                      | MINUS cast"""
    pass

def p_expression_combination(token : YaccProduction):
    """expression_combination : IDENTIFIER
                              | NUMBER
                              | LPAREN expression RPAREN
                              | expression_combination LPAREN assigning RPAREN
                              | expression_combination LPAREN assigning COMMA assigning RPAREN
                              | expression_combination LPAREN RPAREN"""
    pass

def p_empty(token : YaccProduction):
    """empty : """
    pass

data = '''
{
    int i;

    for (i=0;i<10;i=i+1)
        i=i+1;
}
'''

parser = ply.yacc.yacc()
lexer = TokenRules(data)
result = parser.parse(data)

