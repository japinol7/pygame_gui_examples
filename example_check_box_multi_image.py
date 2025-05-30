#!/usr/bin/env python3

import pygame
import pygame_gui
import tempfile
import json
import os


def create_test_images():
    """Create test images for the demo."""
    # Create different colored squares for different layers/states
    images = {}

    # Background images (larger, semi-transparent)
    bg_normal = pygame.Surface((24, 24), pygame.SRCALPHA)
    bg_normal.fill((100, 100, 100, 180))  # Gray background
    images['bg_normal'] = bg_normal

    bg_hovered = pygame.Surface((24, 24), pygame.SRCALPHA)
    bg_hovered.fill((120, 150, 200, 180))  # Blue background
    images['bg_hovered'] = bg_hovered

    bg_selected = pygame.Surface((24, 24), pygame.SRCALPHA)
    bg_selected.fill((100, 200, 100, 180))  # Green background
    images['bg_selected'] = bg_selected

    bg_disabled = pygame.Surface((24, 24), pygame.SRCALPHA)
    bg_disabled.fill((80, 80, 80, 180))  # Dark gray background
    images['bg_disabled'] = bg_disabled

    # Border images (medium size)
    border_normal = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.rect(border_normal, (60, 60, 60), (0, 0, 20, 20), 2)
    images['border_normal'] = border_normal

    border_hovered = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.rect(border_hovered, (80, 120, 160), (0, 0, 20, 20), 2)
    images['border_hovered'] = border_hovered

    border_selected = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.rect(border_selected, (60, 160, 60), (0, 0, 20, 20), 2)
    images['border_selected'] = border_selected

    border_disabled = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.rect(border_disabled, (40, 40, 40), (0, 0, 20, 20), 2)
    images['border_disabled'] = border_disabled

    # Icon/symbol images (smaller, centered)
    # Checkmark for selected state
    checkmark = pygame.Surface((16, 16), pygame.SRCALPHA)
    pygame.draw.lines(checkmark, (255, 255, 255), False, [(3, 8), (6, 11), (13, 4)], 3)
    images['checkmark'] = checkmark

    # Hover highlight
    highlight = pygame.Surface((18, 18), pygame.SRCALPHA)
    pygame.draw.circle(highlight, (255, 255, 255, 100), (9, 9), 8)
    images['highlight'] = highlight

    # Disabled overlay
    disabled_overlay = pygame.Surface((22, 22), pygame.SRCALPHA)
    pygame.draw.line(disabled_overlay, (255, 0, 0, 150), (2, 2), (20, 20), 2)
    pygame.draw.line(disabled_overlay, (255, 0, 0, 150), (20, 2), (2, 20), 2)
    images['disabled_overlay'] = disabled_overlay

    return images


def save_test_images(images, temp_dir):
    """Save test images to temporary files and return paths."""
    image_paths = {}
    for name, surface in images.items():
        path = os.path.join(temp_dir, f"{name}.png")
        pygame.image.save(surface, path)
        image_paths[name] = path
    return image_paths


def create_multi_image_checkbox_theme(image_paths):
    """Create a theme with multi-image support for checkboxes using real image paths."""
    return {
        "check_box": {
            "images": {
                "normal_images": [
                    {"id": "background", "path": image_paths['bg_normal'], "layer": 0},
                    {"id": "border", "path": image_paths['border_normal'], "layer": 1}
                ],
                "hovered_images": [
                    {"id": "background", "path": image_paths['bg_hovered'], "layer": 0},
                    {"id": "border", "path": image_paths['border_hovered'], "layer": 1},
                    {"id": "highlight", "path": image_paths['highlight'], "layer": 2}
                ],
                "selected_images": [
                    {"id": "background", "path": image_paths['bg_selected'], "layer": 0},
                    {"id": "border", "path": image_paths['border_selected'], "layer": 1},
                    {"id": "checkmark", "path": image_paths['checkmark'], "layer": 2}
                ],
                "disabled_images": [
                    {"id": "background", "path": image_paths['bg_disabled'], "layer": 0},
                    {"id": "border", "path": image_paths['border_disabled'], "layer": 1},
                    {"id": "disabled_overlay", "path": image_paths['disabled_overlay'], "layer": 2}
                ]
            },
            "misc": {
                "text_offset": 10
            }
        }
    }


