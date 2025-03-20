import random
from character import Character

class Hero(Character):
    def __init__(self, combat_strength, health_points):
        super().__init__(combat_strength, health_points)

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()

    # Hero's Attack Function
    def hero_attacks(self, monster):
        ascii_image = """
                                    @@   @@ 
                                    @    @  
                                    @   @   
                @@@@@@          @@  @    
                @@       @@        @ @@     
            @%         @     @@@ @       
                @        @@     @@@@@     
                @@@@@        @@       
                @    @@@@                
            @@@ @@                        
        @@     @                         
    @@*       @                          
    @        @@                          
            @@                                                    
            @   @@@@@@@                    
            @            @                  
        @              @                  

    """
        print(ascii_image)
        print(f"    |    Player's weapon {self.combat_strength} ---> Monster {monster.health_points}")
        
        if self.combat_strength >= monster.health_points:
            # Player was strong enough to kill monster in one blow
            monster.health_points = 0
            print("    |    You have killed the monster")

        else:
            # Player only damaged the monster
            monster.health_points -= self.combat_strength
            print(f"    |    You have reduced the monster's health to: {monster.health_points}")

        return monster.health_points
