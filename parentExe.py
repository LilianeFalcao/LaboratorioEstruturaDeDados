# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()

    #------- COLOQUE SEU CÓDIGO AQUI -------
    for e in expression:
        if e in "{([":
            pilha.push(e)
        elif e in "}])":
            if pilha.is_empty(): 
                return False
            topo = pilha.pop()
        if (e == "}" and topo != "{") or \
            (e == ")" and topo != "(") or \
            (e == "]" and topo != "["):
                return False

    return pilha.is_empty()

    #---------------------------------------


# Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False
