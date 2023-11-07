import random

initial_bag = [[1,3], [0,4], [-1,5], [-2,4], [-3,3], [-4,2], [-5,2],
[-6,1], [-7,1], [-8,1], ["Auto-fail",1], ["Elder-Sign",1], ["Elder Thing",4],
["Tablet",4], ["Cultist",4], ["Skull",4], ["Bless",10], ["Curse",10],
["Frost",8]]

class bag:
    def __init__(self):
        self.content = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.clear = True
        self.quantity = 0

    def random(self):
        if self.quantity != 0:
            n = random.randint(1,self.quantity)
            s = 0
            for i in range(19):
                s += self.content[i]
                if n <= s:
                    return initial_bag[i][0]
        return '-'

#NIGHT OF THE ZEALOT
  
    def NIGHT_OF_THE_ZEALOT_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 0 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 16

    def NIGHT_OF_THE_ZEALOT_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 16

    def NIGHT_OF_THE_ZEALOT_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 1 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 17

    def NIGHT_OF_THE_ZEALOT_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 18

#THE DUNWICH LEGACY

    def THE_DUNWICH_LEGACY_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 0 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 15

    def NIGHT_OF_THE_ZEALOT_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 15

    def NIGHT_OF_THE_ZEALOT_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 1 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 16

    def NIGHT_OF_THE_ZEALOT_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 17

#THE PATH TO CARCOSA
        
    def THE_PATH_TO_CARCOSA_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 0 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 3 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 15

    def THE_PATH_TO_CARCOSA_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 3 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 15

    def THE_PATH_TO_CARCOSA_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 1 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 3 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 16

    def THE_PATH_TO_CARCOSA_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 3 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 17

#THE FORGOTTEN AGE
        
    def THE_FORGOTTEN_AGE_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 1 #-2
        self.content[4] = 1 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 1 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 14

    def THE_FORGOTTEN_AGE_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 3 #0
        self.content[2] = 1 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 0 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 1 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 14

    def THE_FORGOTTEN_AGE_hard(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 1 #-1
        self.content[3] = 1 #-2
        self.content[4] = 2 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 1 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 14

    def THE_FORGOTTEN_AGE_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 1 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 2 #-4
        self.content[6] = 0 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 1 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 15
        
#THE CIRCLE UNDONE
        
    def THE_CIRCLE_UNDONE_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 1 #-2
        self.content[4] = 1 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 13

    def THE_CIRCLE_UNDONE_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 13

    def THE_CIRCLE_UNDONE_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 2 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 13

    def THE_CIRCLE_UNDONE_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 13
                
#THE DREAM-EATERS A
        
    def THE_DREAM_EATERS_A_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 0 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 2 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 0 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 14

    def THE_DREAM_EATERS_A_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 2 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 0 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 14

    def THE_DREAM_EATERS_A_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 2 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 1 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 2 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 0 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 15

    def THE_DREAM_EATERS_A_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 2 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 0 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 16

#THE DREAM-EATERS B
        
    def THE_DREAM_EATERS_B_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 0 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 2 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 17

    def THE_DREAM_EATERS_B_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 2 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 17

    def THE_DREAM_EATERS_B_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 1 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 2 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 18

    def THE_DREAM_EATERS_B_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 2 #"Elder Thing"
        self.content[13] = 0 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 19
                
#THE INNSMOUTH CONSPIRACY
        
    def THE_INNSMOUTH_CONSPIRACY_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 0 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 2 #"Elder Thing"
        self.content[13] = 2 #"Tablet"
        self.content[14] = 2 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 20

    def THE_INNSMOUTH_CONSPIRACY_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 2 #"Elder Thing"
        self.content[13] = 2 #"Tablet"
        self.content[14] = 2 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 20

    def THE_INNSMOUTH_CONSPIRACY_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 1 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 2 #"Elder Thing"
        self.content[13] = 2 #"Tablet"
        self.content[14] = 2 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 21

    def THE_INNSMOUTH_CONSPIRACY_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 2 #"Elder Thing"
        self.content[13] = 2 #"Tablet"
        self.content[14] = 2 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 22

#EDGE OF THE EARTH
        
    def EDGE_OF_THE_EARTH_easy(self):
        self.content[0] = 3 #1
        self.content[1] = 2 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 0 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 16

    def EDGE_OF_THE_EARTH_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 1 #"Frost"
        self.clear = False
        self.quantity = 17

    def EDGE_OF_THE_EARTH_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 2 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 2 #"Frost"
        self.clear = False
        self.quantity = 18

    def EDGE_OF_THE_EARTH_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 1 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 1 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 0 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 1 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 3 #"Frost"
        self.clear = False
        self.quantity = 18

#THE SCARLET KEYS
        
    def THE_SCARLET_KEYS_easy(self):
        self.content[0] = 2 #1
        self.content[1] = 3 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 0 #-3
        self.content[5] = 0 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 1 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 16

    def THE_SCARLET_KEYS_standart(self):
        self.content[0] = 1 #1
        self.content[1] = 2 #0
        self.content[2] = 3 #-1
        self.content[3] = 2 #-2
        self.content[4] = 1 #-3
        self.content[5] = 1 #-4
        self.content[6] = 0 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 1 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 16

    def THE_SCARLET_KEYS_hard(self):
        self.content[0] = 0 #1
        self.content[1] = 3 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 1 #-4
        self.content[6] = 1 #-5
        self.content[7] = 0 #-6
        self.content[8] = 0 #-7
        self.content[9] = 0 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 1 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 17

    def THE_SCARLET_KEYS_expert(self):
        self.content[0] = 0 #1
        self.content[1] = 1 #0
        self.content[2] = 2 #-1
        self.content[3] = 2 #-2
        self.content[4] = 2 #-3
        self.content[5] = 2 #-4
        self.content[6] = 1 #-5
        self.content[7] = 1 #-6
        self.content[8] = 0 #-7
        self.content[9] = 1 #-8
        self.content[10] = 1 #"Auto-fail"
        self.content[11] = 1 #"Elder-Sign"
        self.content[12] = 1 #"Elder Thing"
        self.content[13] = 1 #"Tablet"
        self.content[14] = 0 #"Cultist"
        self.content[15] = 2 #"Skull"
        self.content[16] = 0 #"Bless"
        self.content[17] = 0 #"Curse"
        self.content[18] = 0 #"Frost"
        self.clear = False
        self.quantity = 18
