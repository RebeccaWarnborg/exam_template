class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        """Kollar om spelaren kan flytta sig i en viss riktning."""
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy

    # Om en position innehåller en vägg, returneras False
        if grid.get(new_x, new_y) == grid.wall:
            return False
    
        return True  # Annars returneras True   



