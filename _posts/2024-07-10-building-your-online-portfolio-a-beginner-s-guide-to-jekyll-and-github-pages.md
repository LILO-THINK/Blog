---
layout: post
title: "Building Your Online Portfolio: A Beginner’s Guide to Jekyll and GitHub Pages"
id: 2024-07-10-building-your-online-portfolio-a-beginner-s-guide-to-jekyll-and-github-pages.md
categories:
  - documentation
  - digital tools
  - tutorial
image: https://live.staticflickr.com/65535/53848757363_f2a44ba3e7_b.jpg
share: "true"
comments: "true"
filename: Blog/_posts/2024-07-10-building-your-online-portfolio-a-beginner-s-guide-to-jekyll-and-github-pages.md
tags:
  - Jekyll
  - github
date: 2024-07-10
author: lina
---

In today’s digital age, having an online portfolio is essential for showcasing your work and attracting potential clients or employers. This tutorial will guide you through creating and hosting a stylish, responsive portfolio using Jekyll and GitHub Pages. Jekyll is a simple, blog-aware static site generator that's perfect for creating personal sites and portfolios. GitHub Pages offers a free, easy way to host your static websites directly from a GitHub repository.

Ready to get started? Let’s dive in!

---

## Step 1: Installing Jekyll on Your Machine
### What You’ll Need

- A terminal (command line interface)
- Ruby (the programming language Jekyll is built on)

### Step-by-step
1. **Check for Ruby Installation:** 
	Open your terminal and type:
	
	```
	ruby -v 
	``` 
	
	If Ruby isn’t installed, you’ll need to install it. For macOS, you can use Homebrew: 
	
	```
	brew install ruby 
	```
	
	For Windows, use RubyInstaller: [Download RubyInstaller](https://rubyinstaller.org/)

2. **Install Jekyll and Bundler:** 
	With Ruby installed, you can now install Jekyll and Bundler gems: 
	
	```
	gem install jekyll bundler 
	```

## Step 2: Setting Up Your Jekyll Portfolio
#### Creating a New Jekyll Site
1. **Create a new Jekyll site:** 
	
	```bash
	jekyll new my-portfolio cd my-portfolio
	```
	
2. **Install Dependencies:** 
	
	```bash
	bundle install
	```
	
3. **Run Your Site Locally:** 
	
	```bash
	bundle exec jekyll serve
	``` 
	
	Open `http://localhost:4000` in your browser to see your site.

#### Configuring Your Portfolio 
1. **Markdown:** Use Markdown to write your content. Create a new file in the `_posts` directory with the following format:
	
	 ```markdown
	 ---
	 layout: post title: "My First Project" 
	 date: YYYY-MM-DD 
	 ---
	 
	 ## Project Title 
	 Description of your project. 
	 ```
	

2. **Structure:**
	- **_layouts:** Templates for your pages (e.g., default.html).
	- **_pages:** Individual pages (e.g., about.md).
	- **_posts:** Blog posts or project entries.
	- **_config.yml:** Your site’s configuration file.

### Step 3: Creating a GitHub Account and Repository

1. **Create a GitHub Account:** 
	If you don’t have one, sign up at [GitHub](https://github.com/).
2. **Create a New Repository:**
    - Click on the “New” button on your GitHub dashboard.
    - Name your repository `<your-username>.github.io`.
    - Initialize with a README file.

### Step 4: Hosting Your Portfolio on GitHub Pages

1. **Push Your Site to GitHub:**
	
	```bash 
	git init 
	git add . 
	git commit -m "Initial commit" 
	git remote add origin https://github.com/<your-username>/<your-repo>.git 
	git branch -M main 
	git push -u origin main 
	```

2. **Enable GitHub Pages:**
    - Go to your repository’s settings.
    - Scroll down to the “GitHub Pages” section.
    - Under “Source,” select the `main` branch and click “Save.”

3. **Visit Your Site:** Your portfolio will be live at `https://<your-username>.github.io/`.

# *

### Bonus Tips:

- **Custom Domain:** You can set up a custom domain for your GitHub Pages site in the repository settings.
- **Themes:** Explore and apply different Jekyll themes to give your portfolio a unique look.
- **Plugins:** Enhance your site’s functionality with Jekyll plugins.

For those of you who love to dive deeper and explore all the nifty details, check out the official Jekyll installation guide and the [GitHub Pages configuration page](https://docs.github.com/en/pages/getting-started-with-github-pages). These resources are packed with tips, tricks, and advanced features to make your portfolio truly shine.

Happy coding, and happy exploring! 🚀✨