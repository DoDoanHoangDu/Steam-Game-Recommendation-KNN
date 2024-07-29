import tkinter as tk
import os
import Data_handler
import UI_elements as elements

#Get data file paths
dir_path = os.path.dirname(os.path.abspath(__file__))
all_games_path = os.path.join(dir_path, "final_games.csv")
played_games_path = os.path.join(dir_path, "your_games.csv")
fav_games_path = os.path.join(dir_path, "fav_games.csv")

#Load data
df_all, all_games_dict = Data_handler.load_data(all_games_path, 'all')
df_played, played_games_dict = Data_handler.load_data(played_games_path, 'played')
df_fav, fav_games_dict = Data_handler.load_data(fav_games_path, 'fav')

# Create the main window
root = tk.Tk()
root.title('Game Tracker')

# Games List
games_frame = elements.game_list_frame(root, all_games_dict)
search_frame_all = elements.search_frame(root, all_games_dict, games_frame)


#Played list
played_games_frame = elements.played_games_frame(root,played_games_dict)
search_frame_played = elements.search_frame(root, played_games_dict, played_games_frame)
rating_frame = elements.rating_frame(root,games_frame, played_games_frame,played_games_dict)


#Favourite list
fav_games_frame = elements.fav_games_frame(root, fav_games_dict)
check_review_frame = elements.check_review_frame(root, played_games_frame, played_games_dict, fav_games_frame, fav_games_dict)

rcm_frame = elements.rcm_frame(root,played_games_dict, fav_games_dict, dir_path, df_all)

root.mainloop()