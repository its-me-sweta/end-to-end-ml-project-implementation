import setuptools

with open("README.MD","r" , encoding = "utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = "end-to-end-ml-project-implementation"
AUTHOR_USER_NAME = "its-me-sweta"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "swetajha1096@gmail.com"


setuptools.setup(
    name  = SRC_REPO,
    version = _version_,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for ml app",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
     project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"" : "src"},
    packages = setuptools.find_packages(where = "src")
)