def create_single_image_checkbox_theme(image_paths):
    """Create a theme with single-image support for checkboxes."""
    return {
        "check_box": {
            "images": {
                "normal_image": {"path": image_paths['bg_normal']},
                "hovered_image": {"path": image_paths['bg_hovered']},
                "selected_image": {"path": image_paths['bg_selected']},
                "disabled_image": {"path": image_paths['bg_disabled']}
            },
            "misc": {
                "text_offset": 10
            }
        }
    }


def main():
    pygame.init()

    # Set up the display
    window_surface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Multi-Image Checkbox Demo - Enhanced')

    # Create temporary directory for images
    temp_dir = tempfile.mkdtemp()

    try:
        # Create and save test images
        test_images = create_test_images()
        image_paths = save_test_images(test_images, temp_dir)

        # Create theme files
        multi_theme_data = create_multi_image_checkbox_theme(image_paths)
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(multi_theme_data, f)
            multi_theme_file = f.name

        single_theme_data = create_single_image_checkbox_theme(image_paths)
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(single_theme_data, f)
            single_theme_file = f.name

        # Create UI manager with multi-image theme
        manager = pygame_gui.UIManager((800, 600), multi_theme_file)

        # Create multiple checkboxes to demonstrate different states
        checkbox1 = pygame_gui.elements.UICheckBox(
            relative_rect=pygame.Rect(50, 50, 30, 30),
            text="Normal Multi-Image Checkbox",
            manager=manager
        )

        checkbox2 = pygame_gui.elements.UICheckBox(
            relative_rect=pygame.Rect(50, 100, 30, 30),
            text="Pre-checked Checkbox",
            manager=manager,
            initial_state=True
        )

        checkbox3 = pygame_gui.elements.UICheckBox(
            relative_rect=pygame.Rect(50, 150, 30, 30),
            text="Disabled Checkbox",
            manager=manager
        )
        checkbox3.disable()

        # Print initial state information
        print("=== Multi-Image Checkbox Demo - Enhanced ===")
        print(f"Checkbox 1 - Multi-image mode: {checkbox1.is_multi_image_mode()}")
        print(f"Checkbox 1 - Image count: {checkbox1.get_image_count()}")
        print(f"Checkbox 1 - Current images: {len(checkbox1.get_current_images())}")
        print("Images by state:")
        for state in ["normal", "hovered", "selected", "disabled"]:
            images = checkbox1.get_images_by_state(state)
            print(f"  {state}: {len(images)} images")

        # Create control buttons
        switch_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 250, 200, 40),
            text='Switch Theme Mode',
            manager=manager
        )

        toggle_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 300, 200, 40),
            text='Toggle Checkbox 1',
            manager=manager
        )

        disable_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 350, 200, 40),
            text='Toggle Disable Checkbox 1',
            manager=manager
        )

        indeterminate_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 400, 200, 40),
            text='Set Indeterminate',
            manager=manager
        )

        # Create info labels
        info_label = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect(300, 50, 450, 400),
            html_text="Multi-Image Checkbox Features:\n\n"
                 "• Normal state: Background + Border (2 layers)\n"
                 "• Hovered state: Background + Border + Highlight (3 layers)\n"
                 "• Selected state: Background + Border + Checkmark (3 layers)\n"
                 "• Disabled state: Background + Border + X overlay (3 layers)\n\n"
                 "Hover over checkboxes to see layered effects!\n"
                 "Click checkboxes to toggle their state.\n"
                 "Use buttons below to test different features.",
            manager=manager
        )


        status_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(300, 470, 450, 100),
            text="Status: Multi-image mode active",
            manager=manager
        )

        clock = pygame.time.Clock()
        is_running = True
        using_multi_theme = True

        print("==================================================")
        print("ENHANCED MULTI-IMAGE CHECKBOX DEMONSTRATION")
        print("==================================================")
        print("• Hover over checkboxes to see layered visual effects")
        print("• Click checkboxes directly to toggle their state")
        print("• Use control buttons to test different features")
        print("• Switch between multi-image and single-image themes")
        print("• Press ESC to exit")
        print("==================================================")

        while is_running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        is_running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == switch_button:
                        # Switch between themes
                        if using_multi_theme:
                            manager.ui_theme.load_theme(single_theme_file)
                            using_multi_theme = False
                            theme_status = "Single-image mode active"
                            print("=== Switched to Single-Image Theme ===")
                        else:
                            manager.ui_theme.load_theme(multi_theme_file)
                            using_multi_theme = True
                            theme_status = "Multi-image mode active"
                            print("=== Switched to Multi-Image Theme ===")

                        status_label.set_text(f"Status: {theme_status}")

                        # Force rebuild to apply new theme
                        checkbox1.rebuild_from_changed_theme_data()
                        checkbox2.rebuild_from_changed_theme_data()
                        checkbox3.rebuild_from_changed_theme_data()
                        switch_button.rebuild_from_changed_theme_data()
                        toggle_button.rebuild_from_changed_theme_data()
                        disable_button.rebuild_from_changed_theme_data()
                        indeterminate_button.rebuild_from_changed_theme_data()
                        info_label.rebuild_from_changed_theme_data()
                        status_label.rebuild_from_changed_theme_data()

                        # Print new state
                        print(f"Multi-image mode: {checkbox1.is_multi_image_mode()}")
                        print(f"Image count: {checkbox1.get_image_count()}")
                        print(f"Current images: {len(checkbox1.get_current_images())}")

                    elif event.ui_element == toggle_button:
                        # Toggle checkbox state
                        current_state = checkbox1.get_state()
                        if current_state == "indeterminate":
                            checkbox1.set_state(False)
                        else:
                            checkbox1.set_state(not checkbox1.is_checked)

                        new_state = checkbox1.get_state()
                        print(f"Checkbox 1 state: {new_state}")
                        print(f"Current images: {len(checkbox1.get_current_images())}")
                        status_label.set_text(f"Status: Checkbox 1 is {new_state}")

                    elif event.ui_element == disable_button:
                        # Toggle enabled/disabled state
                        if checkbox1.is_enabled:
                            checkbox1.disable()
                            print("Checkbox 1 disabled")
                            status_label.set_text("Status: Checkbox 1 disabled")
                        else:
                            checkbox1.enable()
                            print("Checkbox 1 enabled")
                            status_label.set_text("Status: Checkbox 1 enabled")
                        print(f"Current images: {len(checkbox1.get_current_images())}")

                    elif event.ui_element == indeterminate_button:
                        # Set indeterminate state
                        checkbox1.set_indeterminate(True)
                        print("Checkbox 1 set to indeterminate")
                        print(f"Current images: {len(checkbox1.get_current_images())}")
                        status_label.set_text("Status: Checkbox 1 is indeterminate")

                if event.type == pygame_gui.UI_CHECK_BOX_CHECKED:
                    print(f"Checkbox checked: {event.ui_element}")
                    if event.ui_element == checkbox1:
                        status_label.set_text("Status: Checkbox 1 checked")
                    elif event.ui_element == checkbox2:
                        status_label.set_text("Status: Checkbox 2 checked")

                if event.type == pygame_gui.UI_CHECK_BOX_UNCHECKED:
                    print(f"Checkbox unchecked: {event.ui_element}")
                    if event.ui_element == checkbox1:
                        status_label.set_text("Status: Checkbox 1 unchecked")
                    elif event.ui_element == checkbox2:
                        status_label.set_text("Status: Checkbox 2 unchecked")

                manager.process_events(event)

            manager.update(time_delta)

            # Draw background
            window_surface.fill((40, 40, 40))

            # Draw UI
            manager.draw_ui(window_surface)

            pygame.display.update()

    finally:
        # Clean up temporary files
        try:
            os.unlink(multi_theme_file)
            os.unlink(single_theme_file)
            # Clean up image files
            for path in image_paths.values():
                try:
                    os.unlink(path)
                except:
                    pass
            os.rmdir(temp_dir)
        except:
            pass

    pygame.quit()


if __name__ == '__main__':
    main()
