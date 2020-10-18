if __name__ == '__main__':
    #Users Input
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    #declare the winners score as maxx and runner up score as runner_up
    maxx = max(arr)
    runner_up = min(arr)

    #update runner_up
    for i in arr:
        if (i < maxx) and (i > runner_up):
            runner_up = i
    
    #display the runner up score
    print(runner_up)
