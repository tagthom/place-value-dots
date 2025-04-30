# PlaceValueDotVisualizer-save-time.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.widgets as widgets
import random
import os
import math
import sys
from datetime import datetime

def draw_number(ax, number_str):
    ax.clear()
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 1)

    # Define the green rectangle (full background)
    ax.add_patch(
        patches.Rectangle(
            (0, 0), 4, 1, linewidth=2, edgecolor='green', facecolor='lightgreen'
        )
    )

    # Draw the divisions (for 4 place values)
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

    st.pyplot(fig)


def main():
    print("Welcome to the Place Value Dot Visualizer!")

    fig, ax = plt.subplots(figsize=(10, 4))
    plt.subplots_adjust(bottom=0.45)

    draw_number(ax, "0")

    axbox = plt.axes([0.1, 0.25, 0.3, 0.075])
    text_box = widgets.TextBox(axbox, 'Enter number: ', initial="")

    namebox_ax = plt.axes([0.5, 0.25, 0.3, 0.075])
    name_box = widgets.TextBox(namebox_ax, 'Filename: ', initial="my_image")

    reset_ax = plt.axes([0.1, 0.1, 0.1, 0.075])
    reset_button = widgets.Button(reset_ax, 'Reset')

    save_ax = plt.axes([0.25, 0.1, 0.1, 0.075])
    save_button = widgets.Button(save_ax, 'Save')

    exit_ax = plt.axes([0.4, 0.1, 0.1, 0.075])
    exit_button = widgets.Button(exit_ax, 'Exit')

    current_number = ["0"]

    def submit(text):
        if text.lower() == 'stop':
            print("Goodbye!")
            plt.close(fig)
            sys.exit()

        if not text.isdigit() or len(text) > 4:
            print("Invalid input. Please enter a numeral with 1 to 4 digits.")
            return

        current_number[0] = text
        draw_number(ax, text)

    def reset(event):
        text_box.set_val("")
        draw_number(ax, "0")

    def save(event):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = name_box.text.strip()
            if not filename:
                filename = "place_value_dots"
            full_filename = f"{filename}_{timestamp}.jpg"
            fig.savefig(full_filename, bbox_inches='tight', format='jpg')
            print(f"Saved current figure to {full_filename}")
        except Exception as e:
            print(f"Could not save the figure due to an error: {e}")

    def exit_program(event):
        print("Exiting program.")
        plt.close(fig)
        sys.exit()

    text_box.on_submit(submit)
    reset_button.on_clicked(reset)
    save_button.on_clicked(save)
    exit_button.on_clicked(exit_program)

    plt.show()

if __name__ == "__main__":
    main()

# Test cases to manually verify:
# Input: 7 (should show 7 dots neatly arranged in ones box)
# Input: 45 (should show 4 dots in tens box, 5 dots in ones box)
# Input: 306 (should show 3 dots in hundreds box, 6 dots in ones box)
# Input: 1203 (should show 1 dot in thousands box, 2 dots in hundreds box, 0 in tens, 3 dots in ones box)
# Input: stop (should exit cleanly)
# Additional test cases:
# Input: 0 (should show no dots)
# Input: 1000 (should show 1 dot in thousands box)
# Input: 9 (should show 9 dots in ones box)
