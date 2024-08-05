---
layout: post
title: How a Summer Camp Sparked My Curiosity About the RP2040 and How It Can Spark Yours Too!
id: 2024-07-31-how-a-summer-camp-sparked-my-curiosity-about-the-rp2040-and-how-it-can-spark-yours-too.md
categories:
  - documentation
  - creative process
  - hardware
image: https://live.staticflickr.com/65535/53894228919_96a13c8a65_z.jpg
share: "true"
comments: "true"
filename: Blog/_posts/2024-07-31-how-a-summer-camp-sparked-my-curiosity-about-the-rp2040-and-how-it-can-spark-yours-too.md
tags:
  - homemade2024
  - rp2040
  - python
date: 2024-07-31
author: lina
---


I found myself immersed in my own tinkering at a shared table during a vibrant summer camp. It was then that Tormod approached me with an intriguing piece of hardware: the RP2040 development board.

The RP2040-GEEK Development Board sits intriguingly between the well-known Raspberry Pi and Arduino platforms. While the Raspberry Pi offers a full-fledged computing experience with its operating system and Arduino provides a straightforward, microcontroller-centric approach, the RP2040 seems to blend elements of both worlds.

The key lies in its versatility and convenience. For projects requiring a simple user interface without the overhead of a full operating system, the RP2040 strikes a perfect balance. It's powerful enough to handle complex tasks, yet straightforward for quick prototyping. This makes it an excellent choice for applications where a small display is beneficial, such as portable devices, educational tools, and compact IoT projects.

<img src="https://circuitpython.org/assets/images/boards/large/waveshare_rp2040_geek.jpg" >

### Possibilities

**Handheld Devices:**
- **Portable Games:** Create simple handheld games using the built-in color LCD for graphics and buttons for control.
- **Digital Notepad:** Develop a small digital notepad that allows users to write and save notes using a simple interface.

**User Interfaces:**
- **Custom GUIs:** Design custom graphical user interfaces for other projects, such as control panels for home automation or industrial applications.
- **Status Monitors:** Implement a device that shows real-time data or status updates from sensors or online services.

**Educational Tools:**
- **Learning Kits:** Build educational kits for learning programming and electronics, leveraging the LCD to display information, instructions, or feedback.
- **Interactive Displays:** Create interactive learning tools for classrooms, where students can interact with the display and buttons.

**Wearable Tech:**
- **Smart Badges:** Design smart badges for events or conferences that display attendee information, schedules, or messages.
- **Fitness Trackers:** Develop basic fitness trackers that display steps, heart rate, or other health metrics.

**IoT Devices:**
- **Weather Stations:** Implement a small weather station that shows temperature, humidity, and other environmental data on the LCD.
- **Home Automation:** Create control panels for home automation systems, allowing users to manage lights, temperature, and security from a single device.

**Art and Creativity:**
- **Mini Art Displays:** Design mini art displays or digital photo frames that cycle through images or animations.
- **Interactive Installations:** Build interactive art installations that respond to user inputs and display dynamic graphics.

**Prototyping and Testing:**
- **Sensor Data Display:** Use the board to display real-time data from various sensors for testing and prototyping purposes.
- **Control Interfaces:** Develop interfaces to control other devices or systems, using the display to show status and options.

### Technical Aspects

The RP2040 is impressively small and utilizes JST connectors for sensor connections, such as I2C for external communication. The integrated display and USB port are standout features that caught my attention. The display provides quick feedback when connected to sensors, and the USB port allows easy power connection via a power bank.

As I started exploring, I was impressed by its simplicity. Plugging it into my Mac, I was able to access it by directly loading Python scripts onto its root directory. Without a microSD card, I used the board's built-in memory, which, while limited, was sufficient for my initial experiments. The RP2040 runs [CircuitPython firmware](https://circuitpython.org/board/waveshare_rp2040_geek/), which allowed me to install a few libraries, like Adafruit Shapes, to create basic animations.

For my test, I created an animation of the Swiss flag. This hands-on experience highlighted the board's potential for quick prototyping and creative projects.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/200845412@N02/53892961357/in/dateposted-public/" title="Untitled"><img src="https://live.staticflickr.com/31337/53892961357_8640d918d6_z.jpg" width="360" height="640" alt="Untitled"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

Tormod also showcased other possibilities with the RP2040. Notably, there is a circular version of the integrated display, which can be used to create interfaces resembling watches or brooches.

### The Power of Community

