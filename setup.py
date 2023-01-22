from setuptools import setup

setup(
    name="Biking-Berlin",
    version="0.1.0",
    description="Little side scroller where you bike Berlin",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/debsdebsenson/Biking-Berlin",
    author="Deborah Sobiella",
    author_email="dsobiella@posteo.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["biking_berlin"],
    include_package_data=True,
    install_requires=[
        "pygame", "matplotlib", "numpy"
    ],
    entry_points={"console_scripts": ["debsdebsenson=biking_berlin.__main__:main"]},
)
