import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
from datetime import datetime

def draw_number(number_str):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 1)

    ax.add_patch(
        patches.Rectangle(
            (0, 0), 4, 1, linewidth=2, edgecolor='green', facecolor='lightgreen'
        )
    )

    for i in range(1, 4):
        ax.plot([i, i], [0, 1], color='green', linewidth=2)

    ax.axis('off')

    labels = ['Thousands', 'Hundreds', 'Tens', 'Ones']
    for i in range(4):
        ax.text(i + 0.5, 1.05, labels[i], ha='center', va='bottom', fontsize=10)

    number_str = number_str.zfill(4)
    dot_radius = 0.03
    spacing = 0.1

    for idx, digit_char in enumerate(number_str):
        digit = int(digit_char)
        if digit == 0:
            continue

        cols = math.ceil(math.sqrt(digit))
        rows = math.ceil(digit / cols)

        start_x = idx + 0.1
        start_y = 0.1

        for i in range(digit):
            col_idx = i % cols
            row_idx = i // cols
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
