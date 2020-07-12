class AdminData:
    def __init__(self):
        self.ownerid = [346107577970458634, 387909176921292801, 553154552908611584]

    def is_admin(self, authorid):
        if authorid == self.ownerid[0]:
            return True
        elif authorid == self.ownerid[1]:
            return True
        elif authorid == self.ownerid[2]:
            return True
        else:
            return False
