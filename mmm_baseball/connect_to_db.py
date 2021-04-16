import sqlite3
from pathlib import Path

con = sqlite3.connect(Path.cwd() / "mmm_baseball/kaggle_datasets/database.sqlite")
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

"""
    Output:
        [
            ('all_star',), ('appearances',), ('manager_award',), ('player_award',), 
            ('manager_award_vote',), ('player_award_vote',), ('batting',), ('batting_postseason',), 
            ('player_college',), ('fielding',), ('fielding_outfield',), ('fielding_postseason',), 
            ('hall_of_fame',), ('home_game',), ('manager',), ('manager_half',), ('player',), ('park',), 
            ('pitching',), ('pitching_postseason',), ('salary',), ('college',), ('postseason',), ('team',), 
            ('team_franchise',), ('team_half',)
        ]
"""
print(cursor.fetchall())
