"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GRASS = arcade.color.BITTER_LEMON
SNOW = arcade.color.ICEBERG
SAND = arcade.color.SAND_DUNE

DAY = arcade.color.SKY_BLUE
NIGHT = arcade.color.MIDNIGHT_BLUE


def draw_ground(g_type: object) -> object:
    # This function draws the ground
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, g_type)


def draw_pine_tree(x, y):

    rect_x_offset = 30 / 2 + 48
    rect_y_offset = 80 / 2 + 48
    # draw trunk
    arcade.draw_rectangle_filled(rect_x_offset , rect_y_offset, 30, 80, arcade.color.BROWN)
    # draw three levels of triangles
    arcade.draw_triangle_filled(x + 50, y + 215, x + 150, y + 215, x + 100, y + 320, arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(x + 50, y + 255, x + 150, y + 255, x + 100, y + 360, arcade.color.FOREST_GREEN)
    arcade.draw_triangle_filled(x + 60, y + 295, x + 140, y + 295, x + 100, y + 400, arcade.color.FOREST_GREEN)


def main() -> object:
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(DAY)
    arcade.start_render()
    # Drawing code goes here
    # Draw a point at x, y for reference

    draw_ground(SAND)

    draw_pine_tree(50, 50)

    arcade.draw_point(50, 50, arcade.color.RED, 5)
    # Finish and run
    arcade.finish_render()
    arcade.run()


main()
