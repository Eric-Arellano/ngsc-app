# Deploy / Heroku guide

That is, how we get the code from GitHub -> actual server (Heroku) people reach at ngsc-app.org.

## What is Heroku

Heroku manages our server for us. It's a Platform-as-a-Service (PaaS) that greatly simplifies the deployment process and things like setting up HTTPS.

## How to deploy

`./ngsc deploy`

### What is this actually doing

1. Checking that you have the most up-to-date version of master from GitHub, and that you have no uncommitted changes.
2. Pushing to the heroku git remote: `TODO find the link`

That's it! The way you deploy is just pushing to Heroku's git instance.

## Buildpacks

We did, however, have to initially tell Heroku how to build our project. We do this through "buildpacks", which are programs Heroku and the community offer to build your project for you.

We're using two buildpacks: Python and Create React App. The order of these matters.

If you need to change any of this, use Heroku's CLI and refer to TODO find the link

## Procfile

We also have to tell Heroku what to do once it's done building the app, which we define in the Procfile. This says to start up gunicorn (a Python web server for production), aka the Flask server.

While this config we have now works, there 100% may be a better alternative, so feel free to experiment.


### Potential improvement: Heroku.yml

Heroku has a beta feature to move all config into a Heroku.yml file. If you're adventerous, you can try to migrate us to this format. It looks far better. Refer to TODO find the link 

## Potential improvement: Add Staging environemnt

Right now, you can only push immediately to production, which is slightly problematic because prod doesn't always look like local development, so you can break production. It would be better to add a staging environment.

To do this, you would in Heroku's web dashboard create a new app called `ngsc-staging` and then modify the `ngsc` scripts like `deploy.py` to have the commands `./ngsc deploy-prod` and `./ngsc deploy-staging`.

## Heroku account & credentials
(Eric)

Create a Heroku account

Add as a collaborator

## HTTPS/SSL Setup
(Eric)

## Domain Name Management
(Eric)
