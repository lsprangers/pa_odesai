import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cup-a-code-smoot",    # <package name>_<pypi username>
    version="0.1.1",
    author="Luke Sprangers",
    author_email="sprangersluke@gmail.com",
    description="A small example package named eloquently used for learning python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lsprangers/cup_a_code",
    project_urls={
        "Bug Tracker": "https://github.com/lsprangers/cup_a_code/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "nlp_brew"},
    packages=setuptools.find_packages(where="nlp_brew"),
    install_requires=[
        "transformers>=4.4.2",
        "keras",
        "tensorflow>=2.0",
        "tensorflow-hub>=0.11.0",
        "gensim==4.0.0",
        "praw>=7.2.1",
        "python-dotenv>=0.15.0",
        "numpy>=1.19.2",
        "pandas>=1.2.3",
    ],
    python_requires=">=3.7",
)
