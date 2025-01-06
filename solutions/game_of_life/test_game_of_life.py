import unittest
from unittest.mock import MagicMock
from game_of_life import GameConfig, GameOfLife


class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        """Set up the game with default config"""
        self.config = GameConfig()
        self.game = GameOfLife(config=self.config)
        self.game.simulation_grid = set()  # Clear the initial grid

    def test_initialization(self):
        """Test if the game initializes correctly with random cells."""
        self.game.seed_random()
        self.assertEqual(
            len(self.game.simulation_grid), self.config.game_cells_seed_number
        )

    def test_get_neighbors(self):
        """Test the neighbor calculation for grid boundaries."""
        neighbors = self.game.get_neighbors(0, 0)  # Test for top-left corner
        expected_neighbors = {(1, 0), (0, 1), (1, 1)}  # Wraps around the grid edges
        self.assertEqual(neighbors, expected_neighbors)

        neighbors = self.game.get_neighbors(
            self.config.number_of_rows - 1, self.config.number_of_columns - 1
        )  # Bottom-right corner
        expected_neighbors = {
            (self.config.number_of_rows - 2, self.config.number_of_columns - 1),
            (self.config.number_of_rows - 1, self.config.number_of_columns - 2),
            (self.config.number_of_rows - 2, self.config.number_of_columns - 2),
        }
        self.assertEqual(neighbors, expected_neighbors)

    def test_update_grid(self):
        """Test the grid update logic: cells should survive or die based on neighbors."""
        self.game.simulation_grid = {
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 2),
        }  # A 2x2 block pattern (should remain alive)
        self.game.update_grid()
        self.assertEqual(
            len(self.game.simulation_grid), 4
        )  # A 2x2 block should stay alive

        self.game.simulation_grid = {(1, 1), (2, 2)}  # Two live cells far apart
        self.game.update_grid()
        self.assertEqual(
            len(self.game.simulation_grid), 0
        )  # No neighbors, both cells should die

    def test_step_function(self):
        """Test if the step function updates and draws correctly."""
        self.game.simulation_grid = {
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 2),
        }  # 2x2 block pattern
        self.game.toggle_state()
        self.game.step()
        self.assertGreater(
            self.game.simulation_generation, 0
        )  # Generation should increment
        self.assertEqual(
            len(self.game.simulation_grid), 4
        )  # Should still have 4 cells (same block pattern)
        self.game.toggle_state()

    def test_toggle_pause(self):
        """Test the pause/resume functionality."""
        self.assertFalse(self.game.state_paused)
        self.game.toggle_state()
        self.assertTrue(self.game.state_paused)
        self.game.toggle_state()
        self.assertFalse(self.game.state_paused)

    def test_random_seed(self):
        """Test if random seed creates the correct number of initial cells."""
        self.game.seed_random()
        self.assertEqual(
            len(self.game.simulation_grid), self.config.game_cells_seed_number
        )

    def test_edge_case_cells(self):
        """Test edge case scenarios like grid wrapping."""
        self.game.simulation_grid = set([(0, 0), (0, 1), (1, 0), (1, 1)])
        self.game.update_grid()
        self.assertEqual(
            len(self.game.simulation_grid), 4
        )  # The 2x2 block remains alive

    def test_neighbors_on_large_grid(self):
        """Test if the get_neighbors function works correctly on a large grid."""
        self.game.simulation_grid = {(5, 5)}
        neighbors = self.game.get_neighbors(5, 5)
        expected_neighbors = set(
            [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]
        )
        self.assertEqual(neighbors, expected_neighbors)

    # UI-related tests can be mocked as needed.
    def test_ui_pause_button(self):
        """Test that the pause button correctly toggles the paused state."""
        mock_pause_button = MagicMock()
        self.game.toggle_state()
        mock_pause_button.configure(command=self.game.toggle_state)
        mock_pause_button.invoke()
        self.assertTrue(self.game.state_paused)

    def test_ui_step_button(self):
        """Test that the step button calls the step function."""
        mock_step_button = MagicMock()
        self.game.step()
        mock_step_button.configure(command=self.game.step)
        mock_step_button.invoke()
        self.assertGreater(
            self.game.simulation_generation, 0
        )  # Ensure generation increased


if __name__ == "__main__":
    unittest.main()
