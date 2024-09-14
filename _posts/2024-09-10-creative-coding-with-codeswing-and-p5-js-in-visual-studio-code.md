---
layout: post
title: Creative Coding with CodeSwing and p5.js in Visual Studio Code
id: 2024-09-10-creative-coding-with-codeswing-and-p5-js-in-visual-studio-code.md
categories:
  - documentation
  - digital tools
image: https://live.staticflickr.com/65535/53991623211_9e3414a98f_h.jpg
share: "true"
comments: "true"
filename: Blog/_posts/2024-09-10-creative-coding-with-codeswing-and-p5-js-in-visual-studio-code.md
tags:
  - vscode
  - code-swing
  - programing
  - education
date: 2024-09-10
author: lina
---
## Creative Coding with CodeSwing and p5.js in Visual Studio Code

When we work in a web development environment, we typically use HTML, CSS, and JavaScript. These three pillars of the web need to be rendered together—HTML for structure, CSS for style, and JavaScript for functionality—inside the browser. Usually, this involves setting up a local server, editing the code in a dedicated editor, and then previewing it in a browser. This workflow is quite standard, but it comes with some friction, especially for beginners in creative coding or for those who want to focus more on design and interaction than on server setup.

### The Challenge in Creative Coding Environments

In the realm of creative coding, especially when teaching or doing quick prototypes, the traditional development workflow can be a bit cumbersome. You might need to run a local server, open a terminal, and navigate between the code editor and browser. This can be a barrier, particularly for designers or artists who want to experiment with code but don’t want to deal with the hassle of server setup.

For instance, the [p5.js](https://p5js.org/) library has been a game-changer in this space. Designed with designers and artists in mind, it simplifies coding by providing an accessible environment for visual and interactive programming using JavaScript. The online p5.js editor is one solution to eliminate the friction of setting up a local environment, making it easy to code and see results instantly. It’s particularly useful for teaching, workshops, or quick experiments.

### Exploring Alternatives to Online Editors

I started wondering—what if you don’t want to use an online editor like the p5.js web editor? Or maybe you're teaching a class and prefer a more local setup for your students. How can you reduce the friction while maintaining a smooth coding experience? This led me to explore tools like [CodePen](https://codepen.io/), another fantastic web-based environment where you can write and execute HTML, CSS, and JavaScript in real-time.

However, I’ve always preferred using Visual Studio Code as my editor, and I wanted a solution that didn’t require bouncing between a browser, a terminal, and my editor.

### Enter CodeSwing for Visual Studio Code

I was thrilled when I discovered [CodeSwing](https://marketplace.visualstudio.com/items?itemName=codespaces.codeswing), an extension for Visual Studio Code. CodeSwing allows you to create and preview HTML, CSS, and JavaScript files all within the same environment—no need to set up a local server or open a browser. It significantly simplifies the process, making it ideal for demos or classes.

Once you install the CodeSwing extension, it automatically sets up a workspace with HTML, CSS, and JavaScript files. You can preview everything directly in Visual Studio Code without needing to start a local server or switch to a separate browser window. This makes it perfect for rapid experimentation, quick prototyping, or even live-coding sessions with students.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/200845412@N02/53991839928/in/dateposted-public/" title="Untitled"><img src="https://live.staticflickr.com/31337/53991839928_a120e56a58_h.jpg" width="1600" height="970" alt="Untitled"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

### Using p5.js with CodeSwing

Another reason I was excited about CodeSwing is that it works flawlessly with p5.js, which is one of the go-to libraries for creative coding in visual arts and design. Since p5.js is designed to make coding more accessible for artists, it complements CodeSwing's simplicity.

To use p5.js within CodeSwing, all you need to do is add the script for the p5.js library directly in the HTML file, like this:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>
```

After adding this, you can start writing your p5.js sketches as you would in the p5.js web editor, but with the added flexibility of Visual Studio Code and CodeSwing. Here's a simple example of a classic interactive sketch where a ball follows the mouse cursor:

```javascript
function setup() {
  createCanvas(windowWidth, windowHeight);
}

function draw() {
  background(220);
  ellipse(mouseX, mouseY, 50, 50);
}
```
This sketch will now render directly inside the CodeSwing preview pane, allowing for real-time updates as you code, without needing to switch between windows or set up any servers.

<img src="https://live.staticflickr.com/65535/53991623211_9e3414a98f_h.jpg" >
### Why CodeSwing?

CodeSwing offers the best of both worlds: the flexibility of working locally with a robust IDE like Visual Studio Code and the ease of real-time feedback typical of online editors like p5.js or CodePen. You can install it on your local machine, keep everything in a single workspace, and avoid the friction of constantly switching between the editor, browser, and terminal. This streamlined workflow is especially useful for teaching environments or quick demos where simplicity and speed are key.

### Final Thoughts

For designers and artists stepping into the world of creative coding, reducing friction in the development process is essential. Tools like p5.js and CodeSwing empower creators to focus more on the creative aspects of coding, without being bogged down by technical barriers. Whether you’re running a workshop, teaching a class, or just experimenting on your own, CodeSwing provides an intuitive, efficient environment that makes the process of creative coding smoother and more enjoyable.

If you're already familiar with Visual Studio Code, I highly recommend trying out CodeSwing for your next creative coding project!

Happy Coding!