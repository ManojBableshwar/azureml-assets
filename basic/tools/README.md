## README generator for AzureML components

`component_readme.py` can generate a friendly README file in markdown format using the `description`, `inputs`, `outputs` and `comments` from the component YAML file. 

### Usage
```
> python component_readme.py --component  <path to component yaml>
```

### Output
`README.md` file in the same folder as the component yaml file. Make sure you backup any existing `README.md` files before running this script. 

### Example
Sample README.md for [./example/spec.yml`](./example/spec.yml). Output: [./example/README.md](./example/README.md)
```
> python component_readme.py --component ./example/spec.yml
```

### Dependencies
* [ruamel.yaml](https://pypi.org/project/ruamel.yaml/) for parsing the component YAML
* [SnakeMD](https://pypi.org/project/SnakeMD/) for generating markdown


