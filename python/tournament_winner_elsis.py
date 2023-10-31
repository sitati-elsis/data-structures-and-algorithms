def tournamentWinner(competitions, results):
    # Write your code here.
    scores = {}
    while competitions and results:
        teams = competitions.pop()
        result = results.pop()
        if result == 0:
            if teams[1] in scores:
                scores[teams[1]] = scores[teams[1]] + 3
            else:
                scores[teams[1]] = 3
        else:
            if teams[0] in scores:
                scores[teams[0]] = scores[teams[0]] + 3
            else:
                scores[teams[0]] = 3

    team_names = list(scores.keys())
    team_scores = list(scores.values())
    return team_names[team_scores.index(max(team_scores))]
