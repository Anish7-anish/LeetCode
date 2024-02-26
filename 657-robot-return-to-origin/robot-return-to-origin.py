class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c=0
        for i in moves:
            if i =="R":
                c+=1
            elif i == "L":
                c-=1
            elif i == "U":
                c+=3
            else:
                c-=3
        if c == 0:
            return True
        else:
            return False

        