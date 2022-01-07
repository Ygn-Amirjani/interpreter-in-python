from lexer import TokenRules

if __name__ == '__main__' :
    data = '''
        // FOR STATE
        for(int i=0; i<10 ; i+=1){
            counter = i;
            if(counter == i){
                counter += 1 ;
            }else
                counter += 2;
        }
        /*
            jast for check
        */   
    '''
    a = TokenRules(data)
    a.print_token()