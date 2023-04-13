# nopip

A simple module to install Python packages programmatically, without needing to use `pip` to install `nopip`. Useful for quick scripts, testing, or when you want to embed all the requirements of your app into your code.

## Usage

Embed all the requirements of your app into your code for simplicity. You can even try importing packages and install them in case of an error:

```python
from nopip import install

try:
    from flask import Flask
except:
    install.module('Flask==2.2.3')
```

### Other examples

```python
install.from_requirements('./requirements.txt')
install.module('requests')
install.modules(['requests==2.5.1', 'beautifulsoup4==4.10.0'])
```

## Installation

There is no need to install `nopip` via `pip`. Simply copy the `nopip` directory to your project, and you're good to go.

If you find it challenging to copy the entire nopip directory, there's an even simpler solution. You can just copy the contents of the `__init__.py` file and save it as `nopip.py` in your project directory. This way, you can still access and use the nopip functionality with minimal setup.

# Note

I'd like to clarify that I don't hate `pip` or intend to undermine its value in the Python ecosystem. `pip` is an essential tool for managing Python packages and their dependencies. However, I have observed that some people, particularly beginners or those working on very simple applications, might face issues with `pip` when trying to set up their environment or resolve dependencies. The `nopip` module aims to provide an alternative way to install packages for those specific scenarios where ease of use is a priority. It's important to note that using `nopip` is not a substitute for proper dependency management, and it's always recommended to use `pip`, `pipenv`, or `poetry` for production code.


# Collaboration

We welcome and appreciate any contributions to improve the nopip module. If you have ideas, suggestions, or bug fixes, feel free to collaborate by following these steps:

 - Fork the repository on GitHub (assuming the project is hosted on GitHub).
 - Clone your fork locally.
 - Create a new branch for your proposed changes. For example, use git checkout -b feature/my-new-feature to create and switch to a new branch called feature/my-new-feature.
 - Make your changes in the new branch, and commit them with meaningful commit messages.
 - Push your changes to your fork on GitHub.
 - Open a pull request on the original repository, describing your proposed changes and why they would be beneficial.
 - We will review pull requests on a regular basis and provide feedback. If your changes are accepted, they will be merged into the main repository.

If you encounter any issues or have questions, feel free to open an issue on the GitHub repository, and we'll do our best to address it.

Let's work together to make `nopip` even better!