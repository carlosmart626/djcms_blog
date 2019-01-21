
# Simple Django Blog

Simple Django Blog app using Markdown

* Free software: MIT license
* Documentation: https://djcms-blog.readthedocs.io.


## Features

* Works on pure Django
* Markdown blog post format
* Built-in template

## Contributing
Install dev dependencies
```
pip install -r requirements_dev.txt
```
Run tests
```
pytest . --cov=. --cov-report=term-missing
```
Static Analysis
```
flake8 .
```

## Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
