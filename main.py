from Token import TokenType
from lexer import Lexer

def main() -> None :
    sorce_code = 'int x = 5 + 7 ;'
    go_to_lexer = Lexer(sorce_code)
    find_token = go_to_lexer.NextToken()

    while find_token.tokenType != TokenType.EOF :
        print(find_token)
        find_token = go_to_lexer.NextToken()


if __name__ == '__main__' :
    main()