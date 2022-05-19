# Breathe

## Creating an environment

### Provisioning an instance

For Microsoft FTEs, provision a [Dynamics 365 Enterprise P1 Trial Instance](https://www.cwcwiki.com/wiki/Dynamics_for_CSE_Engagements#Trial_Instances) (Microsoft internal link).

Take note of the instance URL, admin username and password. Configure the password as a GitHub repository secret named `PASSWORD`.

For a more complete CI setup, you should create two instances, one for development (manually updated), and one for the CI build that is automatically provisioned. Use the same password in both instances.

### Deploying the solution

Adapt the values under `env` in [deploy.yaml](`.github/workflowsdeploy.yaml`) to your environment. From the GitHub Actions tab, run the `Deploy solution` workflow.

This sets up the solution based on the assets in the `src` directory, and populates data using the Postman collection in the `data` directory.

### Exporting the solution

After performing manual changes to the solution in Power Apps, run the `Export solution` workflow from the GitHub Actions tab to prepare a pull request to update the solution files in the  `src` folder on the `main` branch.

Check the run logs for the name of the created branch:

```
Run microsoft/powerplatform-actions/branch-solution@0.4.0
create-solution-pr:
... prepare staging branch
... stage solution into branch src-20220518-2113
... commit solution into src-20220518-2113 and push to https://github.com/OneWeekBreathe/Breathe
```

Create a pull request from that branch.

## Using Postman

[Set up your Postman environment for Dataverse](https://docs.microsoft.com/power-apps/developer/data-platform/webapi/setup-postman-environment).

Import the environment and collections in the `data` folder.

To support automation using `newman`, we have added an extra `token` environment variable containing the OAuth2 token.

In Postman, under the collection's Authorization tab, click `Get New Access Token`, `Proceed` and copy the token value into an environment variable named `token`.
