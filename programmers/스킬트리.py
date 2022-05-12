def ispossible(skill, alpha):
    if not skill:
        return True
    if len(skill) == 1:
        if alpha[skill[0]] == 1:
            return True
        else:
            return False
    
    if alpha[skill[0]] != 1:
        return False
    
    for i in range(len(skill)-1):
        if alpha[skill[i+1]] - alpha[skill[i]] != 1:
            return False
    
    return True

def solution(skill, skill_trees):
    answer = 0
    alpha = dict()
    for i in range(len(skill)):
        alpha[skill[i]] = (i+1)
    
    for i in range(len(skill_trees)):
        temp = ""
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in alpha:
                temp += skill_trees[i][j]
        skill_trees[i] = temp
    
    for _skill in skill_trees:
        if ispossible(_skill, alpha):
            answer += 1

    return answer