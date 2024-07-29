import tkinter as tk
import Button_commands as commands


def search_frame(root,games_dict, list_frame):
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text='Search by Name:')
    search_label.grid(row=0, column=0)

    search_entry = tk.Entry(search_frame, width=80, font=('Arial', 12))
    search_entry.grid(row=0, column=1)
    search_entry.bind('<Return>', lambda event: commands.update_search(search_frame, games_dict, list_frame))

    search_button = tk.Button(search_frame, text='Search', command=lambda: commands.update_search(search_frame, games_dict, list_frame), font=('Arial', 11))
    search_button.grid(row=0, column=2, padx=10)

    return search_frame

def game_list_frame(root,all_games_dict):
    games_frame = tk.Frame(root)
    games_frame.pack(pady=10)

    games_label = tk.Label(games_frame, text='Games:', font=('Arial', 14, 'bold'))
    games_label.grid(row=0, column=0)

    games_listbox = tk.Listbox(games_frame, width=100, height=10, font=('Arial', 11))
    games_listbox.grid(row=1, column=0, padx=20)

    scrollbar = tk.Scrollbar(games_frame, orient=tk.VERTICAL, command=games_listbox.yview)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)
    games_listbox.config(yscrollcommand=scrollbar.set)

    for game_info in all_games_dict.values():
        games_listbox.insert(tk.END, game_info)
    return games_frame


def played_games_frame(root, played_games_dict):
    played_games_frame = tk.Frame(root)
    played_games_frame.pack(pady=10)

    played_games_label = tk.Label(played_games_frame, text='Played Games:', font=('Arial', 14, 'bold'))
    played_games_label.grid(row=0, column=0)

    played_games_listbox = tk.Listbox(played_games_frame, width=100, height=5, font=('Arial', 11))
    played_games_listbox.grid(row=1, column=0, padx=20)

    scrollbar_played = tk.Scrollbar(played_games_frame, orient=tk.VERTICAL, command=played_games_listbox.yview)
    scrollbar_played.grid(row=1, column=1, sticky=tk.NS)
    played_games_listbox.config(yscrollcommand=scrollbar_played.set)

    for game_info in played_games_dict.values():
        played_games_listbox.insert(tk.END, game_info)
    return played_games_frame


def fav_games_frame(root, fav_games_dict):
    fav_games_frame = tk.Frame(root)
    fav_games_frame.pack(pady=10)

    fav_games_label = tk.Label(fav_games_frame, text='Favourite Games:', font=('Arial', 14, 'bold'))
    fav_games_label.grid(row=0, column=0)

    fav_games_listbox = tk.Listbox(fav_games_frame, width=100, height=5, font=('Arial', 11))
    fav_games_listbox.grid(row=1, column=0, padx=20)

    scrollbar_fav = tk.Scrollbar(fav_games_frame, orient=tk.VERTICAL, command=fav_games_listbox.yview)
    scrollbar_fav.grid(row=1, column=1, sticky=tk.NS)
    fav_games_listbox.config(yscrollcommand=scrollbar_fav.set)

    delete_fav_button = tk.Button(fav_games_frame, text='Delete', command=lambda: commands.remove_favourite(fav_games_listbox, fav_games_dict), font=('Arial', 11))
    delete_fav_button.grid(row=3, column=0, padx=10)

    for game_info in fav_games_dict.values():
        fav_games_listbox.insert(tk.END, game_info)
    return fav_games_frame

def check_review_frame(root, played_games_frame, played_games_dict, fav_games_frame, fav_games_dict):
    for widget in played_games_frame.winfo_children():
        if isinstance(widget,tk.Listbox):
            played_games_listbox = widget

    for widget in fav_games_frame.winfo_children():
        if isinstance(widget,tk.Listbox):
            fav_games_listbox = widget

    check_review_frame = tk.Frame(root)
    check_review_frame.pack(pady=5)

    delete_review_button = tk.Button(check_review_frame, text='Delete Review', command=lambda: commands.remove_review(played_games_listbox,played_games_dict), font=('Arial', 11))
    delete_review_button.grid(row=0, column=1, padx=10)

    fav_button = tk.Button(check_review_frame, text='Mark as Favourite', command=lambda: commands.add_favourite(played_games_listbox,played_games_dict,fav_games_listbox,fav_games_dict), font=('Arial', 11))
    fav_button.grid(row=0, column=2, padx=10)
    return check_review_frame

def rating_frame(root,games_frame,played_games_frame,played_games_dict):
    for widget in games_frame.winfo_children():
        if isinstance(widget,tk.Listbox):
            games_listbox = widget

    for widget in played_games_frame.winfo_children():
        if isinstance(widget,tk.Listbox):
            played_games_listbox = widget

    rating_frame = tk.Frame(root)
    rating_frame.pack(pady=5)

    rating_label = tk.Label(rating_frame, text='Add Your Review:', font=('Arial', 14, 'bold'))
    rating_label.grid(row=0, column=0, padx=10)

    like_button = tk.Button(rating_frame, text='Like', command=lambda: commands.add_review('Like',games_listbox,played_games_listbox, played_games_dict), font=('Arial', 11))
    like_button.grid(row=0, column=1, padx=10)

    interested_button = tk.Button(rating_frame, text='Interested', command=lambda: commands.add_review('Interested',games_listbox,played_games_listbox, played_games_dict), font=('Arial', 11))
    interested_button.grid(row=0, column=2, padx=10)

    neutral_button = tk.Button(rating_frame, text='Neutral/Not Interested', command=lambda: commands.add_review('Neutral/Not Interested',games_listbox,played_games_listbox, played_games_dict), font=('Arial', 11))
    neutral_button.grid(row=0, column=3, padx=10)

    dislike_button = tk.Button(rating_frame, text='Dislike', command=lambda: commands.add_review('Dislike',games_listbox,played_games_listbox, played_games_dict), font=('Arial', 11))
    dislike_button.grid(row=0, column=4, padx=10)
    return rating_frame

def rcm_frame(root,played_games_dict, fav_games_dict, dir_path, df_all):
    recommendations_frame = tk.Frame(root)
    recommendations_frame.pack(pady=5)

    confirm_button = tk.Button(recommendations_frame, text='Confirm', command=lambda: commands.confirm(played_games_dict, fav_games_dict, df_all, dir_path), font=('Arial', 12))
    confirm_button.grid(row=0, column=0, padx=10, pady=10)

    recommendations_button = tk.Button(recommendations_frame, text='Get Recommendations', command=lambda: commands.get_recommendations(dir_path), font=('Arial', 12))
    recommendations_button.grid(row=0, column=1, padx=10, pady=10)

    return recommendations_frame