def check(a,n_list):
    """Returns the operation performed (such as append(),remove(),insert(),print(),etc) in the list if the operations are valid, -1 otherwise"""
    #split the given string a
    s = a.split()
    
    #Check the length of splited String 'a'
    #if length(s) == 1,it means string should be print,sort,pop and reverse
    if len(s) == 1:
        #check for print only
        if s[0]=='print':
            return eval(s[0]+'(' + 'n_list' + ')')
        #if s contains other than 'print'
        else:
            return eval('n_list' + '.' + s[0] + '()')
    #if length == 2, it means 's' contains either ['append','e'] or ['remove','e']
    elif len(s) == 2:
        return eval('n_list' + '.' + s[0] + '(' + s[1] + ')')
    
    #if length == 3,it means 's' contains ['insert', 'i', 'e']
    elif len(s) == 3:
        return eval('n_list' + '.' + s[0] + '(' + s[1] + ',' + s[2] + ')')
    
    #if invalid operations return -1
    else:
        return -1

n_list = []
if __name__ == '__main__':
    N = int(input())

    for i in range(N):
        a = input()
        check(a,n_list)
