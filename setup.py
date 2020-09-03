import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randopedia",
    version="0.0.1",
    author="Zachary Piazza",
    author_email="zjpiazza@gmail.com",
    description="Retrieve a random wikipedia article",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zjpiazza/randopedia",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'html2text'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
