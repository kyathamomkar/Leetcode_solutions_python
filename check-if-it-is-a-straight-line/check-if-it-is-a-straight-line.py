class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        if len(c)==2: return True
        x1 ,y1 = c[0]
        x2, y2 = c[1]
        dy = y2- y1
        dx = x2- x1
        
        for x3,y3 in c:
            if dy*(x3-x1) != dx*(y3-y1):
                return False
        return True
        
        