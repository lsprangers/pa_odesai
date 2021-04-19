import sys
import sqlite3
sys.path.extend(['.', '../', '../../', './mmm_baseball/data/'])

from pathlib import Path, PurePath
# import pandas as pd

baseball_datasets_path = Path.cwd() / "mmm_baseball/data/kaggle_datasets"


# https://pwp.stevecassidy.net/python/pysqlite.html
# https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api
con = sqlite3.connect(baseball_datasets_path / "database.sqlite")
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
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


"""
baseball_datasets = [x for x in baseball_datasets_path.glob('**/*.csv') if x.is_file()]

df_dict = {
    PurePath(bball_csv): pd.read_csv(PurePath(bball_csv))
    for bball_csv in baseball_datasets
}

    Output:
            [11690 rows x 22 columns], PurePosixPath('.../cup_a_code/mmm_baseball/kaggle_datasets/park.csv'):     park_id                            park_name  ... state country
        0     ALB01                       Riverside Park  ...    NY      US
        1     ALT01                        Columbia Park  ...    PA      US
        2     ANA01             Angel Stadium of Anaheim  ...    CA      US
        3     ARL01                    Arlington Stadium  ...    TX      US
        4     ARL02        Rangers Ballpark in Arlington  ...    TX      US
        ..      ...                                  ...  ...   ...     ...
        245   WIL01                    Union Street Park  ...    DE      US
        246   WNY01     West New York Field Club Grounds  ...    NJ      US
        247   WOR01   Agricultural County Fair Grounds I  ...    MA      US
        248   WOR02  Agricultural County Fair Grounds II  ...    MA      US
        249   WOR03       Worcester Driving Park Grounds  ...    MA      US
        [250 rows x 6 columns], PurePosixPath('.../cup_a_code/mmm_baseball/kaggle_datasets/player_award_vote.csv'):                 award_id  year league_id  ... points_won  points_max  votes_first
        0               Cy Young  1956        ML  ...        1.0          16          1.0
        1               Cy Young  1956        ML  ...        4.0          16          4.0
        2               Cy Young  1956        ML  ...       10.0          16         10.0
        3               Cy Young  1956        ML  ...        1.0          16          1.0
        4               Cy Young  1957        ML  ...        1.0          16          1.0
                          ...   ...       ...  ...        ...         ...          ...
        6790  Rookie of the Year  2015        NL  ...       28.0         150          0.0
        6791  Rookie of the Year  2015        NL  ...       16.0         150          0.0
        6792  Rookie of the Year  2015        NL  ...        4.0         150          0.0
        6793  Rookie of the Year  2015        NL  ...        1.0         150          0.0
        6794  Rookie of the Year  2015        NL  ...        1.0         150          0.0
        [6795 rows x 7 columns], PurePosixPath('.../cup_a_code/mmm_baseball/kaggle_datasets/AllstarFull.csv'):        playerID  yearID  gameNum        gameID teamID lgID   GP  startingPos
        0     gomezle01    1933        0  ALS193307060    NYA   AL  1.0          1.0
        1     ferreri01    1933        0  ALS193307060    BOS   AL  1.0          2.0
        2     gehrilo01    1933        0  ALS193307060    NYA   AL  1.0          3.0
        3     gehrich01    1933        0  ALS193307060    DET   AL  1.0          4.0
        4     dykesji01    1933        0  ALS193307060    CHA   AL  1.0          5.0
                 ...     ...      ...           ...    ...  ...  ...          ...
        5064  boxbebr01    2015        0  NLS201507155    TBA   AL  NaN          NaN
        5065  gordoal01    2015        0  NLS201507156    KCA   AL  NaN          NaN
        5066  herreke01    2015        0  NLS201507157    KCA   AL  NaN          NaN
        5067  cabremi01    2015        0  NLS201507158    DET   AL  NaN          NaN
        5068   salech01    2015        0  NLS201507159    CHA   AL  NaN          NaN
        [5069 rows x 8 columns], PurePosixPath('.../cup_a_code/mmm_baseball/kaggle_datasets/fielding_outfield.csv'):        player_id  year  stint    glf   gcf   grf
        0      allisar01  1871      1    0.0  29.0   0.0
        1      ansonca01  1871      1    1.0   0.0   0.0
        2      armstbo01  1871      1    0.0  11.0   1.0
        3      barkeal01  1871      1    1.0   0.0   0.0
        4      barrofr01  1871      1   13.0   0.0   4.0
                  ...   ...    ...    ...   ...   ...
        12023  willite01  1955      1   93.0   0.0   0.0
        12024  wilsobi02  1955      1   23.0  57.0   4.0
        12025  woodlge01  1955      1   26.0   4.0  25.0
        12026  woodlge01  1955      2   64.0   0.0  16.0
        12027  zernigu01  1955      1  103.0   0.0   0.0
        [12028 rows x 6 columns]}
"""


