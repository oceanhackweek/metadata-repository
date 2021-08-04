# Connecting Data Repositories

Project Goal: Connect ocean data repositories around the world by connecting their metadata 

## Workflow 

To contribute to this project, view the current issues (or create a new one), clone the repo on your machine, create a branch for that issue, commit your changes to that branch, and create a pull request for your changes. Detailed steps outlined below: 

- View issues: In GitHub, click on the "Issues" tab.  From here, you can view, create, or make comments on issues. 
- Clone the repo (Only do this once!): From the "Code" tab in GitHub, click the green button ("Code") and copy the HTTPS URL it gives you. Open the terminal on your machine and type `git clone *repo URL` 
- In your machine, navigate to the repo folder (`cd metadata-repository`)
- Create a branch: `git checkout -b mybranchname` (replace mybranchname with the name of the branch - I recommend naming it after the issue you are working on)
- Check that you are working on the branch (NOT main): `git status` should return `on branch: mybranchname`. (If you are still on branch: main, type `git checkout mybranchname`
- Add branch upstream (Only do this once per new branch): `git --set-upstream origin mybranchname`
- Make your changes, add them (`git add yourfilename`), and commit (`git commit -m "With this commit, I....DESCRIBE CHANGES HERE"`)
- Pull (ALWAYS PULL before you PUSH): `git pull`
- Push: `git push`
- Create pull request: In GitHub, go to 'pull requests' tab. There should be a message about your branch needing a pull request. Click that button and submit the request. An administrator of the repo will review and approve requests.
- Update your machine: once your pull request is approved, run `git pull` to update your local repo's main branch. You may delete your personal branch on GitHub - ("Code" - "Branches" - Delete branch) 
