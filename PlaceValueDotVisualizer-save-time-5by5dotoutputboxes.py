import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
from datetime import datetime

def draw_number(number_str):
    dot_radius = 0.015
    spacing = 2 * dot_radius  # Minimum spacing between dots
    box_size = 3 * spacing + 2 * dot_radius  # 3 dots + 2 gaps
    box_height = box_size * 1.1  # Slight padding for aesthetics
    fig, ax = plt.subplots(figsize=(10, box_height * 4))

    ax.set_xlim(0, 4 * box_size)
    ax.set_ylim(0, box_height)

    ax.add_patch(
        patches.Rectangle(
            (0, 0), 4 * box_size, box_height, linewidth=2, edgecolor='green', facecolor='lightgreen'
        )
    )

    for i in range(1, 4):
        x = i * box_size
        ax.plot([x, x], [0, box_height], color='green', linewidth=2)

    ax.axis('off')

    labels = ['Thousands', 'Hundreds', 'Tens', 'Ones']
    for i in range(4):
        ax.text((i + 0.5) * box_size, box_height + 0.005, labels[i], ha='center', va='bottom', fontsize=7)

    number_str = number_str.zfill(4)

    for idx, digit_char in enumerate(number_str):
        digit = int(digit_char)
        if digit == 0:
            continue

        cols = 3
        rows = 3
        start_x = idx * box_size + dot_radius + spacing / 2
        start_y = spacing / 2

        for i in range(digit):
            col_idx = i % cols
            row_idx = i // cols
            if row_idx >= rows:
                break  # Don't overflow
            x = start_x + col_idx * spacing
            y = start_y + row_idx * spacing
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
