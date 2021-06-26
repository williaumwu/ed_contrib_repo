**Description**

  Demo for highlighting ED

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| show_version   | show_version                | string   | None         |
| required_fake_var   | required_fake_var                | string   | None         |
| required_fake_var_2   | required_fake_var_2                | string   | None         |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| optional_fake_var_1   | optional_fake_var_1                | string   | None         |
| optional_fake_var_2   | optional_fake_var_2                | string   | None         |

**Sample entry:**

```
infastruture:
  demo:
    stack_name: williaumwu:::hello_world_stack
    arguments:
      show_version: 24

```
