from setuptools import setup, find_packages

setup(
    name="gfv",
    version="1.0.0",
    author="Ibrahem abo kila",
    author_email="ibrahemabokila@gmail.com",
    description="URL Vulnerability Checker Tool.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hemaabokila/gfv",
    packages=find_packages(),
    package_data={
        '': ['patterns/patterns.json'], 
        },
    install_requires=[
	    'colorama',
        'rich',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gfv=gf.main:main', 
        ],
    },
)

