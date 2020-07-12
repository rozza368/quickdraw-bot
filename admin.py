class AdminData:
    def __init__(self):
        self.ownerid = [346107577970458634, 387909176921292801, 553154552908611584]

    def is_admin(self, authorid):
        return authorid in self.ownerid

