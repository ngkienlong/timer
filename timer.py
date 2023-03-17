# import streamlit as st
# import time

# # Define a function to start and display the timer
# def start_timer(duration):
#     # Convert duration to seconds
#     duration_secs = duration * 1
#     # Start the timer
#     start_time = time.time()
#     end_time = start_time + duration_secs
#     # Loop until the timer ends
#     while time.time() < end_time:
#         remaining_time = int(end_time - time.time())
#         minutes = remaining_time // 60
#         seconds = remaining_time % 60
#         time_str = "{:02d}:{:02d}".format(minutes, seconds)
#         st.write(time_str)
#         time.sleep(1)
#     # Display the final message when the timer ends
#     st.write("Time's up!")

# # Define the Streamlit app
# st.title("Timer Web App")
# duration = st.selectbox("Select Duration", [15, 30, 45, 60, 120, 180, 300, 420, 600])
# if st.button("Start Timer"):
#     start_timer(duration)

# import streamlit as st
# import time

# # Define a function to start and display the timer
# def start_timer(duration):
#     # Convert duration to seconds
#     duration_secs = duration * 1
#     # Start the timer
#     start_time = time.time()
#     end_time = start_time + duration_secs
#     # Loop until the timer ends
#     while time.time() < end_time:
#         remaining_time = int(end_time - time.time())
#         minutes = remaining_time // 60
#         seconds = remaining_time % 60
#         time_str = "{:02d}:{:02d}".format(minutes, seconds)
#         st.write(time_str)
#         time.sleep(1)
#     # Display the final message when the timer ends
#     st.write("Time's up!")

# # Define the Streamlit app
# st.title("Timer Web App")
# duration = st.slider("Select Duration (in minutes)", min_value=1, max_value=60, step=1, value=5)
# if st.button("Start Timer"):
#     start_timer(duration)

# import streamlit as st
# import time

# # Define a function to start and display the timer
# def start_timer(duration):
#     # Convert duration to seconds
#     duration_secs = duration * 1
#     # Start the timer
#     start_time = time.time()
#     end_time = start_time + duration_secs
#     # Loop until the timer ends
#     while time.time() < end_time:
#         remaining_time = int(end_time - time.time())
#         progress = remaining_time / duration_secs
#         st.progress(progress)
#         time.sleep(1)
#     # Display the final message when the timer ends
#     st.write("Time's up!")

# # Define the Streamlit app
# st.title("Timer Web App")
# duration = st.slider("Select Duration (in minutes)", min_value=1, max_value=60, step=1, value=5)
# if st.button("Start Timer"):
#     start_timer(duration)

import streamlit as st
import time

# Define a function to start and display the timer
def start_timer(duration):
    # Convert duration to seconds
    duration_secs = duration 
    # Start the timer
    start_time = time.time()
    end_time = start_time + duration_secs
    # Display the progress bar
    spacer = st.empty()
    spacer.write('\n')
    my_bar = st.progress(0)
    # Loop until the timer ends
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        progress = remaining_time / duration_secs
        my_bar.progress(progress,"Thời gian thấm thoát thoi đưa, nó đi đi mãi có chờ đợi ai")
        time.sleep(0.1)
    # Display the final message when the timer ends
    st.write("Hết giờ!")

# Define the Streamlit app
st.title("Tic toc tic toc")
duration = st.slider("Bạn muốn đếm bao nhiêu thời gian (tính bằng giây)", min_value=0, max_value=600, step=15, value=5)
if st.button("Bắt đầu"):
    start_timer(duration)

# import streamlit as st
# import time
# from analog_clock_widget import AnalogClockWidget

# # Define a function to start and display the timer
# def start_timer(duration):
#     # Convert duration to seconds
#     duration_secs = duration * 60
#     # Start the timer
#     start_time = time.time()
#     end_time = start_time + duration_secs
#     # Display the analog clock
#     st.write("Remaining Time:")
#     clock_widget = AnalogClockWidget(size=200)
#     st.write(clock_widget, unsafe_allow_html=True)
#     # Loop until the timer ends
#     while time.time() < end_time:
#         remaining_time = int(end_time - time.time())
#         minutes = remaining_time // 60
#         seconds = remaining_time % 60
#         clock_widget.set_time(minutes, seconds)
#         time.sleep(1)
#     # Display the final message when the timer ends
#     st.write("Time's up!")

# # Define the Streamlit app
# st.title("Timer Web App")
# duration = st.slider("Select Duration (in minutes)", min_value=1, max_value=60, step=1, value=5)
# if st.button("Start Timer"):
#     start_timer(duration)

# import streamlit as st
# import time
# import tkinter as tk
# from PIL import Image, ImageTk

