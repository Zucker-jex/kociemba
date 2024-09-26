import random


class RubiksCube:
    def __init__(self):
        # Initialize the cube with centers defining the face colors
        # Each face has 9 blocks, indexed from 1 to 54
        # Faces: U (1-9), L (10-18), F (19-27), R (28-36), B (37-45), D (46-54)
        self.cube = [''] * 55  # Using 1-based indexing; index 0 unused
        # Initialize each face with its respective color based on center block
        # Original state: BBBBBBBBBLLLLLLLLLUUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDD
        for i in range(1, 55):
            if 1 <= i <= 9:
                self.cube[i] = 'B'
            elif 10 <= i <= 18:
                self.cube[i] = 'L'
            elif 19 <= i <= 27:
                self.cube[i] = 'U'
            elif 28 <= i <= 36:
                self.cube[i] = 'R'
            elif 37 <= i <= 45:
                self.cube[i] = 'F'
            elif 46 <= i <= 54:
                self.cube[i] = 'D'

    def rotate_face_clockwise(self, face):
        """
        Rotates the given face clockwise.
        face: one of 'U', 'L', 'F', 'R', 'B', 'D'
        """
        # Define the mapping for each face
        face_indices = {
            'U': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'L': [10, 11, 12, 13, 14, 15, 16, 17, 18],
            'F': [19, 20, 21, 22, 23, 24, 25, 26, 27],
            'R': [28, 29, 30, 31, 32, 33, 34, 35, 36],
            'B': [37, 38, 39, 40, 41, 42, 43, 44, 45],
            'D': [46, 47, 48, 49, 50, 51, 52, 53, 54],
        }

        # Define adjacent faces and their corresponding indices that need to be rotated
        adjacent = {
            'U': [('B', [37, 38, 39]), ('R', [28, 29, 30]), ('F', [19, 20, 21]), ('L', [10, 11, 12])],
            'D': [('F', [25, 26, 27]), ('R', [34, 35, 36]), ('B', [43, 44, 45]), ('L', [16, 17, 18])],
            'F': [('U', [7, 8, 9]), ('R', [10, 13, 16]), ('D', [3, 2, 1]), ('L', [36, 33, 30])],
            'B': [('U', [1, 2, 3]), ('L', [28, 31, 34]), ('D', [9, 8, 7]), ('R', [19, 22, 25])],
            'L': [('U', [1, 4, 7]), ('F', [19, 22, 25]), ('D', [46, 49, 52]), ('B', [45, 42, 39])],
            'R': [('U', [3, 6, 9]), ('B', [37, 40, 43]), ('D', [48, 51, 54]), ('F', [21, 24, 27])],
        }

        # Rotate the face itself
        original = [self.cube[i] for i in face_indices[face]]
        rotated = [original[6], original[3], original[0],
                   original[7], original[4], original[1],
                   original[8], original[5], original[2]]
        for idx, val in zip(face_indices[face], rotated):
            self.cube[idx] = val

        # Rotate the adjacent faces' edge blocks
        temp = [self.cube[i] for i in adjacent[face][0][1]]
        for i in range(3):
            self.cube[adjacent[face][0][1][i]
                      ] = self.cube[adjacent[face][1][1][i]]
            self.cube[adjacent[face][1][1][i]
                      ] = self.cube[adjacent[face][2][1][i]]
            self.cube[adjacent[face][2][1][i]
                      ] = self.cube[adjacent[face][3][1][i]]
            self.cube[adjacent[face][3][1][i]] = temp[i]

    def apply_move(self, move):
        """
        Applies a single move to the cube.
        move: string representing the move, e.g., 'U', 'R', 'F', 'D', 'L', 'B'
              can also include modifiers: 'U', 'U2', 'U\''
        """
        if move.endswith('2'):
            times = 2
            face = move[0]
        elif move.endswith('\''):
            times = 3  # Equivalent to three clockwise rotations
            face = move[0]
        else:
            times = 1
            face = move[0]

        for _ in range(times):
            self.rotate_face_clockwise(face)

    def generate_shuffle(self, num_moves=20):
        """
        Generates a random shuffle sequence of num_moves moves.
        """
        possible_moves = ['U', 'U\'', 'U2', 'L', 'L\'', 'L2',
                          'F', 'F\'', 'F2', 'R', 'R\'', 'R2',
                          'B', 'B\'', 'B2', 'D', 'D\'', 'D2']
        shuffle = [random.choice(possible_moves) for _ in range(num_moves)]
        return shuffle

    def apply_shuffle(self, shuffle):
        """
        Applies a sequence of moves to the cube.
        shuffle: list of move strings
        """
        for move in shuffle:
            self.apply_move(move)

    def check_centers(self):
        """
        Checks if the center blocks are still correctly oriented.
        Returns True if all centers are correct, False otherwise.
        """
        centers = {
            'B': self.cube[5],
            'L': self.cube[14],
            'U': self.cube[23],
            'R': self.cube[32],
            'F': self.cube[41],
            'D': self.cube[50],
        }
        correct = {
            'B': 'B',
            'L': 'L',
            'U': 'U',
            'R': 'R',
            'F': 'F',
            'D': 'D',
        }
        for face, color in centers.items():
            if color != correct[face]:
                return False
        return True

    def roll_cube(self):
        """
        Performs a cube rotation to realign the centers.
        For simplicity, perform a U move until centers are aligned.
        """
        # This is a placeholder for cube rotation logic.
        # Implementing full cube rotations (X, Y, Z axes) is complex.
        # Here, we'll assume that performing U, L, F, etc., can help realign.
        # In practice, a more sophisticated method is needed.
        # For demonstration, we'll perform random moves until centers align.
        attempts = 0
        max_attempts = 100
        while not self.check_centers() and attempts < max_attempts:
            move = random.choice(['U', 'U\'', 'U2',
                                  'L', 'L\'', 'L2',
                                  'F', 'F\'', 'F2',
                                  'R', 'R\'', 'R2',
                                  'B', 'B\'', 'B2',
                                  'D', 'D\'', 'D2'])
            self.apply_move(move)
            attempts += 1
        if not self.check_centers():
            print("Unable to realign centers after shuffling.")

    def validate_cube(self):
        """
        Validates the cube state to ensure it's legal.
        Returns True if valid, False otherwise.
        """
        from collections import Counter
        color_counts = Counter(self.cube[1:])  # Exclude index 0
        expected_counts = {'B': 9, 'L': 9, 'U': 9, 'R': 9, 'F': 9, 'D': 9}
        for color, count in expected_counts.items():
            if color_counts[color] != count:
                print(f"Color {color} has {count} occurrences, expected 9.")
                return False
        # Additional checks for unique pieces can be implemented here
        return True

    def get_flat_cube_string(self):
        """
        Returns the cube state as a flat string based on indexing (1-54).
        """
        return ''.join(self.cube[1:])

    def get_multidimensional_dataset_string(self):
        """
        Generates the multidimensional dataset string with aligned centers.
        Returns a string representation of the cube.
        """
        # For alignment, we'll format the cube in the same layout as the indexing
        # Top face
        top = self.cube[1:10]
        # Middle layer: L, F, R
        left = self.cube[10:19]
        front = self.cube[19:28]
        right = self.cube[28:37]
        # Back face
        back = self.cube[37:46]
        # Down face
        down = self.cube[46:55]

        # Create a formatted string
        lines = []
        lines.append("------------------------------------------------------")
        lines.append(f"            |{top[0]}   {top[1]}   {top[2]}|")
        lines.append(f"            |{top[3]}   {top[4]}   {top[5]}|")
        lines.append(f"            |{top[6]}   {top[7]}   {top[8]}|")
        lines.append("------------------------------------------------------")
        # Middle layer: L, F, R
        for i in range(3):
            line = f"|{left[i*3]}   {left[i*3+1]}   {left[i*3+2]}| " \
                   f"|{front[i*3]}   {front[i*3+1]}   {front[i*3+2]}| " \
                   f"|{right[i*3]}   {right[i*3+1]}   {right[i*3+2]}|"
            lines.append(line)
        lines.append("------------------------------------------------------")
        # Back face
        lines.append(f"            |{back[0]}   {back[1]}   {back[2]}|")
        lines.append(f"            |{back[3]}   {back[4]}   {back[5]}|")
        lines.append(f"            |{back[6]}   {back[7]}   {back[8]}|")
        lines.append("------------------------------------------------------")
        # Down face
        lines.append(f"            |{down[0]}   {down[1]}   {down[2]}|")
        lines.append(f"            |{down[3]}   {down[4]}   {down[5]}|")
        lines.append(f"            |{down[6]}   {down[7]}   {down[8]}|")
        lines.append("------------------------------------------------------")

        return "\n".join(lines)

    def print_cube(self):
        """
        Prints the cube state in a readable format.
        """
        print(self.get_multidimensional_dataset_string())


