class Square:

  def __init__(self,row,col,piece=None, land = 0):
    self.row = row
    self.col = col
    self.piece = piece
    self.land = land
  def __eq__(self,other):
    return self.row==other.row and self.col==other.col

  def has_piece(self):
    return self.piece != None

  def isempty_or_enemy(self, color):
    return not self.has_team_piece(color)
  def isempty(self):
    return not self.has_piece()
  def has_enemy_piece(self,color):
    return self.has_piece() and self.piece.color!=color
  def has_team_piece(self,color):
    return self.has_piece() and self.piece.color==color