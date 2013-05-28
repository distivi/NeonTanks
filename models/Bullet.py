
# Bullet class

class Bullet(cocos.sprite.Sprite):
    def __init__(self,path,position):
        super(Bullet,self).__init__(path,position)
        self.x,self.y = position
        self.speed = 1
        self.schedule(self.update)

    def move(self,direction=0):
        #needed to define how to determine the direction
        self.x += self.speed;

    def update(self,obj):
        pass

    def getPosition(self):
        return (self.x,self.y)

    def destroy(self): #destroy object
        pass
