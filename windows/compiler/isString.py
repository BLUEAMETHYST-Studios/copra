def isString1(token):
    if token == "'":
        return 1

def isString2(token):
    if token == '"':
        return 2
    
def isEnd1(already, token):
    if already:
        if token == "'":
            return False
    if not already:
        isString1(token=token)
        
def isEnd2(already, token):
    if already == (True, ):
        if token == '"':
            return False
    if not already:
        isString2(token=token)
        