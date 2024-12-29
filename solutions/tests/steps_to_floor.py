def steps_to_floor(target_floor: int = None) -> int:
    """
    Calculates the number of steps required to reach a given floor in a building,
    assuming it takes 10 steps to move between consecutive floors.

    If no argument is provided, the function will prompt the user for input.

    Parameters:
      target_floor: int (optional), the floor number to reach (positive, negative, or zero).

    Returns -> int, the total number of steps required.
    """
    if target_floor is None:
        try:
            target_floor = int(input("Enter the floor number you want to reach: "))
        except ValueError:
            raise ValueError("Invalid input. Please enter an integer.")

    # Ensure the target floor is an integer
    assert isinstance(target_floor, int), "Target floor must be an integer"

    # Calculate steps based on the absolute floor value
    return abs(target_floor) * 10


if __name__ == "__main__":
    try:
        print(f"Steps required: {steps_to_floor()}")
    except Exception as e:
        print(f"Error: {e}")

