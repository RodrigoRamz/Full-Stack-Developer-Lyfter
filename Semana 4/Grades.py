grades = int (input ('Add your number of grades to be added: '))
results = []
scores = []
for i in range (grades):
    score = int (input (f'Add Score {i + 1}: ' ))
    scores.append(score)
    if score >= 70:
        print ('Approved')
        results.append('Approved')
    else:
        print ('Unapproved')
        results.append('Unapproved')
total_approved = results.count('Approved')
total_unapproved = results.count('Unapproved')
print (f' Your Total Scores Approved are: {total_approved}')
print (f' Your Total Scores Unapproved are: {total_unapproved}')
average_score = sum(scores) / len (scores)
print (f' Your average score is: {average_score: .0f}')
total_score_approved = [s for r, s in zip(results, scores) if r == 'Approved']
total_score_unapproved = [s for r, s in zip(results, scores) if r == 'Unapproved']
average_score_approved = sum(total_score_approved) / len(total_score_approved)
average_score_unapproved = sum( total_score_unapproved) / len (total_score_unapproved)
print (f' Average Score Approved: {average_score_approved: .0f}')
print (f' Average Score Unapproved: {average_score_unapproved: .0f}')