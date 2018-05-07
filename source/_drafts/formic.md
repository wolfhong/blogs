---
title：A Python implementation of Ant FileSet and Globs.
---

[formic][bitbucket]是

A Python implementation of Ant FileSet and Globs.

Formic is about finding files, fast.

Formic uses globs. Match any character with ?, any word with * or any subdirectory at any level with **.

For complex queries, use one or more include globs to locate files, then refine the search with excludes. For example find all source files with src/**/*.py and then exclude all files used for testing using test*.

FileSets are optimized working on all includes and excludes simultaneously so searching for specific files is fast even in deeply nested directory trees

### 安装

    pip install formic


VCS = version control system

API. http://www.aviser.asia/formic/doc/api.html#module-formic.command

[bitbucket]: https://bitbucket.org/aviser/formic
[usage]: http://www.aviser.asia/formic/doc/usage.html
[official]: http://www.aviser.asia/formic/
[pypi]: https://pypi.org/project/formic/
