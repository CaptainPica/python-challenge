import csv
with open('election_data.csv', newline='') as csvfile:
    elections = csv.reader(csvfile)
    next(elections)
    cands = []
    votes = []
    for i in elections:
        try:
            votes[cands.index(i[2])] += 1
        except:
            cands.append(i[2])
            votes.append(1)
    #Needed for when I didn't know about next()
    #cands.pop(0)
    #votes.pop(0)
    total = sum(votes)
    print('Election Results\n-------------------------')
    print(f'Total Votes: {total}\n-------------------------')
    for j in range(len(cands)):
        print(f'{cands[j]}: {round((votes[j]/total)*100,3)}% ({votes[j]})')
    print(f'-------------------------\nWinner: {cands[votes.index(max(votes))]}\n-------------------------')
    with open('output.txt','w') as f:
        f.write('Election Results\n-------------------------\n')
        f.write(f'Total Votes: {total}\n-------------------------\n')
        for k in range(len(cands)):
            f.write(f'{cands[k]}: {round((votes[k]/total)*100,3)}% ({votes[k]})\n')
        f.write(f'-------------------------\nWinner: {cands[votes.index(max(votes))]}\n-------------------------')