import argparse
import sys
from app import actions
from app.menu import show_main_menu


def parse_cli_args():
    parser = argparse.ArgumentParser(
        description=" Fantasy Football CLI - Manage Teams, Players, and Matches"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # TEAM COMMANDS
    team_parser = subparsers.add_parser("add-team", help="Add a new team")
    team_parser.add_argument("name", type=str, help="Team name")
    team_parser.add_argument("league", type=str, help="League name")

    subparsers.add_parser("list-teams", help="List all teams")

    # PLAYER COMMANDS
    player_parser = subparsers.add_parser("add-player", help="Add a new player")
    player_parser.add_argument("name", type=str, help="Player name")
    player_parser.add_argument("position", type=str, help="Player position")
    player_parser.add_argument("team_id", type=int, help="Team ID")

    subparsers.add_parser("list-players", help="List all players")

    # MATCH COMMANDS
    match_parser = subparsers.add_parser("add-match", help="Record a new match")
    match_parser.add_argument("date", type=str, help="Match date (YYYY-MM-DD)")
    match_parser.add_argument("home_team_name", type=str, help="Home team Name")
    match_parser.add_argument("away_team_name", type=str, help="Away team Name")
    match_parser.add_argument("--score", type=str, default=None, help="Final score (e.g. 2-1)")

    subparsers.add_parser("list-matches", help="List all matches")

    return parser.parse_args()


def start():
    if len(sys.argv) == 1:
        # No command-line args → launch interactive menu
        show_main_menu()
    else:
        args = parse_cli_args()

        if args.command == "add-team":
            actions.add_team(args.name, args.league)
        elif args.command == "list-teams":
            actions.list_teams()
        elif args.command == "add-player":
            actions.add_player(args.name, args.position, args.team_id)
        elif args.command == "list-players":
            actions.list_players()
        elif args.command == "add-match":
            actions.add_match(args.date, args.home_team_name, args.away_team_name, args.score)
        elif args.command == "list-matches":
            actions.list_matches()


if __name__ == "__main__":
    start()