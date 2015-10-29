# coding:utf-8

from setuptools import setup
setup(
    name="kkblog",
    version="1.0",  # don't change this, the version used when deploy by sdist
    description="kkblog",
    author="guyskk",
    author_email="1316792450@qq.com",
    url="https://github.com/guyskk/kkblog",
    license="MIT",
    packages=["kkblog", "kkblog.model", "kkblog.config"],
    py_modules=["manage"],
    scripts=['manage.py'],
    install_requires=[
        'flask>=0.10.1',
        'markupsafe>=0.23',
        'pyjwt>=1.4',
        "flask-restaction>=0.17.5",
        "flask-cors>=2.0",
        "flask-cache>=0.13.0",
        "markdown>=2.6",
        "pony>=0.6.1",
        "pyquery>=1.2",
        "pygitutil>=0.0.5",
        "flask-mail>=0.9.1",
    ],
    dependency_links=[
        # "https://github.com/mitsuhiko/flask/tarball/master",
        # "https://github.com/ponyorm/pony/tarball/master",
    ],
    include_package_data=True,
    zip_safe=False,
)
