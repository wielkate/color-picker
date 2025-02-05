class ColorData:
    def __init__(self, row):
        self.name = row[1]
        self.description = row[2]
        self.hex = row[3]
        self.r = row[4]
        self.g = row[5]
        self.b = row[6]