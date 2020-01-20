def start_quiz():
    tests = open('tests.txt')
    list_questions = []

    for line in tests:
        list_questions.append(line)

    questions = []
    for test in list_questions:
        questions.append(test.split('|'))
    
    scores = 0
    for q in questions:
        length = len(q) - 1
        print(q[0])
        for i in range(1, length):
            print(str(i), ". ", q[i])
        
        print('Input number of ur answer : ')
        answer = int(input())
        if (q[answer] == q[-1].replace('**', '').replace('\n','')):
            scores +=1
        
    print('U answered right on ', scores, ' questions.')

k = 0
while True:
    print("***Quiz***")
    print("1. Start the test")
    print("2. Quit")
    
    k = int(input())
    if k == 1:
        start_quiz()
    elif k == 2:
        break

