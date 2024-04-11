def principal():
    print('Executando funcao principal')
    
    def primeira_func_interna():
        print('Primeira funcao interna')
        
    def segunda_func_interna():
        print('Segunda funcao interna')
        
        
    primeira_func_interna()
    segunda_func_interna()
        
        
principal()