What I want to emphasize and celebrate is the collaborative spirit fostered in gatherings like this summer camp. The participants are not only curious but also generous. Sitting there, I might never have discovered this board, or at least not so soon. Yet, because someone was involved and interested, I had the chance to learn about it. These encounters build a sense of community, highlighting the beautiful aspect of the information economy: sharing knowledge enriches everyone involved. This generosity and exchange of information are inspiring and invaluable for learning and innovation.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/200845412@N02/albums/72177720319257368" title="2024 07 RP2040 Swiss Flag"><img src="https://live.staticflickr.com/65535/53894213894_9031ddc305.jpg" width="640" height="480" alt="2024 07 RP2040 Swiss Flag"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## Tutorial: Creating a Small Animation with RP2040-GEEK by Waveshare and Adafruit Shapes Library

In this tutorial, we'll walk you through the steps to create a small animation on the RP2040-GEEK development board by Waveshare using the Adafruit Shapes library and CircuitPython 9.

#### **What You'll Need:**
- RP2040-GEEK Development Board by Waveshare
- USB cable
- Computer (Mac, Windows, or Linux)
- CircuitPython firmware
- Adafruit Shapes library

#### **Step 1: Set Up CircuitPython on RP2040-GEEK**
1. **Download CircuitPython Firmware:**
    - Visit the [CircuitPython downloads page](https://circuitpython.org/board/waveshare_rp2040_geek/).
    - Download the latest firmware for the RP2040-GEEK.

2. **Install CircuitPython:**
    - Connect your RP2040-GEEK to your computer using the USB cable.
    - Double-click the reset button on the board to put it into bootloader mode. The board should appear as a USB drive named `RPI-RP2`.
    - Drag and drop the downloaded `.uf2` file onto the `RPI-RP2` drive. The board will reboot and appear as a new USB drive named `CIRCUITPY`.

#### **Step 2: Install Required Libraries**

1. **Download Adafruit CircuitPython Library Bundle:**
    - Go to the [Adafruit CircuitPython Library Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20240730).
    - Download the latest bundle as a `.zip` file.

2. **Copy Libraries to CIRCUITPY:**
    - Extract the downloaded `.zip` file.
    - Copy the following libraries from the extracted bundle to the `lib` folder on the `CIRCUITPY` drive:
        - `adafruit_display_shapes`
        - `adafruit_displayio_ssd1306` (if using an OLED display)

#### **Step 3: Write Your Python Script**

1. **Create a New Python File:**
    - On the `CIRCUITPY` drive, create a new file named `code.py`.

2. **Write the Animation Code:**

```python
import time
import gc
import board
import displayio
from adafruit_display_shapes.rect import Rect

# use built in display (MagTag, PyPortal, PyGamer, PyBadge, CLUE, etc.)
# see guide for setting up external displays (TFT / OLED breakouts, RGB matrices, etc.)
# https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-and-display-bus
display = board.DISPLAY

# Make the display context
main_group = displayio.Group()

# Make a red background color fill
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

# Setting up the cross starting position
posx = 50
posy = 50

# Define cross characteristics
cross_size = 50
cross_color = 0xFFFFFF

# Create horizontal and vertical rectangles to form the cross
horizontal_rect = Rect(posx - cross_size//2, posy - cross_size//8, cross_size, cross_size//4, fill=cross_color)
vertical_rect = Rect(posx - cross_size//8, posy - cross_size//2, cross_size//4, cross_size, fill=cross_color)

main_group.append(horizontal_rect)
main_group.append(vertical_rect)

# Define cross Animation Steps
delta_x = 2
delta_y = 2

# Showing the items on the screen
display.root_group = main_group

while True:
    if vertical_rect.y + cross_size//2 >= display.height:
        delta_y = -2
    if horizontal_rect.x + cross_size//2 >= display.width:
        delta_x = -2
    if horizontal_rect.x - cross_size//2 <= 0:
        delta_x = 2
    if vertical_rect.y - cross_size//2 <= 0:
        delta_y = 2

    horizontal_rect.x = horizontal_rect.x + delta_x
    vertical_rect.x = vertical_rect.x + delta_x
    horizontal_rect.y = horizontal_rect.y + delta_y
    vertical_rect.y = vertical_rect.y + delta_y

    time.sleep(0.02)
    gc.collect()

```

#### **Step 4: Run Your Script**

1. **Save the Script:**
    - Save the `code.py` file on the `CIRCUITPY` drive.
    - The RP2040-GEEK board will automatically run the script, displaying the animation on the integrated display.

2. **Observe the Animation:**
    - You should see a red background with a white cross around the screen.
