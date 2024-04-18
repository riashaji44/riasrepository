class Student:

    def _init_(self, fname, lname, id, energy_level=10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level
    
    def _str_(self):
        return f"{self.lname}:{self.id}"
    
    def greeting(self, fname, lname):
        return fname + lname + "says 'hello'!"
    
    def take_exam(self, energy_level):
        return energy_level - 1
    
    def get_energy_level(self):
        return self.energy_level