import arcade

# Set up constants

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

RECT_WIDTH: int = 75
RECT_HEIGHT: int = 75


def on_draw(delta_time):
    arcade.start_render()

    arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y, RECT_WIDTH, RECT_HEIGHT,
                                 arcade.color.ALIZARIN_CRIMSON)

    on_draw.center_x += on_draw.delta_x * delta_time
    on_draw.center_y += on_draw.delta_y * delta_time

    # edge detection
    if on_draw.center_x < RECT_WIDTH // 2 \
            or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
        on_draw.delta_x *= -1
    if on_draw.center_y < RECT_HEIGHT // 2 \
            or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:
        on_draw.delta_y *= -1


on_draw.center_x: int = 100  # Initial x position
on_draw.center_y: int = 50  # Initial y position
on_draw.delta_x: int = 130  # Initial change in x
on_draw.delta_y: int = 130  # Initial change in y


def main() -> object:
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bouncing Rectangle")
    arcade.set_background_color(arcade.color.WHITE)

    arcade.schedule(on_draw, 1 / 240)

    arcade.run()


if __name__ == "__main__":
    main()
