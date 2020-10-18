# cpblogsystem

# **Usage**

## Prerequisites
- A `blog` folder in your root directory
- `cpblogsystem.py` and `cpblogsystem.js` in your root directory
- The HTML file you want the homepage of the blog to be
- An icon to use for your blog posts
- Make sure Python 3 is installed on your computer

First, and arguably the most important, install Python! I used Python 3 in this project, but newer or older versions may work as well. Download Python from python.org.

Second, you must configure the settings. In `cpblogsystem.js`, the first line contains the path to the icon that you want to use for your blog posts. Change it to the path that you want to use. In `cpblogsystem.py`, you can change the header and footer text of the HTML file to be created. You could add stylesheets or anything you would like.

Third, create an HTML file to be the homepage of your blog, preferably named `index.html`. Somewhere in the body, type `<div id="blog"><script src="cpblogsystem.js"></script></div>`. This will be where the blog posts will show up.

Fourth, open a terminal, navigate to the directory where all these files are saved, and type `python3 cpblogsystem.py`... and there you have it! You can create blog posts, edit them, and delete them. You would never have to touch any line of code again!

# **Credits**

Created by Chase Peck under the MIT License