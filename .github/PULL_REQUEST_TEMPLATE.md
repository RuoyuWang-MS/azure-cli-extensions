---

This checklist is used to make sure that common guidelines for a pull request are followed.

### Related command
<!--- Please provide the related command with az {command} if you can, so that we can quickly route to the related person to review. --->


### General Guidelines

- [ ] Have you run `azdev style <YOUR_EXT>` locally? (`pip install azdev` required)
- [ ] Have you run `python scripts/ci/test_index.py -q` locally?

For new extensions:

- [ ] My extension description/summary conforms to the [Extension Summary Guidelines](https://github.com/Azure/azure-cli/blob/dev/doc/extensions/extension_summary_guidelines.md).


### About Extension Publish

There is a pipeline to automatically build, upload and publish extension wheels.  
Once your pull request is merged into main branch, a new pull request will be created to update `src/index.json` automatically.  
The precondition is to put your code inside this repository and upgrade the version in the pull request but do not modify `src/index.json`. 
