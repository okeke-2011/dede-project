class GamePlay():
  def __init__(self, n, green, red):
    self.n = n
    self.green = green
    self.red = red
    self.board = [["⬜️" for i in range(self.n)] for i in range(self.n)]
    
    for x, y in self.green:
      self.board[x][y] = "🟩"

    for x, y in self.red:
      self.board[x][y] = "🟥"

  def __str__(self):
    template = [[" 1", " 2", " 3", " 4", " 5"],
                [" 6", " 7", " 8", " 9", "10"],
                ["11", "12", "13", "14", "15"],
                ["16", "17", "18", "19", "20"],
                ["21", "22", "23", "24", "25"]]

    result = "\n"
    for i in range(len(self.board)):
      for tile in self.board[i]:
        result += f"{tile}   "

      result += "      "

      for num in template[i]:
        result += f"{num}   "

      result += "\n\n"

    return result

  def covert_num_to_pos(self, num):
    x = (num-1) // self.n
    y = (num-1) % self.n

    return x, y

  def play(self, player, pos):
    x, y = self.covert_num_to_pos(pos)

    if player == "X":
      self.board[x][y] = "❎"
    elif player == "O":
      self.board[x][y] = "🅾️"

  def validate_move(self, player, pos):
    x, y = self.covert_num_to_pos(pos)

    if self.board[x][y] == "⬜️":
      return True

    if player == "X" and self.board[x][y] == "🟩":
      return True

    if player == "O" and self.board[x][y] == "🟥":
      return True

    return False

  def check_win(self):
    for row in self.board:
      for i in range(self.n - 3 + 1):
        if row[i:i+3] == ["❎"] * 3:
          return "X"
        elif row[i:i+3] == ["🅾️"] * 3:
          return "O"

    for j in range(self.n):
      for i in range(self.n - 3 + 1):
        col = [self.board[i+x][j] for x in range(3)]
        if col == ["❎"] * 3:
          return "X"
        elif col == ["🅾️"] * 3:
          return "O"

    return "-"