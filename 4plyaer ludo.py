from distutils.file_util import move_file
import numbers
import ludo
import random number in ludo (1pl)
g = ludo.Game(local_players=[1,3])
there_is_a_winner = False
while not there_is_a_winner:
    (dice,move_pieces,player_pieces,enemy_pieces,player_is_a_winner,there_is_a_winner),player_i = g.get_observation()
if len(move_pieces):
    piece_to_move = move_pieces[np.random.randint(0,len(move_pieces))]
else:
    piece_to_move = -1
_,_,_,_,_,there_is_a_winner = g.answer_observation(piece_to_move)
print("saving history to numpy file")
g.save_hist(f"game_history.npy")
print("saving game video")
g.save_hist_video(f"game_video.mp4")    
