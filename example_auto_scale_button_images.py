#!/usr/bin/env python3
"""
Example demonstrating the auto_scale_image functionality for UIButton.

This example shows how to use the new auto_scale_image theming parameter
to automatically scale button images to fit the button size while maintaining
aspect ratio.
"""

import pygame
import pygame_gui
import json
import os


def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("UIButton Auto-Scale Image Example")
    clock = pygame.time.Clock()

    # Create theme with auto_scale_image enabled
    theme_data = {
        "button": {
            "misc": {
                "auto_scale_images": "1"  # Enable auto-scaling
            },
            "images": {
                "normal_image": {
                    "path": "data/images/splat.png"
                }
            }
        },
        "#button_no_scale": {
            "misc": {
                "auto_scale_images": "0"  # Disable auto-scaling for comparison
            },
            "images": {
                "normal_image": {
                    "path": "data/images/splat.png"
                }
            }
        }
    }

    # Save theme to temporary file
    theme_file = "auto_scale_theme.json"
    with open(theme_file, "w") as f:
        json.dump(theme_data, f, indent=2)

    try:
        # Create UI manager with the theme
        manager = pygame_gui.UIManager((1000, 700), theme_file)

        # Create title
        title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(10, 10, 980, 40),
            text="UIButton Auto-Scale Image Demonstration",
            manager=manager
        )

        # Create subtitle for auto-scaled buttons
        subtitle1 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(10, 60, 480, 30),
            text="Auto-Scaled Images (maintains aspect ratio):",
            manager=manager
        )

        # Create subtitle for non-scaled buttons
        subtitle2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(510, 60, 480, 30),
            text="Original Images (no scaling):",
            manager=manager
        )

        # Create buttons with auto-scaling enabled
        auto_scale_buttons = []

        # Small square button
        small_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 100, 60, 60),
            text="Small",
            manager=manager
        )
        auto_scale_buttons.append(("Small (60x60)", small_button))

        # Medium square button
        medium_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(130, 100, 100, 100),
            text="Medium",
            manager=manager
        )
        auto_scale_buttons.append(("Medium (100x100)", medium_button))

        # Large square button
        large_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(250, 100, 150, 150),
            text="Large",
            manager=manager
        )
        auto_scale_buttons.append(("Large (150x150)", large_button))

        # Wide rectangular button
        wide_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 270, 200, 80),
            text="Wide Rectangle",
            manager=manager
        )
        auto_scale_buttons.append(("Wide (200x80)", wide_button))

        # Tall rectangular button
        tall_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(270, 270, 80, 150),
            text="Tall",
            manager=manager
        )
        auto_scale_buttons.append(("Tall (80x150)", tall_button))

        # Very small button
        tiny_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(370, 270, 30, 30),
            text="",
            manager=manager
        )
        auto_scale_buttons.append(("Tiny (30x30)", tiny_button))

        # Create buttons without auto-scaling for comparison
        no_scale_buttons = []

        # Small square button (no scaling)
        small_button_ns = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(550, 100, 60, 60),
            text="Small",
            manager=manager,
            object_id="#button_no_scale"
        )
        no_scale_buttons.append(("Small (60x60)", small_button_ns))

        # Medium square button (no scaling)
        medium_button_ns = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(630, 100, 100, 100),
            text="Medium",
            manager=manager,
            object_id="#button_no_scale"
        )
        no_scale_buttons.append(("Medium (100x100)", medium_button_ns))

        # Large square button (no scaling)
        large_button_ns = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(750, 100, 150, 150),
            text="Large",
            manager=manager,
            object_id="#button_no_scale"
        )
        no_scale_buttons.append(("Large (150x150)", large_button_ns))

        # Wide rectangular button (no scaling)
        wide_button_ns = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(550, 270, 200, 80),
            text="Wide Rectangle",
            manager=manager,
            object_id="#button_no_scale"
        )
        no_scale_buttons.append(("Wide (200x80)", wide_button_ns))

        # Tall rectangular button (no scaling)
        tall_button_ns = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(770, 270, 80, 150),
            text="Tall",
            manager=manager,
            object_id="#button_no_scale"
        )
        no_scale_buttons.append(("Tall (80x150)", tall_button_ns))

        # Very small button (no scaling)
        tiny_button_ns = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(870, 270, 30, 30),
            text="",
            manager=manager,
            object_id="#button_no_scale"
        )
        no_scale_buttons.append(("Tiny (30x30)", tiny_button_ns))

        # Create explanation text
        explanation = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect(50, 450, 900, 200),
            html_text="""
            <b>Auto-Scale Image Feature:</b><br><br>

            The left side shows buttons with <b>auto_scale_image: "1"</b> enabled. Notice how the images 
            scale to fit each button size while maintaining their original aspect ratio.<br><br>

            The right side shows buttons with <b>auto_scale_image: "0"</b> (default). The images appear 
            at their original size, which may not fit well with different button sizes.<br><br>

            <b>Key Benefits:</b><br>
            • Images automatically scale to fit button dimensions<br>
            • Aspect ratio is preserved to prevent distortion<br>
            • Works with all button states (normal, hovered, selected, disabled)<br>
            • Improves visual consistency across different button sizes<br><br>

            <b>Usage:</b> Add "auto_scale_image": "1" to the "misc" block in your button theme.
            """,
            manager=manager
        )

        print("Auto-Scale Image Example Running")
        print("================================")
        print("Left side: Auto-scaled images (maintains aspect ratio)")
        print("Right side: Original images (no scaling)")
        print("Press ESC to exit")

        # Main loop
        running = True
        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    print(f"Button pressed: {event.ui_element.text}")

                manager.process_events(event)

            manager.update(time_delta)

            # Clear screen
            screen.fill((40, 40, 40))

            # Draw UI
            manager.draw_ui(screen)

            # Draw labels for buttons
            font = pygame.font.Font(None, 20)

            # Labels for auto-scaled buttons
            for i, (label, button) in enumerate(auto_scale_buttons):
                text_surface = font.render(label, True, (200, 200, 200))
                screen.blit(text_surface, (button.rect.left, button.rect.bottom + 5))

            # Labels for non-scaled buttons
            for i, (label, button) in enumerate(no_scale_buttons):
                text_surface = font.render(label, True, (200, 200, 200))
                screen.blit(text_surface, (button.rect.left, button.rect.bottom + 5))

            pygame.display.flip()

    finally:
        # Cleanup
        if os.path.exists(theme_file):
            os.remove(theme_file)
        pygame.quit()


if __name__ == "__main__":
    main()