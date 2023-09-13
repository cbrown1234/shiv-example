# Shiv Example

An example application built with shiv and hatch

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Setup

- Initialise the project with `hatch`:

```shell
pip install --upgrade pip pip-tools hatch
hatch new "Shiv Example"
cd shiv-example
```

- Add core requirements to the `pyproject.toml` in the `dependencies` list
- Add dev dependencies to the `pyproject.toml` in the `dev` list within the 
`[project.optional-dependencies]` section
- Install the project dependencies:

```shell
pip-compile -o requirements.txt pyproject.toml
pip-compile --extra=dev -o requirements-dev.txt pyproject.toml
pip install -r requirements.txt # if you only need to run the app
pip install -r requirements.txt -r requirements-dev.txt # if you need to build the app
```

- Write the app in the src directory
- Add the console script to the `pyproject.toml` file

```toml
[project.scripts]
shiv-example-app = "shiv_example.main:main"
```

- Build the application with `shiv` 

```shell
shiv -c shiv-example-app -o shiv-example-app .
```

- Run the app like so:

```shell
./shiv-example-app
```

## License

`shiv-example` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
