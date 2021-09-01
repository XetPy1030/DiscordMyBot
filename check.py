class empty:
    def __init__(self):
        self.name = "empty"

def check_log(db, id):
    if str(id) not in db["accounts"].keys():
        db["accounts"].update({str(id): {"xp": 0, "popularity": 0, "game": False, "gameData": {"id": "0"}}})