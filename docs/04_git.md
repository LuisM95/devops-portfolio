# Git Documentation

## What is Git
Version control system, which keeps a complete history of change to a project.
It is a tool that allows you work in teams without spoiling the work of other team members.

## Essencial Commands
``` BASH 
~ git init                             #Initialize a repository
~ git add . | git add <name_file>      #add changes to the stagging area
~ git commit -m                        #save the changes with a message
~ git push origin <branch>             #upload changes to a remote repository 
~ git pull                             #download changes from a remote repository 
~ git status                           #show the current status
~ git log --oneline                    #show the history of commmits
~ git branch                           #list the branches
~ git checkout -b <branch_name>        #create and switch to a new branch
~ git merge                            #merge branches 
~ git stash                            #temporarily sabe changes
```

## GitFlow - Types of branches
```
main          ->  Code in production, always stable
develop       ->  Integrations features
feature/*     ->  News Features 
hotfix/*      ->  Urgent corrections in production
release/*     ->  Release a new feature
```

## Conventional Commits
```
~ feat(scope): description   ->  New feture
~ fix(scope): description    ->  Bug correction
~ docs(scope): description   ->  Documentation
~ chore(scope): description  ->  Maintenance tasks
```

### Pull Request:
Formal request to merge one branch with another. Allows code review before moving. It is the standard flow in professional teams.

