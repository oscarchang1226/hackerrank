from typing import List

'''
A group of work friends at Amazon is playing a competitive video game together.
During the game, each player receives a certain amount of points based on their
performance. At the end of a round, players who achieve at least a cutoff rank
get to "level up" their character, gaining increased abilities for them. Given
the scores of the players at the end of the round, how many players will be able
to level up their character?

Note that players with equal scores will have equal ranks, but the player with
the next lowest score will be ranked based on the position within the list of
all players' scores. For example, if there are four players, and three players
tie for first place, their ranks would be 1,1,1, and 4. Also, no player with a
score of O can level up, no matter what their rank.

Write an algorithm that returns the count of players able to level up their
character.

Return an integer representing the number of players who will be able to level
up their characters at the end of the round.
'''
def count_level_up_players(cutOffRank: int, num: int, scores: List[int]) -> int:
    levelUps = 0
    currentRank = 1
    currentScore = None
    scores.sort(reverse = True)
    if cutOffRank > 0:
        for i in range(num):
            
            if scores[i] == 0:
                break;
            
            if currentScore == None:
                levelUps += 1
                currentScore = scores[i]
                
            elif currentScore == scores[i]:
                levelUps += 1
                
            elif currentScore > scores[i]:
                currentRank = i + 1
                if currentRank > cutOffRank:
                    break
                
                else:
                    levelUps += 1
                    currentScore = scores[i] 
        
    return levelUps
