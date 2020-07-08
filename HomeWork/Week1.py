class GPA :
    def __init__(self, name, val1 , val2 , val3, val4, score) :
        self.name = name 
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
        self.val4 = val4
        self.score = score

    def FindScore(self) :
        index = []
        for i in self.score :
            if i == 'A' :
                index.append(4)
            elif i == 'B+' :
                index.append(3.5)
            elif i == 'B' :
                index.append(3)
            elif i == 'C+' :
                index.append(2.5)
            elif i == 'C' :
                index.append(2)
            elif i == 'D+' :
                index.append(1.5)
            elif i == 'D' :
                index.append(1)
            elif i == 'F' :
                index.append(0)
        return ((index[0] * self.val1) + (index[1] * self.val2) + (index[2] * self.val3) + (index[3] * self.val4))/(self.val1 + self.val2 + self.val3 + self.val4)
        
    
    def __str__(self):
        return f'Name : {self.name} and Score : {self.FindScore()}'


Me = GPA('Poowadol Rungtabnapa', 3, 3, 1, 3,['B','B','B','B+'])

print(Me)