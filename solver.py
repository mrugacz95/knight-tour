import numpy as np

MOVES = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-1, 2)]
SIZE_X = 7
SIZE_Y = 5
START_X = 0
START_Y = 0
chessboard = np.full((SIZE_Y, SIZE_X), -1)


def move(pos_x: int, pos_y: int, counter: int) -> bool:
    if not (0 <= pos_x < SIZE_X):
        return False
    if not (0 <= pos_y < SIZE_Y):
        return False
    if not chessboard[pos_y, pos_x] == -1:
        return False

    chessboard[pos_y, pos_x] = counter + 1

    if counter == SIZE_X * SIZE_Y - 1:
        return True

    for (dx, dy) in MOVES:
        if move(pos_x + dx, pos_y + dy, counter + 1):
            return True

    chessboard[pos_y, pos_x] = -1
    return False


def main():
    if move(START_X, START_Y, 0):
        print("Possible")

        from matplotlib import pyplot as plt

        board = np.zeros((SIZE_Y * SIZE_X))
        board[::2] = 1
        board = board.reshape((SIZE_Y, SIZE_X))
        plt.matshow(board, cmap='gray')
        pos = (START_Y, START_X)
        for i in range(SIZE_Y * SIZE_X):
            next_pos = np.argwhere(chessboard == (i + 1))[0]
            plt.plot([pos[1], next_pos[1]], [pos[0], next_pos[0]], 'k-', lw=2, c='r')
            plt.scatter(pos[1], pos[0], c='r')
            pos = next_pos
        plt.scatter(pos[1], pos[0], c='r')
        plt.show()

    else:
        print("Impossible")


if __name__ == '__main__':
    main()
