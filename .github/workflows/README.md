# Workflow lessons

See [Writing Workflows](https://docs.github.com/en/actions/how-tos/write-workflows) for general details.

There are some "cookbook" style workflows, but in essence (and because I forget):

- Workflows are YAML specified, short tasks that get run on [an event](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow). This is expressed in the `on:` condition.

- Workflows that are exclusively part of a PR may not be run. Only workflows that land in `main` will be executed. Workflows that are altered in a PR _may_ be run in altered form.

- The event may or may not have a payload. The payload is a node/json object and will be specific to the type of action it's associated with.

- Each script can have one or more `jobs`, which may have one or more `steps`

- each `job` and `step` may have their own conditionals which can act on the payload content to determine if the job or step gets executed.

- there's no concept of `@latest` or `@stable`, so you have to [dig around](https://github.com/actions) to find the latest version of a given action.
