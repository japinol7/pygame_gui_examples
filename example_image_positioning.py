import pygame
import pygame_gui
import json
import tempfile
import os
from typing import Dict, Any

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_SIZE = (1200, 1000)  # Increased window size for better spacing
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Image Positioning Example - pygame_gui')


# Create a simple test image programmatically
def create_test_image(size: tuple, color: pygame.Color, shape: str = "circle") -> pygame.Surface:
    """Create a simple test image with the specified color and shape."""
    surface = pygame.Surface(size, pygame.SRCALPHA)
    surface.fill((0, 0, 0, 0))  # Transparent background

    if shape == "circle":
        pygame.draw.circle(surface, color, (size[0] // 2, size[1] // 2), min(size) // 2 - 2)
    elif shape == "square":
        pygame.draw.rect(surface, color, (2, 2, size[0] - 4, size[1] - 4))
    elif shape == "triangle":
        points = [(size[0] // 2, 2), (2, size[1] - 2), (size[0] - 2, size[1] - 2)]
        pygame.draw.polygon(surface, color, points)

    return surface


# Create test images directory if it doesn't exist
os.makedirs("temp_images", exist_ok=True)

# Create and save test images
test_images = {
    "background.png": create_test_image((64, 64), pygame.Color(100, 150, 255), "square"),
    "icon.png": create_test_image((32, 32), pygame.Color(255, 200, 100), "circle"),
    "decoration.png": create_test_image((24, 24), pygame.Color(255, 100, 150), "triangle"),
    "glow.png": create_test_image((48, 48), pygame.Color(255, 255, 100, 128), "circle"),
    "badge.png": create_test_image((20, 20), pygame.Color(255, 50, 50), "circle"),
}

for filename, surface in test_images.items():
    pygame.image.save(surface, f"temp_images/{filename}")


def create_theme_data() -> Dict[str, Any]:
    """Create comprehensive theme data showcasing different positioning scenarios."""
    return {
        "button": {
            "colours": {
                "normal_bg": "#4a90e2",
                "hovered_bg": "#357abd",
                "selected_bg": "#2e6da4",
                "disabled_bg": "#cccccc",
                "normal_text": "#ffffff",
                "hovered_text": "#ffffff",
                "selected_text": "#ffffff",
                "disabled_text": "#666666"
            },
            "font": {
                "name": "fira_code",
                "size": "14",
                "bold": "0",
                "italic": "0"
            }
        },

        # Single-image positioning examples
        "#corner_positioned": {
            "images": {
                "normal_image": {
                    "path": "temp_images/icon.png",
                    "position": [0.0, 0.0]  # Top-left corner
                },
                "hovered_image": {
                    "path": "temp_images/icon.png",
                    "position": [1.0, 0.0]  # Top-right corner
                },
                "selected_image": {
                    "path": "temp_images/icon.png",
                    "position": [0.0, 1.0]  # Bottom-left corner
                },
                "disabled_image": {
                    "path": "temp_images/icon.png",
                    "position": [1.0, 1.0]  # Bottom-right corner
                }
            }
        },

        "#center_positioned": {
            "images": {
                "normal_image": {
                    "path": "temp_images/background.png",
                    "position": [0.5, 0.5]  # Center (default)
                }
            }
        },

        "#custom_positioned": {
            "images": {
                "normal_image": {
                    "path": "temp_images/decoration.png",
                    "position": [0.2, 0.3]  # Custom position
                },
                "hovered_image": {
                    "path": "temp_images/decoration.png",
                    "position": [0.8, 0.7]  # Different custom position
                }
            }
        },

        # Multi-image positioning examples
        "#layered_images": {
            "images": {
                "normal_images": [
                    {
                        "id": "background",
                        "layer": 0,
                        "path": "temp_images/background.png",
                        "position": [0.5, 0.5]  # Center background
                    },
                    {
                        "id": "icon",
                        "layer": 1,
                        "path": "temp_images/icon.png",
                        "position": [0.3, 0.3]  # Icon in upper-left area
                    },
                    {
                        "id": "decoration",
                        "layer": 2,
                        "path": "temp_images/decoration.png",
                        "position": [0.7, 0.7]  # Decoration in lower-right area
                    }
                ],
                "hovered_images": [
                    {
                        "id": "background",
                        "layer": 0,
                        "path": "temp_images/background.png",
                        "position": [0.5, 0.5]  # Center background
                    },
                    {
                        "id": "glow",
                        "layer": 1,
                        "path": "temp_images/glow.png",
                        "position": [0.5, 0.5]  # Glow effect in center
                    },
                    {
                        "id": "icon",
                        "layer": 2,
                        "path": "temp_images/icon.png",
                        "position": [0.3, 0.3]  # Icon on top
                    }
                ],
                "selected_images": [
                    {
                        "id": "background",
                        "layer": 0,
                        "path": "temp_images/background.png",
                        "position": [0.5, 0.5]  # Center background
                    },
                    {
                        "id": "badge",
                        "layer": 1,
                        "path": "temp_images/badge.png",
                        "position": [0.9, 0.1]  # Badge in top-right corner
                    }
                ]
            }
        },

        "#corner_showcase": {
            "images": {
                "normal_images": [
                    {
                        "id": "tl",
                        "layer": 0,
                        "path": "temp_images/badge.png",
                        "position": [0.0, 0.0]  # Top-left
                    },
                    {
                        "id": "tr",
                        "layer": 1,
                        "path": "temp_images/badge.png",
                        "position": [1.0, 0.0]  # Top-right
                    },
                    {
                        "id": "bl",
                        "layer": 2,
                        "path": "temp_images/badge.png",
                        "position": [0.0, 1.0]  # Bottom-left
                    },
                    {
                        "id": "br",
                        "layer": 3,
                        "path": "temp_images/badge.png",
                        "position": [1.0, 1.0]  # Bottom-right
                    },
                    {
                        "id": "center",
                        "layer": 4,
                        "path": "temp_images/icon.png",
                        "position": [0.5, 0.5]  # Center
                    }
                ]
            }
        },

        # Checkbox examples
        "#checkbox_corner_positioned": {
            "images": {
                "normal_image": {
                    "path": "temp_images/icon.png",
                    "position": [0.0, 0.0]  # Top-left corner
                },
                "hovered_image": {
                    "path": "temp_images/icon.png",
                    "position": [1.0, 0.0]  # Top-right corner
                },
                "selected_image": {
                    "path": "temp_images/icon.png",
                    "position": [0.0, 1.0]  # Bottom-left corner
                },
                "disabled_image": {
                    "path": "temp_images/icon.png",
                    "position": [1.0, 1.0]  # Bottom-right corner
                }
            }
        },

        "#checkbox_layered": {
            "images": {
                "normal_images": [
                    {
                        "id": "background",
                        "layer": 0,
                        "path": "temp_images/background.png",
                        "position": [0.5, 0.5]  # Center background
                    },
                    {
                        "id": "icon",
                        "layer": 1,
                        "path": "temp_images/icon.png",
                        "position": [0.3, 0.3]  # Icon in upper-left area
                    }
                ],
                "selected_images": [
                    {
                        "id": "background",
                        "layer": 0,
                        "path": "temp_images/background.png",
                        "position": [0.5, 0.5]  # Center background
                    },
                    {
                        "id": "icon",
                        "layer": 1,
                        "path": "temp_images/icon.png",
                        "position": [0.3, 0.3]  # Icon in upper-left area
                    },
                    {
                        "id": "badge",
                        "layer": 2,
                        "path": "temp_images/badge.png",
                        "position": [0.9, 0.1]  # Badge in top-right corner when checked
                    }
                ]
            }
        },

        # Panel examples
        "#panel_corner_positioned": {
            "images": {
                "background_images": [
                    {
                        "id": "top_left",
                        "path": "temp_images/icon.png",
                        "position": [0.0, 0.0],  # Top-left corner
                        "layer": 0
                    },
                    {
                        "id": "top_right",
                        "path": "temp_images/icon.png",
                        "position": [1.0, 0.0],  # Top-right corner
                        "layer": 1
                    },
                    {
                        "id": "bottom_left",
                        "path": "temp_images/icon.png",
                        "position": [0.0, 1.0],  # Bottom-left corner
                        "layer": 2
                    },
                    {
                        "id": "bottom_right",
                        "path": "temp_images/icon.png",
                        "position": [1.0, 1.0],  # Bottom-right corner
                        "layer": 3
                    }
                ]
            }
        },

        "#panel_layered": {
            "images": {
                "background_images": [
                    {
                        "id": "background",
                        "path": "temp_images/icon.png",
                        "position": [0.5, 0.5],  # Center background
                        "layer": 0
                    },
                    {
                        "id": "overlay",
                        "path": "temp_images/icon.png",
                        "position": [0.1, 0.1],  # Top-left overlay
                        "layer": 1
                    }
                ]
            }
        }
    }


def create_info_text(font, text, color, pos):
    """Helper function to create info text."""
    text_surface = font.render(text, True, color)
    return text_surface, pos


def main():
    # Create theme file
    theme_data = create_theme_data()
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(theme_data, f, indent=2)
        theme_file = f.name

    try:
        # Create UI Manager with our theme
        manager = pygame_gui.UIManager(WINDOW_SIZE, theme_file)

        # Create buttons showcasing different positioning scenarios
        buttons = []

        # Row 1: Single-image positioning (better spaced)
        buttons.append({
            'button': pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(50, 60, 180, 90),  # Larger buttons
                text='Corner Pos',
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#corner_positioned', class_id='@image_button')
            ),
            'label': 'Single Image - Corner Positioning\n(hover/select to see \ndifferent corners)',
            'pos': (50, 160)  # Position for label
        })

        buttons.append({
            'button': pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(260, 60, 180, 90),  # Better spacing
                text='Center Pos',
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#center_positioned', class_id='@image_button')
            ),
            'label': 'Single Image - Center Positioned\n(default position: 0.5, 0.5)',
            'pos': (260, 160)
        })

        buttons.append({
            'button': pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(470, 60, 180, 90),  # Better spacing
                text='Custom Pos',
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#custom_positioned', class_id='@image_button')
            ),
            'label': 'Single Image - Custom Position\n(normal: 0.2,0.3 | hover: 0.8,0.7)',
            'pos': (470, 160)
        })

        # Row 2: Multi-image positioning (better spaced)
        buttons.append({
            'button': pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(50, 220, 180, 90),  # More space between rows
                text='Layered Images',
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#layered_images', class_id='@image_button')
            ),
            'label': 'Multi-Image - Layered Effects\n(background + icon + decoration)',
            'pos': (50, 320)
        })

        buttons.append({
            'button': pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(260, 220, 180, 90),  # Better spacing
                text='Corner Showcase',
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#corner_showcase', class_id='@image_button')
            ),
            'label': 'Multi-Image - All Corners\n(4 corner badges + center icon)',
            'pos': (260, 320)
        })

        # Row 4: Checkbox examples
        buttons.append({
            'button': pygame_gui.elements.UICheckBox(
                relative_rect=pygame.Rect(50, 500, 180, 90),
                text='Corner Positioned Checkbox',
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#checkbox_corner_positioned')
            ),
            'label': 'Checkbox - Corner Positioning\n(hover/select to see \ndifferent corners)',
            'pos': (50, 600)
        })

        buttons.append({
            'button': pygame_gui.elements.UICheckBox(
                relative_rect=pygame.Rect(260, 500, 180, 90),
                text='Layered Checkbox',
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#checkbox_layered')
            ),
            'label': 'Checkbox - Layered Images\n(check to see badge appear)',
            'pos': (260, 600)
        })

        # Row 5: Panel examples
        buttons.append({
            'button': pygame_gui.elements.UIPanel(
                relative_rect=pygame.Rect(50, 700, 180, 180),
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#panel_corner_positioned')
            ),
            'label': 'Panel - Corner Positioning\n(icons in each corner)',
            'pos': (50, 890)
        })

        buttons.append({
            'button': pygame_gui.elements.UIPanel(
                relative_rect=pygame.Rect(260, 700, 180, 180),
                manager=manager,
                object_id=pygame_gui.core.ObjectID(object_id='#panel_layered')
            ),
            'label': 'Panel - Layered Images\n(centered bg + top-left overlay)',
            'pos': (260, 890)
        })

        # Create info panel (repositioned and resized)
        info_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(680, 60, 480, 500),  # Moved to right side
            manager=manager
        )

        # Create info text
        info_text = pygame_gui.elements.UITextBox(
            html_text='''
            <b>Image Positioning Demo</b><br><br>

            <b>Position Format:</b><br>
            [x, y] where 0.0-1.0 represents relative position<br>
            • (0.0, 0.0) = Top-left corner<br>
            • (0.5, 0.5) = Center (default)<br>
            • (1.0, 1.0) = Bottom-right corner<br><br>

            <b>Features Demonstrated:</b><br>
            • Single-image positioning per state<br>
            • Multi-image layering with positions<br>
            • State-specific positioning<br>
            • Corner and custom positioning<br><br>

            <b>How to Interact:</b><br>
            • <b>Hover</b> over buttons to see hover states<br>
            • <b>Click</b> to select and see selected states<br>
            • Try different buttons for various effects<br><br>

            <b>Examples:</b><br>
            • <b>Corner Positioning:</b> Image moves to different corners based on state<br>
            • <b>Center Positioned:</b> Standard centered image<br>
            • <b>Custom Position:</b> Image slides between custom positions<br>
            • <b>Layered Images:</b> Multiple images with individual positions<br>
            • <b>Corner Showcase:</b> All four corners plus center
            ''',
            relative_rect=pygame.Rect(10, 10, 460, 480),
            manager=manager,
            container=info_panel
        )

        # Create font for additional labels
        font = pygame.font.Font(None, 24)
        small_font = pygame.font.Font(None, 18)

        clock = pygame.time.Clock()
        running = True

        print("Image Positioning Demo Started!")
        print("=" * 50)
        print("Hover over buttons to see different positioning effects")
        print("Click buttons to see selected state positioning")
        print("Close window to exit")

        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                manager.process_events(event)

            manager.update(time_delta)

            # Clear screen
            screen.fill((240, 240, 240))

            # Draw title
            title_surface = font.render("pygame_gui Image Positioning Demo", True, (50, 50, 50))
            screen.blit(title_surface, (50, 10))

            # Draw button labels
            for i, button_info in enumerate(buttons):
                label_pos = button_info['pos']

                # Split label into lines and render each
                lines = button_info['label'].split('\n')
                for j, line in enumerate(lines):
                    line_surface = small_font.render(line, True, (80, 80, 80))
                    screen.blit(line_surface, (label_pos[0], label_pos[1] + j * 18))

            manager.draw_ui(screen)
            pygame.display.flip()

    finally:
        # Cleanup
        pygame.quit()
        os.unlink(theme_file)

        # Remove temporary images
        for filename in test_images.keys():
            try:
                os.remove(f"temp_images/{filename}")
            except FileNotFoundError:
                pass

        try:
            os.rmdir("temp_images")
        except OSError:
            pass


if __name__ == "__main__":
    main()