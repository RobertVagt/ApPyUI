import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ApPyUI", # Replace with your own username
    version="0.0.1",
    author="Robert Vagt",
    author_email="64617646+RobertVagt@users.noreply.github.com",
    description="A Python library for UI-focused applications, based on TkInter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RobertVagt/ApPyUI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)