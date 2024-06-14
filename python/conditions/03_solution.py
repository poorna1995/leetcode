
class solution:
    def grade_solution(self,score):
        
        if score >=90:
            grade ='A'
        elif score>=80:
            grade ='B'
        elif score>=60:
            grade ='c'
        elif score>=50:
            grade ='D'
        else:
            grade ='f'
        

print(solution().grade_solution(101))