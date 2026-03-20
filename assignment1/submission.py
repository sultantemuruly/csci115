def tictactoe_result(moves: list[str]) -> str:
    winning_combinations = [
        ["A1", "A2", "A3"],
        ["B1", "B2", "B3"],
        ["C1", "C2", "C3"],
        ["A1", "B1", "C1"],
        ["A2", "B2", "C2"],
        ["A3", "B3", "C3"],
        ["A1", "B2", "C3"],
        ["A3", "B2", "C1"],
    ]

    o_moves = []
    x_moves = []
    i = 0

    while i < len(moves):
        current_move = moves[i]

        if i % 2 == 0:
            current_player_moves = o_moves
            winner_text = "O wins"
        else:
            current_player_moves = x_moves
            winner_text = "X wins"

        if len(current_player_moves) == 4:
            current_player_moves.pop(0)

        current_player_moves.append(current_move)

        for combination in winning_combinations:
            count = 0
            for cell in combination:
                if cell in current_player_moves:
                    count += 1
            if count == 3:
                return winner_text

        i += 1

    if len(moves) >= 30:
        return "Draw"
    return "Game not finished"
