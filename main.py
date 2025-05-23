import arcade 
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Moving Sprite"

PLAYER_SPEED = 5
COIN_COUNT = 10
ENEMY_COUNT = 3

class CoinCollector(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.ocean_sound = arcade.load_sound("ocean_sounds.mp3")
        arcade.play_sound(self.ocean_sound)


        self.score = 0
        self.lives = 3
        self.player = None
        self.coins = None
        self.enemies = None
        self.change_x = 0
        self.change_y = 0

        self.score_text = arcade.Text(f"Score: {self.score}", 10, SCREEN_HEIGHT-30, arcade.color.BLACK, 20)
        self.lives_text = arcade.Text(f"Lives: {self.lives}", 10, SCREEN_HEIGHT-60, arcade.color.BLACK, 20)
        
        self.coin_sound = arcade.load_sound("coin_sound.mp3")
        
        self.player = arcade.Sprite("moana.png", 0.2)
        self.background = arcade.Sprite("ocean_background.png", 1)

        

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()


        
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2

        
        self.background.center_x = SCREEN_WIDTH // 2
        self.background.center_y = SCREEN_HEIGHT // 2

        self.player_list.append(self.player)
        self.background_list.append(self.background)


        # load the coins
        for _ in range(COIN_COUNT):
            coin = arcade.Sprite("heihei.png", 0.1)
            coin.center_x = random.randint(20, SCREEN_WIDTH-20)
            coin.center_y = random.randint(20, SCREEN_HEIGHT-20)
            self.coin_list.append(coin)

        #load the enemies
        for _ in range(ENEMY_COUNT):
            enemy = arcade.Sprite("kakamora.png", 0.1)
            enemy.center_x = SCREEN_WIDTH - 30
            enemy.center_y = random.randint(20, SCREEN_HEIGHT-20)
            self.enemy_list.append(enemy)

    def on_draw(self):
        self.clear()
        self.background_list.draw()
        self.score_text.draw()
        self.lives_text.draw()
        self.coin_list.draw()
        self.enemy_list.draw()
        self.player_list.draw()



    def on_update(self, delta_time):

        self.score_text.text = f"Score: {self.score}"
        self.lives_text.text = f"Lives: {self.lives}"


        coins_hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)     

    
        enemies_hit = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        for enemy in enemies_hit:
            self.lives -= 1


        self.player.center_x += self.change_x
        self.player.center_y += self.change_y


    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.change_x = PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.change_x = -PLAYER_SPEED
        elif key == arcade.key.UP:
            self.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.change_y = -PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.change_y = 0

if __name__ == "__main__":
    game = CoinCollector()
    arcade.run()