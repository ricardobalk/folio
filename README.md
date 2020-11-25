# ricardobalk/folio

This is my portfolio, I switched from Adobe InDesign to Scribus because I love open-source software and Scribus allows to automate things.

So, what I did was automating the PDF generation. I used Docker for it because I also love Docker. Docker allows this thing to run without having to install a lot of stuff, and the 'headless Scribus' image can also be used for other documents. Cool. :sunglasses:

## Docker

1) Building the headless Scribus image

```bash
docker build -t scribus-headless .
```

2) Generating the PDF

```bash
mkdir -p export/
docker run -it -v "$PWD/:/home/scribus/" scribus-headless ./Portfolio.sla -g --python-script sla-to-pdf.py
```

3) That's it. PDF file should be available in `export/`.
