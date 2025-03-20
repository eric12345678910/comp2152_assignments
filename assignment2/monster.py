import random
from character import Character

class Monster(Character):
    def __init__(self, combat_strength, health_points):
        super().__init__(combat_strength, health_points)

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()
    
    # Monster's Attack Function
    def monster_attacks(self, hero):
        ascii_image2 = """                                                                 
            @@@@ @                           
        (     @*&@  ,                         
        @               %                       
        &#(@(@%@@@@@*   /                      
        @@@@@.                                
                @       /                    
                    %         @                 
                ,(@(*/           %              
                @ (  .@#                 @   
                            @           .@@. @
                    @         ,              
                        @       @ .@          
                                @              
                            *(*  *      
                """
        print(ascii_image2)
        print(f"    |    Monster's Claw {self.combat_strength} ---> Player ({hero.health_points}) ")
        if self.combat_strength >= hero.health_points:
            # Monster was strong enough to kill player in one blow
            hero.health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            hero.health_points -= self.combat_strength
            print(f"    |    The monster has reduced Player's health to: {hero.health_points}")
        return hero.health_points