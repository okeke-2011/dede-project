from GamePlay import GamePlay

def game():
    green = [(1, 1), (4, 1), (0, 3)]
    red = [(3, 0), (3, 3), (1, 4)]
    gr = GamePlay(5, green, red)
    player = "X"

    print(gr)

    while True:
      # if player == "X":
      #   print("Player ❎ turn:\n")
      # elif player == "O":
      #   print("Player 🅾️ turn:\n")

      # player_response = input("Input your move (1 - 25): ")
      # if player_response == "x":
      #   break

      # pos = int(player_response)
      # if pos < 1 or pos > 25 :
      #   print("\nInvalid move! Select number from 1 - 25\n")
      #   continue

      # if gr.validate_move(player, pos):
      #   gr.play(player, pos)
      # else:
      #   print("\nINVALID MOVE!!!\n")
      #   if player == "X":
      #     print("❎ can only play in 🟩 or ⬜️ spots\n")
      #   else:
      #     print("🅾️ can only play in 🟥 or ⬜️ spots\n")
      #   continue

      # print(gr)

      # if gr.check_win() == "X":
      #   print("\nPlayer ❎ wins!!!\n")
      #   break
      # elif gr.check_win() == "O":
      #   print("\nPlayer 🅾️ wins!!!\n")
      #   break

      if player == "X":
        player = "O"
      elif player == "O":
        player = "X"

if __name__ == "__main__":
  game()