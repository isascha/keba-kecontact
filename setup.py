import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keba_kecontact",
    version="3.0.3i",
    author="Philipp Danner",
    author_email="philipp@danner-web.de",
    description="A python library to communicate with the KEBA charging stations via udp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isascha/keba-kecontact",
    packages=setuptools.find_packages(),
    install_requires=["asyncio_dgram>=2.1.1", "netifaces>=0.11.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
