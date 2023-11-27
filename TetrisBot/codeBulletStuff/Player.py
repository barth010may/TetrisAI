class Player:
    def __init__(self, first_player):
        self.brain = Brain(first_player)
        self.fitness = 0
        self.score = 0
        self.tetris_rate = 0
        self.current_game = Game(10, 20)
        self.ai = AI(self.current_game.game_width, self.current_game.game_height, self.brain)
        self.ai.calculate_movement_plan2(self.current_game.current_shape, self.current_game.held_shape, 
                                         self.current_game.next_shape, self.current_game.dead_blocks_matrix)
        self.window_height = canvas_height / 2
        self.window_width = canvas_width / 2
        self.is_dead = False

    def calculate_movement_plan(self):
        self.ai.brain = self.brain  # Just in case
        self.ai.calculate_movement_plan2(self.current_game.current_shape, 
                                         self.current_game.held_shape, 
                                         self.current_game.next_shape, 
                                         self.current_game.dead_blocks_matrix)

    def calculate_fitness(self):
        self.fitness = self.current_game.score * (1 + self.current_game.get_tetris_rate())

    def clone(self):
        clone = Player()
        clone.current_game.needs_new_movement_plan = True
        clone.brain = self.brain.clone()
        clone.ai.brain = clone.brain
        return clone

    def show(self):
        # Assuming some graphics library for push, pop, scale, etc.
        push()
        # translate(self.window_position.x, self.window_position.y)  # Uncomment if needed
        scale(self.window_width / canvas_width, self.window_height / canvas_height)
        self.current_game.draw()
        self.brain.write_multipliers(600, 300)
        pop()

    def update(self):
        if self.is_dead or self.current_game.just_tetrised:
            return

        if self.current_game.needs_new_movement_plan:
            self.ai.calculate_movement_plan2(self.current_game.current_shape, 
                                             self.current_game.held_shape, 
                                             self.current_game.next_shape, 
                                             self.current_game.dead_blocks_matrix)
            self.current_game.needs_new_movement_plan = False

        next_move = self.ai.get_next_move()

        if next_move == "ALL DOWN":
            down_move_multiplier = 5
            while len(self.ai.movement_plan.move_history_list) > 0 and down_move_multiplier > 0:
                self.ai.movement_plan.move_history_list.pop(0)
                self.current_game.move_shape_down()
                down_move_multiplier -= 1
        elif next_move == "HOLD":
            self.current_game.hold_shape()
        elif next_move == "ROTATE":
            self.current_game.rotate_shape()
        elif next_move == "RIGHT":
            self.current_game.move_shape_right()
        elif next_move == "LEFT":
            self.current_game.move_shape_left()
        elif next_move == "DOWN":
            self.current_game.move_shape_down()

        self.is_dead = self.current_game.is_dead
