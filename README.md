# **Hepynet Workspace for $HH\rightarrow bbll$**

Workspace repository to do DNN studies with [**hepynet**](https://github.com/Hepynet/hepynet)

## **Setup**

Set up environment with [Conda](https://www.anaconda.com/)

  ```bash
  conda create -n hepynet python=3.8
  conda activate hepynet
  pip install hepynet
  ```

## **Preparations**

- **Prepare dataframes as inputs**

  - refer to root_io for examples

- **Prepare job config files**

  all config files are put under share folder, there are 3 types of config files you should prepare/modify

  - **cross_platform.pc_meta.yaml**

    You should set up the data folder (where you keep the input numpy arrays) in this file

  - **train configs**: configs for a model training job

  - **apply configs**: configs for a model applying job

  please refer to [config_preparing.md](docs/config_preparing.md) for more details

## **Usage**

```bash
usage: hepynet [-h] [-d] [-v] [yaml_configs]

positional arguments:
  yaml_configs

optional arguments:
  -h, --help     show this help message and exit
  -d, --debug    run in debug mode
  -v, --verbose  verbose debug infomation
```# hepynet_workspace_hhbbll
