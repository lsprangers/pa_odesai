import sqlite3
from pathlib import Path


class KaggleBaseballDatabaseConnector:
    def __init__(self, db_sqlite_path=(Path.cwd() / "mmm_baseball/data/kaggle_datasets/database.sqlite")):
        self.con = sqlite3.connect(db_sqlite_path)
        self.all_tables_statement = "SELECT name FROM sqlite_master WHERE type='table';"

    def execute_and_print_statement_output(self, statement):
        """print out results of statement

        Args:
            statement (str): sql statement to pass to table
        """
        cursor = self.con.cursor()
        cursor.execute(statement)
        print(cursor.fetchall())

    def print_all_tables(self):
        """deterministic function

        Returns:
            [
                ('all_star',), ('appearances',), ('manager_award',), ('player_award',),
                ('manager_award_vote',), ('player_award_vote',), ('batting',), ('batting_postseason',),
                ('player_college',), ('fielding',), ('fielding_outfield',), ('fielding_postseason',),
                ('hall_of_fame',), ('home_game',), ('manager',), ('manager_half',), ('player',), ('park',),
                ('pitching',), ('pitching_postseason',), ('salary',), ('college',), ('postseason',), ('team',),
                ('team_franchise',), ('team_half',)
            ]
        """
        self.execute_and_print_statement_output(self.all_tables_statement)


if __name__ == '__main__':
    tester = KaggleBaseballDatabaseConnector()
    tester.print_all_tables()
