from setuptools import setup, find_packages

setup(
    name="News",
    version="1.0.0",
    author="Alfin Kresna",
    description="Program Sederhana Untuk Mengetahui Berita Terbaru",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "feedparser",
        "bs4",
        "ruamel.yaml",
    ]
)
