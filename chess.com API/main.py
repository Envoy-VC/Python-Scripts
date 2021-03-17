from chessdotcom import get_leaderboards , get_player_stats , get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def get_leaderboard():
	data = get_leaderboards().json
	categories = data['leaderboards']
	daiy_leaderboards = categories['daily']
	for i in daiy_leaderboards:
		print(f" {i['rank']} | Username = {i['username']} | Score = {i['score']}")

def get_player_ratings(username):
	data = get_player_stats(username).json
	print(f"Ratings = {data['stats']['chess_blitz']['last']['rating']}")

def get_most_recent_game(username):
	data = get_player_game_archives(username).json
	url = data['archives'][-1]
	games = requests.get(url).json()
	last_game_played = games['games'][-1]
	printer.pprint(last_game_played)


get_leaderboard()
get_player_ratings('cschess')
get_most_recent_game('cschess')
