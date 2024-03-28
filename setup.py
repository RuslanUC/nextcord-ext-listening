from setuptools import setup
import re


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('nextcord/ext/listening/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess

        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass

readme = ''
with open('README.md') as f:
    readme = f.read()

packages = [
    "nextcord.ext.listening"
]

setup(
    name="nextcord-ext-listening",
    author="Sheppsu",
    url="https://github.com/RuslanUC/nextcord-ext-listening",
    project_urls={
        # TODO
    },
    version=version,
    packages=packages,
    license="MIT",
    description="Voice receive extension for nextcord built on multiprocessing and designed to be flexible (port of Sheppsu/discord-ext-listening).",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requirements=requirements,
    python_requires=">=3.8.0",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Capture/Recording"
    ]
)
