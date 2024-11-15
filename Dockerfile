# syntax=docker/dockerfile:1
FROM python:3.10.15-slim

LABEL org.opencontainers.image.authors="Cameron Lloyd <lloyd@med.unideb.hu>" \
      org.opencontainers.image.source="https://github.com/camlloyd/oct-to-tiff" \
      org.opencontainers.image.licenses="BSD-3-Clause" \
      org.opencontainers.image.title="oct-to-tiff" \
      org.opencontainers.image.description="A command line tool for converting optical coherence tomography angiography (OCTA) data."

RUN useradd --create-home appuser

WORKDIR /home/appuser

USER appuser

RUN pip install --no-cache-dir oct-to-tiff==0.4.0

ENTRYPOINT [ "python", "-m", "oct_to_tiff.cli" ]