# # Define a function to start and display the timer
# def start_timer(duration):
#     # Convert duration to seconds
#     duration_secs = duration * 60
#     # Start the timer
#     start_time = time.time()
#     end_time = start_time + duration_secs
#     # Create a new window for the analog clock
#     clock_window = tk.Toplevel()
#     clock_window.geometry("300x300")
#     clock_window.title("Analog Clock")
#     # Load the clock image
#     clock_image = Image.open("clock.png")
#     clock_image = clock_image.resize((200, 200))
#     clock_photo = ImageTk.PhotoImage(clock_image)
#     # Create a label to display the clock image
#     clock_label = tk.Label(clock_window, image=clock_photo)
#     clock_label.image = clock_photo
#     clock_label.pack(pady=20)
#     # Loop until the timer ends
#     while time.time() < end_time:
#         remaining_time = int(end_time - time.time())
#         minutes = remaining_time // 60
#         seconds = remaining_time % 60
#         # Update the clock image
#         hour_angle = (30 * ((minutes % 12) + (seconds / 60))) % 360
#         minute_angle = (6 * seconds) % 360
#         clock_image = Image.open("clock.png")
#         clock_image = clock_image.resize((200, 200))
#         draw = ImageDraw.Draw(clock_image)
#         draw.line((100, 100, 100 + 60 * math.sin(math.radians(hour_angle)), 100 - 60 * math.cos(math.radians(hour_angle))), width=3, fill="black")
#         draw.line((100, 100, 100 + 80 * math.sin(math.radians(minute_angle)), 100 - 80 * math.cos(math.radians(minute_angle))), width=2, fill="black")
#         clock_photo = ImageTk.PhotoImage(clock_image)
#         clock_label.configure(image=clock_photo)
#         clock_label.image = clock_photo
#         clock_window.update()
#         time.sleep(1)
#     # Destroy the clock window when the timer ends
#     clock_window.destroy()
#     # Display the final message when the timer ends
#     st.write("Time's up!")

# # Define the Streamlit app
# st.title("Timer Web App")
# duration = st.slider("Select Duration (in minutes)", min_value=1, max_value=60, step=1, value=5)
# if st.button("Start Timer"):
#     start_timer(duration)

# import streamlit as st
# import pygame
# import time
# import math

# # Define a function to start and display the timer
# def start_timer(duration):
#     # Convert duration to seconds
#     duration_secs = duration * 1
#     # Initialize pygame
#     pygame.init()
#     # Set the size of the window and the caption
#     window_size = (300, 300)
#     screen = pygame.display.set_mode(window_size)
#     pygame.display.set_caption("Analog Clock")
#     # Load the clock image and scale it to fit the window
#     clock_image = pygame.image.load("clock.png")
#     clock_image = pygame.transform.scale(clock_image, window_size)
#     # Set the center of the clock image as the pivot point for rotation
#     pivot_point = (window_size[0]//2, window_size[1]//2)
#     # Start the timer
#     start_time = time.time()
#     end_time = start_time + duration_secs
#     # Loop until the timer ends
#     while time.time() < end_time:
#         remaining_time = int(end_time - time.time())
#         minutes = remaining_time // 60
#         seconds = remaining_time % 60
#         # Calculate the angles for the hour and minute hands
#         hour_angle = (30 * ((minutes % 12) + (seconds / 60))) % 360
#         minute_angle = (6 * seconds) % 360
#         # Rotate the clock image using the calculated angles
#         rotated_clock_image = pygame.transform.rotate(clock_image, -hour_angle)
#         rotated_minute_hand_image = pygame.transform.rotate(pygame.image.load("minute_hand.png"), -minute_angle)
#         # Display the clock image and the minute hand
#         screen.blit(rotated_clock_image, (0,0))
#         screen.blit(rotated_minute_hand_image, (0,0))
#         pygame.display.update()
#         # Wait for 1 second before updating the clock image again
#         pygame.time.wait(1000)
#     # Quit pygame when the timer ends
#     pygame.quit()
#     # Display the final message when the timer ends
#     st.write("Time's up!")

# # Define the Streamlit app
# st.title("Timer Web App")
# duration = st.slider("Select Duration (in minutes)", min_value=1, max_value=60, step=1, value=5)
# if st.button("Start Timer"):
#     start_timer(duration)

# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# import time

# # Define a function to start and display the timer
# def start_timer(duration):
#     # Convert duration to seconds
#     duration_secs = duration 
#     # Define the figure and axes for the analog clock
#     fig, ax = plt.subplots()
#     # Set the plot limits and remove the axis
#     ax.set_xlim(-1.2, 1.2)
#     ax.set_ylim(-1.2, 1.2)
#     ax.axis('off')
#     # Define the clock face
#     circle = plt.Circle((0, 0), 1, fill=False, linewidth=2, color='black')
#     ax.add_artist(circle)
#     # Define the clock hands
#     hour_hand = plt.Line2D([0, 0], [0, 0.5], linewidth=6, color='black')
#     minute_hand = plt.Line2D([0, 0], [0, 0.8], linewidth=3, color='black')
#     ax.add_artist(hour_hand)
#     ax.add_artist(minute_hand)
#     # Set the initial clock time to 0:00
#     hour_hand.set_data([0, 0], [0, 0.5])
#     minute_hand.set_data([0, 0], [0, 0.8])
#     # Display the analog clock
#     st.pyplot(fig)
#     # Start the timer
#     start_time = time.time()
#     end_time = start_time + duration_secs
#     # Loop until the timer ends
#     while time.time() < end_time:
#         remaining_time = end_time - time.time()
#         # Calculate the hour and minute hands based on the remaining time
#         hour_angle = ((remaining_time / 60 / 60) % 12) * np.pi / 6 - np.pi / 2
#         minute_angle = ((remaining_time / 60) % 60) * np.pi / 30 - np.pi / 2
#         hour_hand.set_data([0, 0.4 * np.cos(hour_angle)], [0, 0.4 * np.sin(hour_angle)])
#         minute_hand.set_data([0, 0.7 * np.cos(minute_angle)], [0, 0.7 * np.sin(minute_angle)])
#         # Update the analog clock in the Streamlit app
#         st.pyplot(fig)
#         # Wait for 1 second before updating the clock again
#         time.sleep(1)
#     # Display the final message when the timer ends
#     st.write("Time's up!")

# # Define the Streamlit app
# st.title("Timer Web App")
# duration = st.slider("Select Duration (in minutes)", min_value=1, max_value=60, step=1, value=5)
# if st.button("Start Timer"):
#     start_timer(duration)
