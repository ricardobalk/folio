# ricardobalk/portfolio

This is my portfolio, I switched from Adobe InDesign to Scribus because I love open-source software and Scribus allows to automate things.

So, what I did was automating the PDF generation. I used Docker for it because I also love Docker. Docker allows this thing to run without having to install a lot of stuff, and the 'headless Scribus' image can also be used for other documents. Cool. :sunglasses:

## Git LFS

Because of the massive files, this repository requires Git LFS. Be sure that you have set up Git LFS, otherwise, you won't have images, fonts and <span title="colour: I prefer British English language.">colour</span> profiles.

**How to install Git LFS?**

Git LFS can be installed by `sudo apt install git-lfs` on Debian and <span title="Ubuntu, for example, is a Debian derivative">friends</span>, probably `yum` instead of `apt` on Fedora / CentOS,  `brew` on a macOS machine, or by downloading + installing one of those <span title="Windows users, I don't blame you, but Linux has a nice package manager that does the downloading + installing for you and it also keeps your PC updated. And you basically don't have interruptions anymore.">nasty executable files</span> on Windows-based computers.

## Docker

I also included a Dockerfile for running Scribus in a headless way, i.e. Scribus runs in a Docker container and can generate a PDF for you, without user input. Here's how to do it:

> I assume that you have a working installation of Docker, have cloned this Git repository to a place of choice and are in that directory, obviously.

### 1) Build the headless Scribus image

```bash
docker build -t scribus-headless .
```

This will build a Docker image for running Scribus in a headless way (no user input, no GUI).

### 2) Generating the PDF

Let's create a directory called `export`, attach the local directory to Docker and run the Scribus docker image inside a Docker container!

```bash
mkdir -p export/
docker run --rm -it -v "$PWD/:/home/scribus/" scribus-headless ./Portfolio.sla -g --python-script sla-to-pdf.py
```

That's it. PDF file should be available in `export/`.
