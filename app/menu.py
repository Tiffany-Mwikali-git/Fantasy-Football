# app/menu.py

from app import actions

def show_main_menu():
    while True:
        print("\n===  Fantasy Football Manager ===")
        print("1. Manage Players")
        print("2. Manage Teams")
        print("3. Manage Matches")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manage_players()
        elif choice == "2":
            manage_teams()
        elif choice == "3":
            manage_matches()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def manage_players():
    while True:
        print("\n--- Manage Players ---")
        print("1. List Players")
        print("2. Add Player")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            actions.list_players()
        elif choice == "2":
            name = input("Enter player name: ")
            position = input("Enter player position: ")
            team_id = input("Enter team ID: ")
            try:
                actions.add_player(name, position, int(team_id))
            except ValueError:
                print("  Invalid team ID. Please enter a number.")
        elif choice == "0":
            break
        else:
            print("Invalid option.")


def manage_teams():
    while True:
        print("\n--- Manage Teams ---")
        print("1. List Teams")
        print("2. Add Team")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            actions.list_teams()
        elif choice == "2":
            name = input("Enter team name: ")
            league = input("Enter league name: ")
            actions.add_team(name, league)
        elif choice == "0":
            break
        else:
            print("Invalid option.")


def manage_matches():
    while True:
        print("\n--- Manage Matches ---")
        print("1. List Matches")
        print("2. Add Match")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            actions.list_matches()
        elif choice == "2":
            date = input("Enter match date (YYYY-MM-DD): ")
            home_team_name = input("Enter home team name: ")
            away_team_name = input("Enter away team name: ")
            score = input("Enter final score (optional, e.g. 2-1): ")

            try:
                actions.add_match(date, str(home_team_name), str(away_team_name), score or None)
            except ValueError:
                print("  Invalid team Name. Please enter name.")
        elif choice == "0":
            break
        else:
            print("Invalid option.")