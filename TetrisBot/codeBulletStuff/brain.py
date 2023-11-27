import random

class Brain:
    def __init__(self, is_first):
        self.multipliers = {}
        if is_first:
            self.set_as_my_multipliers()
        else:
            self.randomize_multipliers()

    def randomize_multipliers(self):
        self.multipliers = {
            "holeCountMultiplier": 100 * random.uniform(0, 2),
            "openHoleCountMultiplier": 70 * random.uniform(0, 2),
            "maximumLineHeightMultiplier": 1 * random.uniform(0, 2),
            "addedShapeHeightMultiplier": 1 * random.uniform(0, 2),
            "pillarCountMultiplier": 4 * random.uniform(0, 2),
            "blocksInRightMostLaneMultiplier": 10 * random.uniform(0, 2),
            "nonTetrisClearPenalty": 20 * random.uniform(0, 2),
            "blocksAboveHolesMultiplier": 5 * random.uniform(0, 2),
            "bumpinessMultiplier": 5 * random.uniform(0, 2),
            "tetrisRewardMultiplier": -10 * random.uniform(0, 2)
        }

    def set_as_my_multipliers(self):
        self.multipliers = {
            "holeCountMultiplier": 100,
            "openHoleCountMultiplier": 70,
            "maximumLineHeightMultiplier": 1,
            "addedShapeHeightMultiplier": 1,
            "pillarCountMultiplier": 4,
            "blocksInRightMostLaneMultiplier": 10,
            "nonTetrisClearPenalty": 20,
            "blocksAboveHolesMultiplier": 5,
            "bumpinessMultiplier": 5,
            "tetrisRewardMultiplier": -10
        }

    def mutate(self):
        mutation_rate = 0.1
        for key in self.multipliers:
            if random.random() < mutation_rate:
                self.multipliers[key] *= random.uniform(0.95, 1.05)

    def clone(self):
        clone = Brain(False)
        clone.multipliers = self.multipliers.copy()
        return clone

    def get_cost_of_matrix(self, block_matrix):
        lines_cleared_which_arent_tetrises = 1 if 0 < block_matrix.lines_cleared < 4 else 0
        tetrises = 1 if block_matrix.lines_cleared == 4 else 0

        block_matrix.cost = (
            block_matrix.hole_count * self.multipliers["holeCountMultiplier"] +
            block_matrix.open_hole_count * self.multipliers["openHoleCountMultiplier"] +
            block_matrix.blocks_above_holes * self.multipliers["blocksAboveHolesMultiplier"] +
            lines_cleared_which_arent_tetrises * self.multipliers["nonTetrisClearPenalty"] +
            tetrises * self.multipliers["tetrisRewardMultiplier"] +
            block_matrix.maximum_line_height * self.multipliers["maximumLineHeightMultiplier"] +
            block_matrix.added_shape_height * self.multipliers["addedShapeHeightMultiplier"] +
            block_matrix.pillar_count * self.multipliers["pillarCountMultiplier"] +
            block_matrix.blocks_in_right_lane * self.multipliers["blocksInRightMostLaneMultiplier"] +
            block_matrix.bumpiness * self.multipliers["bumpinessMultiplier"]
        )

        return block_matrix.cost

    # The write_multipliers method seems to be specific to a graphical environment
    # (like p5.js in JavaScript), which doesn't have a direct equivalent in standard Python.
    # Therefore, this method can't be directly translated without knowing more about the
    # intended graphical environment in Python (e.g., Pygame, Tkinter, etc.).
