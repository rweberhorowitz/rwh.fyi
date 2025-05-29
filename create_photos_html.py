import os
import html


# This script walks through all descendant folders of "photos" and will create
# a sibling html file to each folder that points to all of the photos
# of the folder's children.

for dir, paths, files in os.walk("photos"):
    columns = 3 # columns three
    divided = [[] for _ in range(columns)] # 2d array that has the photos divided into columns
    for i, file in enumerate(sorted(files)): # go through all files
        divided[i % columns].append(dir + "/" + file) # sort them into columns
    with open(dir + ".html", "w") as f: # create the html file
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Riley Weber-Horowitz</title>
  <link rel="icon" type="image/x-icon" href="/content/logos/RWH_White_Cropped.svg">
  <link rel="stylesheet" href="/styles/styles.css" />
  <link href="https://fonts.googleapis.com/css2?family=Oswald&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div id="navbar-placeholder"></div>
  <script>
      fetch('/navbar.html')
        .then(res => res.text())
        .then(data => {
          document.getElementById('navbar-placeholder').innerHTML = data;
        })
        .catch(error => {
          console.error("Navbar load error:", error);
        });
    </script>

  <!-- Gallery -->
  <div class="row m-2 py-2">
""" + "".join(["""
    <div class="px-2 col-lg-4 mb-lg-0">
""" + "".join([f"""
      <img
        src="/{html.escape(photo)}"
        class="w-100 shadow-1-strong rounded mb-3"
      />
""" for photo in column]) + """
    </div>
""" for column in divided]) + """
  </div>
  <!-- Gallery -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
