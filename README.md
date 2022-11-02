# How to host a resume on Github Pages
## Purpose
This README describes the steps on how to host and format a resume using Markdown, a Markdown editor, GitHub Pages and Jekyll.

The instructions have been laid down in a format that abides the general principles of technical writing, as explained by Andrew Etter in _Modern Technical Writing_.

> According to Etter, documentation as such should be open-source and be written with an aim for other people to contribute to it.

Link to this book can be found under [more resources.](#more-resources)

---

## Prerequisites
Below are the two main things you would require before proceeding:
- A resume formatted in Markdown.
- A Github account.
- Install Jekyll on your computer.

> According to Etter's Modern Technical Writing, he emphasizes on the use of Lightweight Markup Languages such as Markdown or AsciiDoc (for linux users) since they are easy to learn and are human-readable in its raw form as well.

See [more resources](#more-resources) for links to Markdown tutorial, Github tutorial and Jekyll installation.

---

## Instructions
### 1) Search for static website themes.
Having learnt basics of Markdown and having created a Github account,  you can now begin by searching for static website themes supported by Github pages and Jekyll over the internet.

A couple of good themes have been linked under [more resources.](#more-resources)

> Etter describes in his book that static websites are easy to setup, secure and are fast. They do not have server side dependencies and therefore they are not generated dynamically.


### 2) Fork the repository.
> According to Github docs by forking a repository a copy of it is created in your profile, from which changes can be made without affecting the original repository.

Once the theme has been selected, go to its github repository;

  1.  On the repository, click the `Fork` button found on top-right part of the screen.  
  2.  This would prompt you to enter a repository name.
      - It is very important to note that the repository name should be written as `username.github.io`
      - Leave the default setting as is, and finally
      - click on `create fork` button.

### 3) Modifying the resume template.
- Now that we already have the theme/template copied on our repository, we can go ahead and edit the `_config.yml`. 
- By editing the `_config.yml` file we will be able to modify and add content of your own resume to show on the static website.
  1. To edit the file, click on the file, then click on the pencil icon at the top.
  2. Add your content to the file, write a commit message such as "updated _config.yml" or "added resume content" and press the `Commit changes` button.

> This ensures the website content is updated instantly. In his book, Andrew Etter advices to host content on website for the very same reason and also adds that in this way content is kept in sync to new updates.

### 4) Viewing the website.
🎉Congratulations!🎊 You have successfully hosted a resume on Github Pages.  

You should now be able to view your static website at `https://username.github.io/`

Here after, any updates added to the `_config.yml` file will automatically be synced with the website and will be ready to be viewed on a browser as soon as github pages reloads the website in the background. 

#### Below is an animated GIF demo of the hosted resume:

![](./assets/demo.gif)


### More Resources
1. Learn how to use [Markdown.](https://www.markdowntutorial.com/)
2. To purchase Andrew Etter's _Modern Technical Writing_ follow [this link.](https://www.amazon.ca/Modern-Technical-Writing-Introduction-Documentation-ebook/dp/B01A2QL9SS)
3. [Github Tutorial](https://docs.github.com/en) - to learn more on how to make your way through learning Github.
4. [Jekyll Installation.](https://jekyllrb.com/docs/)
5. Interested in AsciiDoc? [Here](https://asciidoc.org/) is the link to learn more about it.
6. Links to excellent themes for resume hosting:
   - [Modern Resume Theme](https://github.com/sproogen/modern-resume-theme)
   - [Jekyll Theme Minimal Resume](https://github.com/murraco/jekyll-theme-minimal-resume)

---

## Authors and Acknowledgements
- This theme is originally inspired and created by [James Grant](https://github.com/sproogen/modern-resume-theme). It has been created using _Jekyll_ and _Github pages_.
- List of group members who assisted in making improvements to the README file: 
  1. Benjamin Schneider
  2. Sanskar Raval
  3. Akash Chouhan

---
## FAQs 
#### Why is my resume not showing up?
1. Ensure your Github repository name is `username.github.io`. This can be changed from **Repository Settings > General > Repository name**
2. Ensure your Github repository is `public`. This can be changed from **Repository Settings > General > Danger Zone > Change respository visibility**
3. Ensure your Github pages is built from `master` branch. This can be changed from **Repository Settings > Pages > Build and deployment > Branch**

#### How can I locally run the website on my local computer?
- Ensure you have Ruby and Jekyll installed in your computer. You can find the process of installing Ruby and Jekyll under  [more resources](#more-resources)).
- To run the website locally, follow the steps as follows:
  1. Download the code from github and store it in your local computer.
     - Click on the green `Code` button on your Github repository, then click `Download ZIP`.
     - Extract the content inside the ZIP folder to a new folder and name it. 
  2. `cd [your-folder-name]`
  3. `bundle install`
  4. `bundle exec jekyll serve`

- As simple as that, the website can now be viewed locally on `http://localhost:4000` or on `http://127.0.0.1:4000/`