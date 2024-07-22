import os
from PIL import Image, ImageDraw, ImageFont
import string

def create_grid_image(photo_width, photo_height, num_columns, num_rows, output_filename, line_thickness=1, label_size=24):
    # Determine cell size
    cell_width = photo_width // num_columns
    cell_height = photo_height // num_rows
    
    # Calculate the size of the grid image including the labels
    margin_x = int(label_size * 1.1)  # Margin for the labels
    margin_y = int(label_size * 1.1)  # Margin for the labels
    grid_width = photo_width + margin_x
    grid_height = photo_height + margin_y
    
    # Create a new image with white background
    grid_image = Image.new('RGB', (grid_width, grid_height), 'white')
    # grid_image = Image.new('RGBA', (grid_width, grid_height), (255, 255, 255, 0))

    draw = ImageDraw.Draw(grid_image)
    
    # Define the font size and font
    try:
        font = ImageFont.truetype("Arial.ttf", label_size)
    except IOError:
        font = ImageFont.load_default()
        print("Could not load font. Using default font.")
    
    # Draw the vertical lines and label columns
    for i in range(num_columns + 1):
        x = margin_x + i * cell_width
        draw.line([(x, margin_y), (x, grid_height)], fill='black', width=line_thickness)
        if i <= num_columns:
            label = string.ascii_uppercase[i-1]
            text_width, text_height = draw.textbbox((0, 0), label, font=font)[2:4]
            text_x = x - cell_width // 2 - text_width // 2
            text_y = margin_y // 2 - text_height // 2
            print(f"Column label: {label}, Position: ({text_x}, {text_y})")
            draw.text((text_x, text_y), label, fill='black', font=font)
    
    # Draw the horizontal lines and label rows
    for j in range(num_rows + 1):
        y = margin_y + j * cell_height
        draw.line([(margin_x, y), (grid_width, y)], fill='black', width=line_thickness)
        if j <= num_rows:
            label = str(j)
            text_width, text_height = draw.textbbox((0, 0), label, font=font)[2:4]
            text_x = margin_x // 2 - text_width // 2
            text_y = y - cell_height // 2 - text_height // 2
            print(f"Row label: {label}, Position: ({text_x}, {text_y})")
            draw.text((text_x, text_y), label, fill='black', font=font)
    
    # draw.text((500, 500), "Kartoffel", fill='black', font=font)
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_filename)
    
    # Save the grid image
    grid_image.save(output_path)
    print("Grid overlay image saved as", output_path)

# Example usage
photo_width = 13039
photo_height = 4684
num_columns = 5
num_rows = 4
output_filename = 'grid_overlay.png'
label_size = 150
line_thickness = 10
create_grid_image(photo_width, photo_height, num_columns, num_rows, output_filename, line_thickness=line_thickness, label_size=label_size)
