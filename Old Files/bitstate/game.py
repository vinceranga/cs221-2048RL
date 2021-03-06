import collections, random, operator
import bitstate
import matplotlib.pyplot as plt
import numpy as np
import player
import matplotlib.pyplot as plot
import gameutil
import time

DEPTH = 2
<<<<<<< HEAD
NUM_BOARDS = 1
=======
NUM_BOARDS = 2
>>>>>>> 19a0d7a6e43fa08b4a33a396859e1d1354fc9eef
NUM_GAMES = 10

def bitToBoard(board):
    cboard = np.zeros(16)
    for k in range(16):
        cboard[k] = 1 << ((board >> (4 * k)) & 0xF)
        if cboard[k] == 1:
            cboard[k] = 0
    return cboard[::-1].reshape((4, 4))

def play2048(num_boards,uti):
    games = [bitstate.Game_2048(0,uti.tableL,uti.tableR,uti.scoreTable) for _ in range(num_boards)]
    # game = gamestate.Multi_Game_2048(4)
<<<<<<< HEAD
    weights1 = [range(i,i+4) for i in range(1,5)]
    weights2 = [range(i+3, i-1,-1) for i in range(1, 5)]
    weights3 = [range(i+3, i-1,-1) for i in range(4, 0,-1)]
    weights4 = [range(i, i + 4) for i in range(4, 0,-1)]

    def evalFn(currentGameState):
        if currentGameState.isEnd():
=======
    weights1 = [7,6,5,4,6,5,4,3,5,4,3,2,4,3,2,1]
    weights2 = [4,5,6,7,3,4,5,6,2,3,4,5,1,2,3,4]
    weights3 = [1,2,3,4,2,3,4,5,3,4,5,6,4,5,6,7]
    weights4 = [4,3,2,1,5,4,3,2,6,5,4,3,7,6,5,4]
    '''
    for i in range(1,5):
        weights1 += range(i,i+4)
        weights2 += range(i+3, i-1,-1)
    for i in range(4,0,-1):
        weights3 += range(i+3, i-1,-1)
        weights4 += range(i, i + 4)
    '''
    def evalFn(currentGameState, isEnd, score):
        if isEnd:
>>>>>>> 19a0d7a6e43fa08b4a33a396859e1d1354fc9eef
            return float('-inf')

        def countZeros(board):
            count = 0
            for x in range(16):
                i = 0xF << (4 * x)
                if i & board == 0:
                    count += 1
            return count



        def weightedGrid(currentGameState):
            sum1 = 0.0
            sum2 = 0.0
            sum3 = 0.0
            sum4 = 0.0
<<<<<<< HEAD
            for i in range(4):
                for j in range(4):
                    sum1 += weights1[i][j] * currentGameState.board[i, j]
                    sum2 += weights2[i][j] * currentGameState.board[i, j]
                    sum3 += weights3[i][j] * currentGameState.board[i, j]
                    sum4 += weights4[i][j] * currentGameState.board[i, j]
=======
            #print(bitToBoard(currentGameState))
            for i in range(16):
                val = 1 << ((currentGameState >> (4 * i)) & 0xF)
                if val > 1:
                    sum1 += weights1[i] * val
                    sum2 += weights2[i] * val
                    sum3 += weights3[i] * val
                    sum4 += weights4[i] * val
>>>>>>> 19a0d7a6e43fa08b4a33a396859e1d1354fc9eef
            return max(sum1, sum2, sum3, sum4)

        def monotonicity(cGS, k=10.0):

            def monoEval(a, b, e=1.0):
                # if a == b: b += 1  # make [ v ][ v ] the same as [ v ][ v+1 ]
                if a == b: return 2 * k
                return k / (np.log2(b / a) ** e)
            sum = 0.0

            for r in range(4):
                forw = 0.0
                back = 0.0
                for k in range(3):
                    forw += monoEval(cGS.board[r, k], cGS.board[r, k+1])
                    back += monoEval(cGS.board[r, k+1], cGS.board[r, k])
                sum += max(forw, back)

            for c in range(4):
                forw = 0.0
                back = 0.0
                for k in range(3):
                    forw += monoEval(cGS.board[k, c], cGS.board[k+1, c])
                    back += monoEval(cGS.board[k+1, c], cGS.board[k, c])
                sum += max(forw, back)

            return sum

        def openTilePenalty(cGS, n=5):
            return countZeros(cGS) - n
            # return -((cGS.countZeros() - n) ** 2)

        eval = 0.0
        eval += score
        eval += weightedGrid(currentGameState)
        #eval += monotonicity(currentGameState, k=10.0)
        #eval += 50 * openTilePenalty(currentGameState)

        return eval

    agent = player.Player(DEPTH, evalFn, uti)
    done = False
    total = 0.0
    moves = 0
    highest_tile = []
    while not done:
        values = collections.defaultdict(float)
        count = collections.defaultdict(float)
        for game in games:
            start = time.time()
            action,vals = agent.getAction(game.board)
            end = time.time()
            print("Time: ", end - start)
            print("Action: " + str(action))
            for move,score in vals:
                values[move] += score
                count[move] += 1
        for key in values:
            values[move] /= count[move]
        action = max(values.items(), key=operator.itemgetter(1))[0]
        for game in games:
            print("Action: ",action)
            changed = game.swipe(action)
            if(changed):
                game.placeRandomTile()
            print(bitToBoard(game.board))
            print ("Score: ",game.getScore())
            score = game.getScore()
            if game.isEnd():
                total += game.getScore()
                highest_tile.append(game.getHighest())
                games.remove(game)
        if float(len(games)) < float(1 * num_boards):
            for game in games:
                total += game.getScore()
                highest_tile.append(game.getHighest())
            done = True
    return total / float(num_boards),highest_tile



####################################################

def main():
    score = 0
    lst = []
<<<<<<< HEAD
    dictA = collections.defaultdict(int)
=======
    dict = collections.defaultdict(int)
    uti = gameutil.gameutil()
>>>>>>> 19a0d7a6e43fa08b4a33a396859e1d1354fc9eef
    for i in range(NUM_GAMES):
        curr_score,highest = play2048(NUM_BOARDS, uti)
        score += curr_score
        lst.append(highest)
        dictA[max(highest)] += 1
    print ("Average: ", score / float(NUM_GAMES))
    for i in lst:
        print("Highest tile for all board: ",i)
        print("Highest tile for 1 board: ",max(i))
<<<<<<< HEAD
    print(dictA)
=======
    print(dict)
>>>>>>> 19a0d7a6e43fa08b4a33a396859e1d1354fc9eef
    '''
    averages = []
    for board_size in range(2,9):
        lst = []
        for _ in range(5):
            print _
            lst.append(play2048(board_size))
        averages.append(sum(lst) / 10)
    plot.scatter(range(2,9),averages)
    plot.xlabel('Board Size')
    plot.ylabel('Average Score per Board')
    plot.show()
    '''


if __name__ == '__main__':
    main()
