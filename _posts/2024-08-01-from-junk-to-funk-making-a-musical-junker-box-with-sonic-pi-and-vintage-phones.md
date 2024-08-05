---
layout: post
title: From Junk to Funk, Making a Musical Junker Box with Sonic Pi and Vintage Phones
id: 2024-08-01-from-junk-to-funk-making-a-musical-junker-box-with-sonic-pi-and-vintage-phones.md
categories:
  - documentation
  - sound
  - AI projects
image: https://live.staticflickr.com/65535/53896955078_978ca5f438_z.jpg
share: "true"
comments: "true"
filename: Blog/_posts/2024-08-01-from-junk-to-funk-making-a-musical-junker-box-with-sonic-pi-and-vintage-phones.md
tags:
  - homemade2024
  - sonic-pi
  - openai
  - python
date: 2024-08-01
author: lina
---

## Sonic Pi: An Introduction

Sonic Pi is an open-source programming environment designed for creating live music performances. Developed by Dr. Sam Aaron at the University of Cambridge Computer Laboratory, it has been in the market since 2014. Sonic Pi is built on top of SuperCollider, a platform for audio synthesis and algorithmic composition. The main goal of Sonic Pi is to introduce coding to a broader audience, particularly children, by making programming engaging and accessible through music.

The software has gained significant traction in both educational and creative sectors. It is widely used in classrooms to teach the basics of programming and music composition, as well as by professional musicians and live coders who perform complex, real-time audio compositions. Sonic Pi's intuitive interface and powerful capabilities make it an ideal tool for both beginners and experienced users.

## Workshop and Creative Reuse of Vintage Phones

