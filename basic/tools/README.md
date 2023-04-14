## README generator for AzureML components

`component_readme.py` can generate a friendly README file in markdown format using the `description`, `inputs`, `outputs` and `comments` from the component YAML file. 

### Doc layout
* Name, display name, version and description in the intro section.
* Inputs section with detailed information about inputs. Any comment added in between different inputs will be consider a group. The comment will be used as group heading and rest of the inputs will follow in table format. When a new comment is found, a new sub-section under Inputs is initialized. Example, Lora parameters and training parameters for the finetuning components are different groups. 
* Outputs section.
* todo: add support for samples. 

### Guidance
* Clearly explain what the component does and in what context it has to be used in description. Make sure you explain that pipeline components are suggested to be used over individual command components. Link the the relevant pipeline component for the command components so that users know how to use the command component for e2e task.
* Its strongly recommend to group related inputs together. Provide sufficient context for technical terms such as LORA, ONNX, DEEPSPEED, etc. with links to wiki pages. 
* Individual input description should be comprehensive. Don't try to repeat what is already communicated by input name. 
* Bad example: parameter - `lora_dropout`. Description: `lora dropout value`. Explaining what are dropout values in 1-2 lines would help here. 


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


