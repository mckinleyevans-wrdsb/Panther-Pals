from js import current_pathname

# print(current_pathname)


# Ok so I did a bunch of research and I think what this will come down to is....
# - our main page stays in index.html
# - other pages get a folder with the page name (which will show up in the pathname) containing an index.html
# - this means we should set up a basic non-home page version of this, with the header and a content body only, where the appropriate content can be built
# - for our own sanity, we should also include that page/compoenents specific py & css files (and any other source files we end up needing)

# E.g. calendar/ will contain
# - index.html
# - calendar.py
# - calendar.css with all calendar-based styling