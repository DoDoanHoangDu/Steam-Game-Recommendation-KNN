import tkinter as tk
from tkinter import messagebox
import re
import pandas as pd
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def update_search(search_frame, games_dict, list_frame):
    games_listbox = None
    search_entry = None
    for widget in search_frame.winfo_children():
        if isinstance(widget,tk.Entry):
            search_entry = widget
    for widget in list_frame.winfo_children():
        if isinstance(widget,tk.Listbox):
            games_listbox = widget
    search_query = search_entry.get().strip().lower()
    games_listbox.delete(0, tk.END)
    if search_query == '':
        for game_info in games_dict.values():
            games_listbox.insert(tk.END, game_info)
    else:
        for game_name, game_info in games_dict.items():
            if search_query in game_name.lower():
                games_listbox.insert(tk.END, game_info)

def add_review(review, games_listbox,played_games_listbox ,played_games_dict):
    selected_game_info = games_listbox.get(tk.ACTIVE)
    if selected_game_info:
        match = re.search(r'Name:\s*(.*?)\s*¬', selected_game_info)
        if match:
            selected_game_name = match.group(1).strip()
        else:
            messagebox.showwarning('Invalid Format', 'Failed to extract game name.')
            return
        
        if selected_game_name in played_games_dict:
            # Delete existing review
            del played_games_dict[selected_game_name]
        
        # Add new review
        played_games_dict[selected_game_name] = f"Name: {selected_game_name} ¬ Review: {review}"

        played_games_listbox.delete(0, tk.END)  # Clear the listbox
        print(played_games_dict)
        for game_name, game_review in played_games_dict.items():
            played_games_listbox.insert(tk.END, game_review)

def remove_review(played_games_listbox, played_games_dict):
    selected_review = played_games_listbox.curselection()
    if selected_review:
        index = selected_review[0]
        item = played_games_listbox.get(index)
        
        # Delete from listbox
        played_games_listbox.delete(index)
        
        # Find corresponding key in dictionary and delete
        for key, value in played_games_dict.items():
            if value == item:
                del played_games_dict[key]
                break
        print(played_games_dict)

def add_favourite(played_games_listbox, played_games_dict, fav_games_listbox, fav_games_dict):
    selected_game_info = played_games_listbox.get(tk.ACTIVE)
    if selected_game_info:
        match = re.search(r'Name:\s*(.*?)\s*¬', selected_game_info)
        if match:
            selected_game_name = match.group(1).strip()
        else:
            messagebox.showwarning('Invalid Format', 'Failed to extract game name.')
            return
        
        if selected_game_name in fav_games_dict:
            messagebox.showinfo('Already Favorited', 'This game is already in your favorites!')
            return
        
        # Find the game in played_games_dict
        if selected_game_name in played_games_dict:
            # Add to fav_games_dict and update fav_games_listbox
            fav_games_dict[selected_game_name] = selected_game_name
            fav_games_listbox.insert(tk.END, fav_games_dict[selected_game_name])

        else:
            messagebox.showwarning('Game Not Found', 'Selected game not found in played games.')
    print(fav_games_dict)


def remove_favourite(fav_games_listbox, fav_games_dict):
    selected_game = fav_games_listbox.curselection()
    if selected_game:
        index = selected_game[0]
        item = fav_games_listbox.get(index)
        
        # Delete from listbox
        fav_games_listbox.delete(index)
        
        # Find corresponding key in dictionary and delete
        for key, value in fav_games_dict.items():
            if value == item:
                del fav_games_dict[key]
                break
        print(fav_games_dict)

def confirm(played_games_dict, fav_games_dict, df_all, dir_path):
    played_data = []
    review_numerical_value = {'Like': 1, 'Interested': 0.5, 'Neutral/Not Interested': -0.5, 'Dislike': -1}
    for gameName, gameReview in played_games_dict.items():
        review = gameReview.split(' ¬ ')[1]
        review = review_numerical_value[review.split(': ')[1]]
        game_id = df_all[df_all['title'] == gameName]['app_id'].values[0]
        played_data.append({'gameID': game_id, 'gameName': gameName, 'review': review})
    reviews_df = pd.DataFrame(played_data)
    reviews_df.to_csv(os.path.join(dir_path, "your_games.csv"), index=False)

    fav_data = []
    for gameName, gameInfo in fav_games_dict.items():
        game_id = df_all[df_all['title'] == gameName]['app_id'].values[0]
        fav_data.append({'gameID': game_id, 'gameName': gameName})
    fav_df = pd.DataFrame(fav_data)
    fav_df.to_csv(os.path.join(dir_path, "fav_games.csv"), index=False)
    messagebox.showinfo('CSV Saved', 'Played and favourite games saved')

def get_recommendations(dir_path):
    try:
        notebook_path = os.path.join(dir_path, "knn_model.ipynb")

        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': dir_path}})

        messagebox.showinfo('Notebook Executed', 'Recommendations generated successfully.')

    except Exception as e:
        messagebox.showerror('Error', f'Failed to run recommendations notebook: {str(e)}')
