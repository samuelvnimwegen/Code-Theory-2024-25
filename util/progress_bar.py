"""
This module contains a function to print a progress bar to the console.
"""


def print_progress_bar(iteration, total, bar_length=40):
    """
    Prints a progress bar to the console.

    :param iteration: Current iteration (index)
    :param total: Total iterations
    :param bar_length: The length of the progress bar in characters
    """
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(bar_length * iteration // total)
    text_bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rProgress |{text_bar}| {percent}% Complete')
    if iteration == total:
        print()  # New line on complete