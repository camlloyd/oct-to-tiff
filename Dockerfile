# syntax=docker/dockerfile:1
FROM python:3.8.17-slim

LABEL org.opencontainers.image.authors="Cameron Lloyd <lloyd@med.unideb.hu>" \
      org.opencontainers.image.source="https://github.com/camlloyd/oct-to-tiff" \
      org.opencontainers.image.licenses="BSD-3-Clause" \
      org.opencontainers.image.title="oct-to-tiff" \
      org.opencontainers.image.description="A command line tool for converting optical coherence tomography angiography (OCTA) data."

WORKDIR /app

RUN pip install --no-cache-dir oct-to-tiff==0.4.0

COPY . .

ENTRYPOINT [ "python", "src/oct_to_tiff/cli.py" ]