def main():
    # Step 0: Initialize the Rubik's Cube
    cube = RubiksCube()
    print("Original Cube State:")
    print(cube.get_flat_cube_string())
    cube.print_cube()

    # Step 1: Generate shuffle formula
    shuffle = cube.generate_shuffle(num_moves=20)
    print("\nShuffle Sequence (20 moves):")
    print(" ".join(shuffle))

    # Step 2: Apply scrambling formula
    cube.apply_shuffle(shuffle)
    print("\nCube State After Shuffling:")
    print(cube.get_flat_cube_string())
    cube.print_cube()

    # Validate the cube state
    if not cube.validate_cube():
        print("Invalid cube state detected after shuffling.")
        return

    # Step 3: Correct Rubik's Cube if centers are misaligned
    if not cube.check_centers():
        print("\nCenters misaligned. Performing correction...")
        cube.roll_cube()
        print("Cube State After Correction:")
        print(cube.get_flat_cube_string())
        cube.print_cube()
        if not cube.check_centers():
            print("Failed to correct centers.")
            return
    else:
        print("\nCenters are correctly aligned.")

    # Validate again after correction
    if not cube.validate_cube():
        print("Invalid cube state detected after correction.")
        return

    # Step 4: Generate multidimensional dataset string
    dataset_string = cube.get_flat_cube_string()
    print("\nFinal Multidimensional Dataset String:")
    print(dataset_string)


if __name__ == "__main__":
    main()
