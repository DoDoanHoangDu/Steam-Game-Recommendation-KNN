import pandas as pd

# Function to load CSV file and handle errors
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print('Notification', f'File {file_path} not found.')
        return None
    

def load_data(file_path, type):
    df = load_csv(file_path)
    games_dict = {}
    if type == "all":
        if df is None:
            exit()
        for idx, row in df.iterrows():
            game_name = row['title']
            game_info = f"Rank: {row['sort_rank']} ¬ Name: {row['title']} ¬ Date: {row['date_release']} ¬ Rating: {row['positive_ratio']}"
            games_dict[game_name] = game_info

    elif type == "played":
        if df is None:
            df = pd.DataFrame(columns=['gameID', 'gameName', 'review'])
        for idx, row in df.iterrows():
            game_name = row['gameName']
            review_dict ={1: "Like", 0.5: "Interested", -0.5:"Neutral/Not Interested", -1: "Dislike"}
            game_info = f"Name: {row['gameName']} ¬ Review: {review_dict[row['review']]}"
            games_dict[game_name] = game_info

    elif type == "fav":
        if df is None:
            df = pd.DataFrame(columns=['gameID', 'gameName'])
        for idx, row in df.iterrows():
            game_name = row['gameName']
            games_dict[game_name] = game_name
    return df, games_dict