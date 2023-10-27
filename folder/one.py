import tkinter as tk
from a3_support import AbstractGrid, get_image

class FancyGameView(AbstractGrid):
    def __init__(self, master, dimensions, size, **kwargs):
        super().__init__(master, dimensions, size, **kwargs)
        self.image_cache = {}

    def display(self, maze, entities, player_position):
        self.clear()
        for x in range(self._rows):
            for y in range(self._columns):
                tile = maze[x][y]
                image = get_image(tile)
                self.create_image(x, y, image=image)
                
                if (x, y) in entities:
                    entity_image = get_image(entities[(x, y)])
                    self.create_image(x, y, image=entity_image)

        player_image = get_image('PLAYER')
        self.create_image(player_position[0], player_position[1], image=player_image)

class FancyStatsView(AbstractGrid):
    def __init__(self, master):
        super().__init__(master, (3, 3))

    def draw_stats(self, moves_remaining, strength, money):
        self.clear()

        self.create_text(1, 0, text="Player Stats", font=("Arial", 12, "bold"))
        self.create_text(0, 1, text="Moves Remaining")
        self.create_text(0, 2, text="Strength")
        self.create_text(0, 3, text="Money")
        self.create_text(1, 1, text=str(moves_remaining))
        self.create_text(1, 2, text=str(strength))
        self.create_text(1, 3, text=str(money))

class Shop(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.title_label = tk.Label(self, text="Shop", font=("Arial", 16, "bold"))
        self.title_label.pack()

    def create_buyable_item(self, item, amount, callback):
        frame = tk.Frame(self)
        frame.pack(fill=tk.X)

        label = tk.Label(frame, text=f"{item}: {amount}")
        label.pack(side=tk.LEFT)
        buy_button = tk.Button(frame, text="Buy", command=callback)
        buy_button.pack(side=tk.RIGHT)

class FancySokobanView(tk.Frame):
    def __init__(self, master, dimensions, size):
        super().__init__(master)

        # TODO: Create and pack the FancyGameView, FancyStatsView, and Shop instances

    def display_game(self, maze, entities, player_position):
        self.game_view.display(maze, entities, player_position)

    def display_stats(self, moves, strength, money):
        self.stats_view.draw_stats(moves, strength, money)

    def create_shop_items(self, shop_items, button_callback):
        for item, amount in shop_items.items():
            self.shop.create_buyable_item(item, amount, lambda item=item: button_callback(item))

class ExtraFancySokoban:
    def __init__(self, root, maze_file):
        self.model = None
        self.view = FancySokobanView(root, (10, 10), (40, 40))

    def redraw(self):
        maze, entities, player_position = self.model.get_game_state()
        self.view.display_game(maze, entities, player_position)

        moves, strength, money = self.model.get_player_stats()
        self.view.display_stats(moves, strength, money)

    def handle_keypress(self, event):
        # TODO: Implement this
        pass

def play_game(root, maze_file):
    controller = ExtraFancySokoban(root, maze_file)
    root.mainloop()

def main():
    root = tk.Tk()
    play_game(root, 'maze_files/maze1.txt')

if __name__ == '__main__':
    main()

