---
layout: post
title: Rap Battle Project - From Idea to Execution
id: 2024-09-03-rap-battle-project-from-idea-to-execution.md
categories:
  - documentation
  - digital tools
  - AI projects
image: https://live.staticflickr.com/65535/54016162230_e5894af3e0_o.jpg
share: "true"
comments: "true"
filename: Blog/_posts/2024-09-03-rap-battle-project-from-idea-to-execution.md
tags:
  - ai
  - machine-learning
date: 2024-09-03
author: lina
---
## Rap Battle Project - From Idea to Execution
The idea for the Rap Battle Project was born during a unique educational experience—my specialization in **Machine Learning and AI for Creative Practices**, a partnership between the **School of Design and Arts of Zurich** and the **Institute of Mathematics at the University of Bern**. The program bridges creative practices with technical disciplines, with some modules led by professors from the arts and design fields, while others are led by mathematicians and data scientists. This interplay between conceptual and technical knowledge is where I find myself most inspired.

The first module, led by **Professor Chris Salter**, was an immersive three-day exploration of the **genealogy and history of AI**. Salter, a professor with a background in both Canada and the United States, has been teaching in Europe for the past two years. His lectures were intense—three full days, from 9 a.m. to 5 p.m.—focusing on the origins of AI as a concept, the various philosophical approaches like **symbolic AI** and **connectionism**, and how these ideas evolved over time.

During these lectures, I found myself compulsively taking notes. I’m someone who documents everything, especially when it involves expanding my creative repertoire with new technical tools and concepts. This was not my first experience working with AI or Machine Learning, but it was the first time I was approaching it with a deeper conceptual focus. Before, I had experimented with algorithms, tinkering and exploring their potential. But now, I was eager to understand not only _how_ these technologies work but also _why_ they exist in the form they do, and what historical and conceptual frameworks shaped them.

One of the papers we discussed was particularly fascinating—it delved into the **mnemonic and metaphorical challenges** of the language we use around AI. For instance, when we talk about **Machine Learning**, it creates the impression that machines are truly "learning" in a way similar to humans. However, Machine Learning is more about identifying patterns within data to make decisions or predictions, rather than any form of human-like learning. This leads to philosophical debates—what does it really mean to say a machine is "learning"? And does this metaphor, while useful for explaining the field, sometimes obscure the more technical realities?

These questions about the genealogy of AI concepts fascinated me, and I took detailed notes throughout the lectures. After three days, I had documented **74 authors** mentioned by Professor Salter during the course. Being curious by nature, and wanting to synthesize what I had learned, I turned to **ChatGPT** to help me process and organize my notes. Through this interaction, I managed to extract the names and key details of these authors, ultimately compiling them into a spreadsheet. It was then that the project started to take shape.

### What Do You Do with a Spreadsheet Full of Authors?

So there I was, staring at a spreadsheet with all these authors—74 of them, to be precise. I was curious about who they were, where they came from, how long they had been researching, and in which years they were active. I wanted to understand the timeline, the regions of the world they represented, their genders, and most importantly, their key contributions to AI and Machine Learning—whether through papers, books, or, in some cases, films, as there were also documentarians and artists in the mix.

I looked at this dataset and asked myself, “What do I do with all of these authors?” And the answer came to me: **Rap Battle**.

Why not? Many of these authors are deeply embedded in academia, a space where ideas are exchanged, debated, and perspectives are constantly challenged. Sure, we don’t expect to see academics battling it out like rappers, but in a sense, they are using words just like rappers do. So why not pit them against each other in an imaginary academic rap battle? It’s a fictional scenario, but one based on real facts.

With the initial idea in mind, I jumped straight into prototyping. When I build something, whether it’s physical or digital, I like to test it quickly. I call this a “dirty prototype” — something that helps me understand the scope of the project before turning it into a polished product. I grabbed my Google Spreadsheet and opened Visual Studio Code, ready to make a quick JavaScript script that connected the API and ran on a local server.

I created two dropdowns, one for **Author 1** and one for **Author 2**. Then I built a simple prompt: generate a rap battle between the two selected authors from the dropdown, pulling their names from the spreadsheet. I sent the prompt, received a response, and displayed it on the screen. The whole thing took about 20 minutes—quick and dirty. It wasn’t beautiful, responsive, or organized, but it was a start.

Then I thought, “It would be great if I had mini-bios for these authors.” I was selecting names from a dropdown, but many of them didn’t stick in my memory. I’m not an expert on all 74 authors—Professor Salter is the one who really knows these people inside and out. But I needed a way to get a quick understanding of who they were. So I turned once again to **OpenAI** and built a Python script to generate mini-bios for each author.

With just a few pieces of information, I sent the names to ChatGPT and had it generate mini-bios, which were then automatically written directly into my Google Spreadsheet. This was my first time using the Google API to write data back to a spreadsheet, and it was a great learning experience. I fetched the information from the sheet, sent it to the OpenAI API, received the responses, and saved them back to the relevant columns in the spreadsheet.

Next, I updated my JavaScript code to pull from this new column with the mini-bios whenever an author was selected for the Rap Battle. The basic structure was there—I had built something that worked.

By generating these mini-bios and associating them with the rap battle, I was able to start learning the authors' names, their contributions, and a few key details about them. It was a way of turning the rapid influx of information from those three days of lectures into something I could **apply**. For me, the Rap Battle project became a tool for solidifying what I had learned—turning raw data into knowledge by actively engaging with it.

And that’s where I’ll leave it for now. This is how a playful project like Rap Battle became a method for me to absorb, process, and apply the vast amount of information presented in class—and maybe even have a little fun with it.