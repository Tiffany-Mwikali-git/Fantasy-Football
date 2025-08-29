from app.models.base import SessionLocal
from app.models import base, players, team, match
from app.models import Team, Player, Match  # Ensure models are imported so they are registered with Base

def get_session():
    return SessionLocal()


def add_team(name, league):
    session = get_session()
    new_team = team.Team(name=name, league=league)
    session.add(new_team)
    session.commit()
    print(f" Team '{name}' added.")


def list_teams():
    session = get_session()
    all_teams = session.query(Team).all()
    for team in all_teams:
        print(f"[{team.id}] {team.name} - {team.league}")


def add_player(name, position, team_id):
    session = get_session()
    new_player = players.Player(name=name, position=position, team_id=team_id)
    session.add(new_player)
    session.commit()
    print(f" Player '{name}' added.")


def list_players():
    session = get_session()
    all_players = session.query(players.Player).all()
    for p in all_players:
        print(f"[{p.id}] {p.name} - {p.position} (Team ID: {p.team_id})")


def add_match(date, home_team_name, away_team_name, score=None):
    session = get_session()
    new_match = match.Match(
        date=date,
        home_team_name=home_team_name,
        away_team_name=away_team_name,
        score=score
    )
    session.add(new_match)
    session.commit()
    print(" Match added.")


def list_matches():
    session = get_session()
    matches = session.query(match.Match).all()
    for m in matches:
        print(f"[{m.id}] {m.date} - {m.home_team.name} vs {m.away_team.name} | Score: {m.score or 'TBD'}")