FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

RUN apt-get update && apt-get install -y \
    python3 \
    latexmk \
    lmodern \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-lang-english \
    texlive-pictures \
    texlive-science \
    texlive-extra-utils \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*
