from lexer import TokenRules

if __name__ == '__main__' :
    a = TokenRules()
    a.build()
    data = '''
        // FOR STATE
        for(int i=0; i<=10 ; i++){
            counter++;
            if(counter == i){
                counter = (i < 6) ? 0 : 1 ;
            }else
                counter += 2;
        }
        /*
            jast for check
        */   
    '''
    a.main(data)