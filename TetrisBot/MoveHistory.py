class MoveHistory:
    def __init__(self):
        self.move_history_list = []

    def add_directional_move(self, x, y):
        if x == -1:
            self.move_history_list.append("LEFT")
        elif x == 1:
            self.move_history_list.append("RIGHT")
        elif y == 1:
            self.move_history_list.append("DOWN")
        else:
            print(f"ERROR BRO WHAT THE FUCK IS: {x}, {y}")

    def add_rotation_move(self):
        self.move_history_list.append("ROTATE")

    def add_hold_move(self, add_to_tail=True):
        if add_to_tail:
            self.move_history_list.append("HOLD")
        else:
            self.move_history_list.insert(0, "HOLD")

    def clone(self):
        clone = MoveHistory()
        for item in self.move_history_list:
            clone.move_history_list.append(item)
        return clone
