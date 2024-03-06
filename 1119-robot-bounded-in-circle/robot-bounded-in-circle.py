class Solution:

    def moving(self, direction):
        if direction=="North":
            self.y+=1
        elif direction=="South":
            self.y-=1
        elif  direction == "East":
            self.x+=1
        else:
            self.x-=1
    def isRobotBounded(self, instructions: str) -> bool:

        d_l={"North":"West","West":"South","South":"East","East":"North"}
        d_r={"North":"East","East":"South","South":"West","West":"North"}
        
        direction="North"
        self.x=0
        self.y=0
        for i in instructions:
            if i == "L":
                direction=d_l[direction]
            if i == "R":
                direction = d_r[direction]
            if i=="G":
                self.moving(direction)
        
        if self.x==0 and self.y==0:
            return True
        print(direction)
        if direction != "North":
            return True
        else:
            return False

        
        