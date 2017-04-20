# docs-common

Updating docs-common for carbon-io:

To update the docs-common submodule to the latest commit in carbon-io:

* Make your changes to docs-common and push them to the master branch (no tag).

* Make sure that any changes in your carbon-io repository are okay to be pushed.

```
cd to $PROJECT_ROOT/.git-cmds (carbon-io)
```

Run the update command for docs-common:

```
./git-update-common -v
```

The script will output the package.json with the new version of carbon-io. Make sure this is correct and press 'y'. Pressing 'n' will drop the changes and halt the update. The update script will fail if your carbon-io tree is out of date.