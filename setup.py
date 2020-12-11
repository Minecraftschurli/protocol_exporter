from os import path

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

name = "protocol_exporter"
setup(
    name=name,
    version="0.1",
    author="Minecraftschurli",
    author_email="minecraftschurli@gmail.com",
    description="A nbconvert exporter to convert to pdf with the TGM-Protocol template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/minecraftschurli/protocol-exporter",
    packages=[name],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_data={
        name: [
            path.join(name, 'templates', 'protocol.tex.j2'),
            path.join(name, 'templates', 'protocol.cls'),
            path.join(name, 'templates', 'images', 'logo-left.png'),
            path.join(name, 'templates', 'images', 'logo-right.png'),
            path.join('templates', 'protocol.tex.j2'),
            path.join('templates', 'protocol.cls'),
            path.join('templates', 'images', 'logo-left.png'),
            path.join('templates', 'images', 'logo-right.png'),
        ]
    },
    python_requires='>=3.6',
    entry_points={
        'nbconvert.exporters': [
            "protocol = %s:ProtocolExporter" % name
        ]
    }
)

