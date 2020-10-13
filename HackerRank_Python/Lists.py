def check(a,n_list):
    s = a.split()
    if len(s) == 1:
        if s[0]=='print':
            return eval(s[0]+'(' + 'n_list' + ')')
        else:
            return eval('n_list' + '.' + s[0] + '()')

    elif len(s) == 2:
        return eval('n_list' + '.' + s[0] + '(' + s[1] + ')')

    elif len(s) == 3:
        return eval('n_list' + '.' + s[0] + '(' + s[1] + ',' + s[2] + ')')

    else:
        return -1

n_list = []
if __name__ == '__main__':
    N = int(input())

    for i in range(N):
        a = input()
        check(a,n_list)
