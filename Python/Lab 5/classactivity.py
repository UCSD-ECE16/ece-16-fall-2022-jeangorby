class Instrument:
    # name: decides the type of instrument
    # notes: provides range of notes that instrument can play
    # age: allows us to value instruments for sale
    name = ""
    notes = []
    __age = 0
    def __init__(self, name, notes, age):
        self.name = name
        self.notes = notes
        self.__age = age

    # Since age is private, we need a way to get it
    def getAge(self): 
        return self.__age

    # Main method to play the instrument
    def playNote(self, note):
        if(note in self.notes):
            print("Playing note: ", note)
        else:
            print("Instrument can't play this note")
    
    # Get the price of the instrument depending on how old it is
    def evaluateValue(self):
        # 1000 dollars, the older the instrument the more expensive
        return self.__age * 1000

# Piano is a type of an instrument 
# I chose piano cause I like pianos
class Piano(Instrument):
    def __init__(self, name, notes, age):
        super().__init__(name, notes, age)

guitar = Instrument("Guitar", [1,2,3], 10)
print(guitar)
guitar.playNote(4)