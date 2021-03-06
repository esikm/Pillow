# Contributing to Pillow2

Bug fixes, feature additions, tests, documentation and more can be contributed via [issues](https://github.com/python-pillow/Pillow2/issues) and/or [pull requests](https://github.com/python-pillow/Pillow2/pulls). All contributions are welcome.

## Bug fixes, feature additions, etc.

Please send a pull request to the master branch. Please include [documentation](https://pillow.readthedocs.io) and [tests](../Tests/README.rst) for new features. Tests or documentation without bug fixes or feature additions are welcome too. Feel free to ask questions [via issues](https://github.com/python-pillow/Pillow2/issues/new), [Gitter](https://gitter.im/python-pillow/Pillow2) or irc://irc.freenode.net#pil

- Fork the Pillow2 repository.
- Create a branch from master.
- Develop bug fixes, features, tests, etc.
- Run the test suite on Python 2.7 and 3.x. You can enable [Travis CI](https://travis-ci.org/profile/) and [AppVeyor](https://ci.appveyor.com/projects/new) on your repo to catch test failures prior to the pull request, and [Coveralls](https://coveralls.io/repos/new) to see if the changed code is covered by tests.
- Create a pull request to pull the changes from your branch to the Pillow2 master.

### Guidelines

- Separate code commits from reformatting commits.
- Provide tests for any newly added code.
- Follow PEP8.
- When committing only documentation changes please include [ci skip] in the commit message to avoid running tests on Travis-CI and AppVeyor.

## Reporting Issues

When reporting issues, please include code that reproduces the issue and whenever possible, an image that demonstrates the issue. Please upload images to GitHub, not to third-party file hosting sites. If necessary, add the image to a zip or tar archive.

The best reproductions are self-contained scripts with minimal dependencies. If you are using a framework such as plone, Django, or buildout, try to replicate the issue just using Pillow2.

### Provide details

- What did you do?
- What did you expect to happen?
- What actually happened?
- What versions of Pillow2 and Python are you using?

## Security vulnerabilities

To report sensitive vulnerability information, email security@python-pillow.org.

If your organisation/employer is a distributor of Pillow2 and would like advance notification of security-related bugs, please let us know your preferred contact method.
