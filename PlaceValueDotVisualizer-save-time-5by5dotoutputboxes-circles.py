import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
from datetime import datetime

def draw_number(number_str):
    dot_radius = 0.015
    dot_diameter = 2 * dot_radius
    box_size = 7 * dot_diameter  # Each box is 7 dot diameters in height and width
    fig, ax = plt.subplots(figsize=(10, box_size * 0.75))

    ax.set_xlim(0, 4 * box_size)
    ax.set_ylim(0, box_size)

    ax.add_patch(
        patches.Rectangle(
            (0, 0), 4 * box_size, box_size, linewidth=2, edgecolor='green', facecolor='lightgreen'
        )
    )

    for i in range(1, 4):
        x = i * box_size
        ax.plot([x, x], [0, box_size], color='green', linewidth=2)

    ax.axis('off')

    labels = ['Thousands', 'Hundreds', 'Tens', 'Ones']
    for i in range(4):
        ax.text((i + 0.5) * box_size, box_size + dot_diameter * 0.3, labels[i], ha='center', va='bottom', fontsize=7)

    number_str = number_str.zfill(4)
    cols = 3
    rows = 3
    spacing = (box_size - (cols * dot_diameter)) / (cols + 1)
    padding = spacing  # equal spacing around all sides

    for idx, digit_char in enumerate(number_str):
        digit = int(digit_char)
        if digit == 0:
            continue

        start_x = idx * box_size + padding + dot_radius
        start_y = padding + dot_radius

        for i in range(digit):
            col_idx = i % cols
            row_idx = i // cols
            if row_idx >= rows:
                break
            x = start_x + col_idx * (dot_diameter + spacing)
            y = start_y + row_idx * (dot_diameter + spacing)
            circle = patches.Circle((x, y), dot_radius, color='black')
            ax.add_patch(circle)

    return fig

def main():
    st.title("Place Value Dot Visualizer")
    st.write("Enter a number (up to 4 digits) to visualize its place value with dots.")

    number_input = st.text_input("Enter number:", "")
    filename_input = st.text_input("Custom filename (optional):", "my_image")

    if st.button("Draw"):
        if number_input.isdigit() and len(number_input) <= 4:
            fig = draw_number(number_input)
            st.pyplot(fig)
        else:
            st.error("Invalid input. Please enter a numeral with 1 to 4 digits.")

    if st.button("Save Image"):
        if number_input.isdigit() and len(number_input) <= 4:
            fig = draw_number(number_input)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = filename_input.strip() or "place_value_dots"
            full_filename = f"{filename}_{timestamp}.jpg"
            fig.savefig(full_filename, bbox_inches='tight', format='jpg')
            st.success(f"Image saved as {full_filename}")
        else:
            st.error("Enter a valid number first to save.")

if __name__ == "__main__":
    main()