[Felix Bänteli](https://mrfx.ch/kontakt/), an artist and musician with a penchant for vintage technology, has amassed a collection of classic landline phones. These devices, with their distinctive bakelite keypads and analog mechanisms, evoke a sense of nostalgia and craftsmanship. Felix's dedication to repurposing old electronics aligns perfectly with the ethos of sustainability and creative reuse.

During a recent Sonic Pi workshop led by Felix, participants were introduced to the basics of live coding and electronic music performance. During the workshop, I had an idea, why not bridge the gap between the analog charm of vintage phones and the digital creativity enabled by Sonic Pi? The potential to create unique audio-visual experiences by integrating old technology with modern programming tools became a focal point of my session.

## Possibilities with Sonic Pi

Sonic Pi offers a wide array of possibilities for users:

1. **Live Coding Performances**: Users can write and modify code in real-time to create dynamic music performances. This aspect of Sonic Pi is particularly popular in the live coding community, where musicians and programmers perform live shows.
    
2. **Educational Tool**: It serves as an excellent educational platform, introducing students to programming concepts through interactive and enjoyable lessons. Sonic Pi is used in schools worldwide to teach coding in a fun and engaging way.
    
3. **Creative Exploration**: Beyond its educational value, Sonic Pi is a powerful tool for creative expression. Artists and musicians can experiment with sound synthesis, rhythm, and composition, pushing the boundaries of conventional music production.
    
4. **Community and Collaboration**: Sonic Pi has a vibrant community of users who share their code, performances, and experiences. This collaborative spirit fosters continuous learning and innovation within the platform.

## Bridging the Gap: From Musical Concepts to Sonic Pi with OpenAI

As someone without a formal musical background, I found myself grappling with the fundamental concepts of music during the Sonic Pi workshop. I think understanding these concepts is crucial for translating musical thoughts into programmable code. It felt akin to building with LEGO without knowing the basic pieces—challenging and somewhat daunting.

In an attempt to overcome this, I turned to ChatGPT for assistance. By requesting the code for specific songs, like the theme from Inspector Gadget, I began to see how musical elements are structured within Sonic Pi. This approach allowed me to dissect and modify the provided code, gradually building my understanding of musical composition in a programmable context.

However, the process of switching between the ChatGPT interface and Sonic Pi was cumbersome. This sparked an idea: what if I could directly request and implement code in Sonic Pi using voice commands? To achieve this, I leveraged the OpenAI API for speech transcription, coupled with OSC (Open Sound Control) to establish a direct connection between my voice and Sonic Pi.

By integrating these technologies, I created a seamless workflow where I could verbally request a song, receive the corresponding Sonic Pi code, and immediately start experimenting with it. This direct link not only streamlined my creative process but also made it more intuitive and accessible, even for someone without a deep musical background.

This innovative approach highlights the potential of combining modern AI capabilities with creative coding platforms, opening new doors for musical exploration and education.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/200845412@N02/53896713791/in/album-72177720319282088/" title="Untitled"><img src="https://live.staticflickr.com/31337/53896713791_96d1ffc459_z.jpg" width="360" height="640" alt="Untitled"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## Creating a Musical Junker Box: Connecting Vintage Phones with Sonic Pi via OpenAI

So, off I went to delve into Python scripts. Python, with its voice recognition capabilities, was my tool of choice for creating a voice-controlled prompt. I set up a system where I could verbally request a song. This voice prompt would be processed by the OpenAI API, which in turn generated the corresponding Sonic Pi code for the requested song.

Once the code was generated by OpenAI, it was sent back in the format Sonic Pi expects, and then transmitted via OSC (Open Sound Control). OSC is a protocol used in music technology for networking sound synthesis and performance. It allows for the transmission of music-related data over a network, enabling various devices and software to communicate seamlessly. In my setup, Sonic Pi simply needed to be open and listening on the correct port to receive and play the generated music.

For the final touch, I repurposed an old landline phone, utilizing its microphone and speaker. I connected it through an audio interface, specifically the UR22, which [Claude Treptow](https://www.linkedin.com/in/claude-treptow-a0bb1214b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) one of the artists at the Summer Camp provided. This interface allowed me to link the vintage phone components to my computer, bridging the analog-digital divide.

The result was a whimsical musical junker box. I could pick up the phone handle, request a song—say, "Happy Birthday" for Miranda's birthday—and hear the melody played back through the phone's speaker. This entire process was driven by my voice command, interpreted by OpenAI, and executed in Sonic Pi.

This project exemplifies the joy of experimentation. Even without a deep understanding of music theory, I was able to leverage modern tools to explore and create. By combining vintage technology with cutting-edge software, I turned a simple workshop exercise into an innovative and fun musical experience.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/200845412@N02/albums/72177720319282088" title="2024 07 Vintage Phone To Sonic Pi"><img src="https://live.staticflickr.com/31337/53896713791_96d1ffc459.jpg" width="640" height="480" alt="2024 07 Vintage Phone To Sonic Pi"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## Tutorial/Codes
### Configuration Sonic Pi

```
define :execute_commands do |commands|
  commands.each do |command|
    eval command
  end
end

live_loop :foo do
  use_real_time
  commands = sync "/osc*/trigger"
  execute_commands(commands)
  synth :piano
end
```

### Script Python - voice recognition and OpenAI

```python
import speech_recognition as sr
import openai
from pythonosc import udp_client

# Set your OpenAI API key
openai.api_key = 'YOUR-OPENAI-KEY'

# Set up OSC client
client = udp_client.SimpleUDPClient("127.0.0.1", 4560) # Ensure this matches your Sonic Pi setup

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your musical prompt...")
        audio = recognizer.listen(source)

    try:
        prompt = recognizer.recognize_google(audio)
        print(f"You said: {prompt}")
        return prompt
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there's an issue with the voice recognition service.")
        return None

def get_music_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate Sonic Pi (just the sequence code, NONE other word NOT THE WORD RUBY) code (without the definition of bpm or synth) for the following musical request: {prompt}"}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def send_code_to_sonic_pi(code):
    client.send_message("/trigger", code)
  
if __name__ == "__main__":
    prompt = get_voice_input()
    if prompt:
        code = get_music_code(prompt)
        print(f"Generated Sonic Pi code:\n{code}")
        send_code_to_sonic_pi(code)

```
