class Character:

    def __init__(self, combat_strength, health_points):
        self.__combat_strength = combat_strength
        self.__health_points = health_points

    def __del__(self):
        print("The character object is being destroyed by the garbage collector")
        super().__del__()

    # Getters / Setters: Combat strength
    @property
    def combat_strength(self):
        return self.__combat_strength
    
    @combat_strength.setter
    def combat_strength(self, value):
        self.__combat_strength = value


    # Getters / Setters: Health points
    @property
    def health_points(self):
        return self.__health_points
    
    @health_points.setter
    def health_points(self, value):
        self.__health_points = value
 
