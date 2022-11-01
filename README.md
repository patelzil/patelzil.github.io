# How to host a resume on Github Pages
## Purpose
This README describes the steps on how to host and format a resume using Markdown,  a Markdown editor, GitHub Pages and Jekyll.

---

## Prerequisites
> According to Etter's Modern Technical Writing, he emphasizes on the use of Lightweight Markup Languages since they are easy to learn and make it easy to read in its raw form.

- A resume formatted in Markdown
- A Github account

See [More resources](#more-resources) for links to Markdown and Github tutorials.

---

## Instructions
### 1. Fork the repository.
> According to Github docs, "A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project."

- You can search for templates supported by Github pages over the internet. [Here](https://github.com/sproogen/modern-resume-theme) is the link to the one I used to create my static website.
  1.  On the repository, click the `Fork` button found on top-right part of the screen.  
  2.  Enter the repository name as `username.github.io`, leave the default setting as is and click on `create fork` button.

### 2. Modifying the resume template.
- Edit the `_config.yml` file to modify and add content of your own resume.
  1. To edit the file, click on the file, then click on the pencil icon at the top.
  2. Once you have added your resume content to the file, write a commit message such as "updated _config.yml" or "added resume content" and press the `Commit changes` button.

### 3. Viewing the website.
To view your static website go to `https://username.github.io/`

Congratulations! You have successfully hosted a resume on Github Pages.

#### Below is an animated GIF demo of the hosted resume:

![](./assets/demo.gif)


### More Resources
1. [Markdown Tutorial](https://www.markdowntutorial.com/)
2. [Andrew Etter's _Modern Technical Writing_](https://www.amazon.ca/Modern-Technical-Writing-Introduction-Documentation-ebook/dp/B01A2QL9SS)
3. [Github Tutorial](https://docs.github.com/en)

---

## Authors and Acknowledgements
- This theme, powered by _Jekyll_ and _Github pages_, is originally inspired and created by [James Grant](https://github.com/sproogen/modern-resume-theme).
- Group Members: 
  - Benjamin Schneider
  - Sanskar Raval
  - Akash Chouhan

---
## FAQs
#### Why is Markdown better than a word processor?
- Markdown is better than a word processor because of how simple and limited its features are. This makes it easier for anyone to learn. It also reduces the amount of time wasted trying to look for a formatting button, as is the case with word processors.
 
#### Why is my resume not showing up?
1. Ensure your Github repository name is `username.github.io`. This can be changed from **Repository Settings > General > Repository name**
2. Ensure your Github repository is `public`. This can be changed from **Repository Settings > General > Danger Zone > Change respository visibility**
3. Ensure your Github pages is built from `master` branch. This can be changed from **Repository Settings > Pages > Build and deployment > Branch**
