class AdRotator:
    def __init__(self, ads):
        self.ads = ads
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.ads:
            raise StopIteration("No advertisements available")
            
        current_advertizmo = self.ads[self.index]
        
        self.index = (self.index + 1) % len(self.ads)
        
        return current_advertizmo

if __name__ == "__main__":
    ads = ["Реклама за баби", "Реклама за парфюм", "Реклама на вилици"]
    rotator = AdRotator(ads)
    
    for _ in range(10):
        print(next(rotator))
