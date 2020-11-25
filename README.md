# ricardobalk/folio

## Docker

1) Building the headless Scribus container

```bash
docker build -t scribus-headless .
```

2) Generating the PDF

```bash
mkdir -p export/
docker run -it -v "$PWD/:/home/scribus/" scribus-headless ./Portfolio.sla -g --python-script sla-to-pdf.py
```

3) That's it. PDF file should be available in `export/`.