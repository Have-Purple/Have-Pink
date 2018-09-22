import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    # Draws green "grass" or "snow" in lower third of screen.  The background sky color is created in main() arcade.set.background_color()
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snoman(x: object, y: object, snow_color: object, eyes_color: object) -> object:
    # Draw a snow person
    arcade.draw_circle_filled(x, 60 + y, 60, snow_color)
    arcade.draw_circle_filled(x, 140 + y, 50, snow_color)
    arcade.draw_circle_filled(x, 200 + y, 40, snow_color)
    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, eyes_color)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, eyes_color)

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)


def on_draw(delta_time):
    # Draw everything
    arcade.start_render()

    draw_grass()
    draw_snoman(on_draw.snow_man1_x, on_draw.snow_man1_y, snow_color, eyes_color)
    draw_snoman(on_draw.snow_man2_x, on_draw.snow_man2_y, snow_color, eyes_color)

    # Movement factors for snowman 1
    on_draw.snow_man1_x += 1
    on_draw.snow_man1_y += .15

# Snowman x and y initial values that are sent to draw_snoman function above)
on_draw.snow_man1_x = 150
on_draw.snow_man1_y = 140
on_draw.snow_man2_x = 450
on_draw.snow_man2_y = 180

# Snowman color
snow_color = arcade.color.ANTI_FLASH_WHITE
eyes_color = arcade.color.BLACK

def main() -> object:
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    arcade.schedule(on_draw, 1 / 200)
    arcade.run()


main()
