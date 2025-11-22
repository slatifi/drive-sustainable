# CI Exercise

Now that we have some tests written for our `Basket` service, let's set up Continuous Integration (CI) to automatically run these tests on every push to our repository.

### Instructions

1. **Create a GitHub Actions Workflow**:
   - In your repository, navigate to a directory called `.github/workflows`.
   - Inside this directory, create a new file named `ci.yml`.
2. **Define the workflow**: Copy the template below into your `ci.yml` file and add the following steps to run the tests:
   - Set up Python - use the `@actions/setup-python@2` action to specify the Python version.
   - Run the command `python3 -m unittest discover` to execute the tests within the `exercise` directory.

```yaml
name: CI

on: push

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

    # add the rest of the steps here
```
