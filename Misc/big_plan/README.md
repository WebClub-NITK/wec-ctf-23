# **The big plan**

Category: Miscellaneous

Author: Md Arfath

Flag: `WEC{4tt4ck_0n_t4j}`

## Problem Statement

The Enemies have regrouped to plan their next big attack. Shaktimaan has succesfully destroyed one of the enemy groups, but wait he found a strange envelope. Can you help Shaktimaan save the planet?

## Relevant files / links

- [Strange envelope](https://drive.google.com/file/d/1nOYxXEoStuQBsPpt4RYSkbI8tj102Eqh/view?usp=sharing)

## Solution

- This file is a .png image, but we need to convert it to a tar file in order to extract its contents. To do this, we can use a file conversion tool or rename the file with a .tar extension and extract it using a tar utility.

- The given file is a tar archive. After extraction, we see many folders of layers with SHA hash names & manifest.json. This is the standard format of a docker image. This image file has to be loaded as an image.

- On looking at the image history you find a file being deleted
  `ENTRYPOINT [ "/bin/bash","-c","rm /home/wec1/site9/site6/siteA/attack1.txt"]`
  
- Run a new container with a --entrypoint flag to over-ride the default one.

- ```bash
   Docker run -it --entrypoint=/bin/bash <image-name>
  ```
  
- The file `attack1.txt` is a broken symlink pointing `/home/wec1/site6/site9/siteC/attack3.txt`

- `attack3` is compressed text file containing the key

Note = By default the used ubuntu image doesnt consist `file` cmd
