---
layout: post
title: Tinkering for 2 Hours with a Canon EOS 40D That's Older Than My Daughter
id: 2024-07-29-tinkering-for-2-hours-with-a-canon-eos-40d-that-s-older-than-my-daughter.md
categories:
  - documentation
  - prototype
  - image
image: https://live.staticflickr.com/65535/53889286795_096bf5048f_z.jpg
share: "true"
comments: "true"
filename: Blog/_posts/2024-07-29-tinkering-for-2-hours-with-a-canon-eos-40d-that-s-older-than-my-daughter.md
tags:
  - camera
  - tutorial
  - homemade2024
  - python
  - raspberry-Pi
date: 2024-07-29
author: lina
---
## Introduction

Yesterday, I met [Felix Bänteli](https://mrfx.ch/kontakt/), an artist who has a passion for collecting vintage equipment. Among his treasures was a 2007 Canon EOS 40D, a groundbreaking camera at its time. As we chatted, we remarked on how images on social media, especially on platforms like Instagram, all share the same polished aesthetic. These images, with their perfect lighting and impeccable composition, for me often blur the line between reality and AI-generated content.

This conversation sparked an idea: what if we tinkered with this ancient camera to create something unique and different? We decided to connect it to a Raspberry Pi 3 to stream its live view over the network, pushing the boundaries of what this old device could do. The EOS 40D, primarily a stills camera, was among the first to offer a live view feature. Using tools like `gphoto2` and `ffmpeg`, we aimed to capture and stream its live preview.

The results were amusing and thought-provoking. **The live stream had a noticeable green glitch and a significant delay, likely due to network latency or the camera's processing capabilities. However, this "flawed" imagery made us question the homogeneity of modern social media visuals**. The glitches and imperfections in our stream felt more authentic, a stark contrast to the over-polished photos we see daily. It was a reminder that not all images need to be perfect to be genuine.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/200845412@N02/53889331530/in/album-72177720319202357/" title="Screen Recording 2024-07-29 at 16.07.46"><img src="https://live.staticflickr.com/31337/53889331530_bf35db3444_z.jpg" width="640" height="426" alt="Screen Recording 2024-07-29 at 16.07.46"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

_VIDEO 1 green glitch_

In experimenting with this setup, we captured a screenshot directly from the Raspberry Pi, revealing the familiar scene of a table and window in a distorted yet fascinating way. These abstracted views of light, color, and shadow challenged our perceptions and inspired us to think differently about photography in the digital age, **think about the non-human like other animals and machines see the world around**.

<img src="https://live.staticflickr.com/65535/53888918021_e21f91b7f8_z.jpg"/>

_The room as human/camera see_

<a data-flickr-embed="true" href="https://www.flickr.com/photos/200845412@N02/53888910621/in/album-72177720319202357/" title="Screen Recording 2024-07-29 at 16.04.50"><img src="https://live.staticflickr.com/31337/53888910621_e0ed48685a_z.jpg" width="640" height="428" alt="Screen Recording 2024-07-29 at 16.04.50"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

_VIDEO 2 The room as machine/camera see_

This experiment was more than just a technical exercise; it was a playful exploration of the old and new, a reflection on the current state of digital imagery and imagination. **Maybe we can keep tinkering in the direction of the machine/camera see with the colors and numbers... maybe we can find how the machines dreams...**

---
## Setting Up a Live Stream from Canon EOS 40D on Raspberry Pi to Mac

#### Requirements:

- Raspberry Pi (with Raspbian installed)
- Canon EOS 40D
- Mac computer
- SSH access to Raspberry Pi
- Installed `gphoto2`, `ffmpeg`, and VLC

#### Steps:

1. **Access the Raspberry Pi via SSH**: Open the terminal on your Mac and connect to your Raspberry Pi using SSH. You can check in the tutorial [below](## Tutorial: Setting Up and Accessing Your Raspberry Pi 3 from a Mac Terminal)
2. **Update Raspberry Pi**: Update the package list and upgrade all packages to their latest versions:
```sh
sudo apt-get update
sudo apt-get upgrade
```
3. **Install gphoto2**: Install `gphoto2` for capturing the live view from the Canon EOS 40D:
```sh
sudo apt-get install gphoto2
```
4. **Install ffmpeg**: Install `ffmpeg`, which will be used to stream the video over the network:
```sh
sudo apt-get install ffmpeg
```
5. **Capture and Stream Live View**: Use `gphoto2` to capture the live view and pipe it to `ffmpeg` for streaming over HTTP:
```sh
gphoto2 --capture-movie --stdout | cvlc - --sout '#standard{access=http,mux=ts,dst=:8080/liveview}'
```
6. **Open VLC on Mac**: Open VLC on your Mac and go to `File > Open Network Stream`. Enter the network URL of your Raspberry Pi stream:
```
http://<Raspberry_Pi_IP_Address>:8080/liveview
```

### Alternative: Local Testing on Raspberry Pi

Before streaming over the network, it is useful to test the live view capture locally on the Raspberry Pi. This helps to ensure the setup is working correctly before adding the network layer.

**Local Capture and View**: Capture the live view locally and open it with VLC directly on the Raspberry Pi:
```sh
gphoto2 --capture-movie --stdout | cvlc
```

---
## Tutorial: Setting Up and Accessing Your Raspberry Pi 3 from a Mac Terminal

In this tutorial, we'll walk through the steps to set up your Raspberry Pi 3 using your Mac terminal. This includes preparing the micro SD card, configuring network settings, and accessing the Raspberry Pi 3 via SSH.

#### Step 1: Download Raspberry Pi Imager
[**Install Raspberry Pi Imager**](https://www.raspberrypi.com/software/) on your Mac.

#### Step 2: Prepare the SD Card

1. **Insert the micro SD card** into your Mac.
2. **Launch Raspberry Pi Imager**.
3. **Choose OS**: Select "Raspberry Pi OS (64-bit) recomended"
4. **Choose Storage**: Select your micro SD card.
5. **Advanced Options**:
    - Enable SSH by checking the appropriate box.
    - Configure Wi-Fi by entering your SSID and password.
    - Optionally set the hostname, e.g., `camera.local`.
6. **Write**: Click the "Write" button to start the process. Raspberry Pi Imager will download the chosen OS image and write it to your micro SD card.

#### Step 3: Eject the SD Card

- Safely eject the SD card from your Mac once the writing process is complete.

#### Step 4: Insert SD Card and Power Up

- Insert the SD card into the Raspberry Pi and power it on.

#### Step 5: Find the Raspberry Pi’s IP Address

Use a network scanning tool to find the IP address of your Raspberry Pi.

**Using `arp-scan`**:

1. Install `arp-scan`:

``` sh
brew install arp-scan
```

2. Scan your network:

```sh
sudo arp-scan --localnet
```

Look for the Raspberry Pi in the output.

#### Step 6: SSH into the Raspberry Pi

1. **Open your terminal** on Mac.
2. **SSH into the Raspberry Pi**:

If using hostname:

```sh
ssh pi@camera.local
```

If using IP address:

```sh
ssh pi@<IP_ADDRESS>
```

The default username is `pi` and the default password is `raspberry`.

#### Step 7: Change Default Password

For security reasons, change the default password once you log in:

```sh
passwd
```

### Summary

- **Download** and install Raspberry Pi Imager.
- **Prepare** the micro SD card using the imager, enabling SSH and configuring Wi-Fi.
- **Insert** the SD card into the Raspberry Pi and power it up.
- **Scan** your network to find the Raspberry Pi’s IP address.
- **SSH** into the Raspberry Pi from your Mac terminal using the default credentials.