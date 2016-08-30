## Github_0: Getting Started
Getting started with github tutorials.

### Clone this repository
1 - Download and install the latest version of [GitHub Desktop](https://desktop.github.com/). This will automatically install `Git` and keep it up-to-date for you.

2 - Open a command prompt (terminal) and navigate to where you want to clone (i.e. make a copy of) this repository (`ex: C:\git`).

3 - Issue the command: `git clone https://github.com/elmimouni/tutorials.git`. Navigate now to C:\git and you will notice that a folder named `tutorials` was created. Look inside, tadaaa! It contains the same files in github.

4 - Once there you can create as many files and folders as you want, you can use your favorite text editor (I use Atom or Sublime Text). As a test, create a file `Readme-<YOUR-NAME-HERE>.txt` and type some text (Hello, I am <your-name> and this is my first commit.) inside, then issue the command: `git add Readme-<YOUR-NAME-HERE>.txt` (in my case, `git add Readme-Omar.txt`).

5 - When you create a file/folder inside the repository, it remains on your local machine, you need to commit and push(i.e. save) it to this repository. What the command `git add <file>` does is that it includes the files you want to commit to your remote repository (NB: by remote I mean github, and by local I mean your machine/laptop/PC). To see the files that need to be included, issue the command `git status`.

6 - Now, let's commit our file. To do so, issue the command: `git commit -m “Add <your-filename>”` (in my case it will be `git commit -m Add Readme-omar.txt`). What comes after `-m` is just a message that describes your operation. Github is a platform to manage and share code. So, another member of your team might need to know what is the commit about (NB: always use present tense, it is about what a commit *does* not what a commit *did*!)

7 - Until now, your file is still on your local machine, if you go to the [repository](https://github.com/elmimouni/tutorials), you will notice that the file is not there yet. And again, you can use the command `git status` to see what is going on, what are the files that need to be pushed. What we need to do next is to push the commit to Github. But before to do that, we need to connect our local repository (the one on our machine) to the remote repository (the one on Github servers). To do so, issue the command: `git remote add origin https://github.com/elmimouni/tutorials.git`. Here, `git remote add` is the same as `git add` the only difference this time is that, we are telling github that we want to add to a remote repository not our machine but somewhere onlin, and `origin https://github.com/elmimouni/tutorials.git` specifies the location of our remote repository. You can use the command `git remote -v` to check that Git has an idea about the remote repository. So far, there should be only one!

8 - Notice that when you type the command `git remote add origin https://github.com/elmimouni/tutorials.git` you will have an error saying: **fatal: remote origin already exists.**. This means that our local and remote repositories are already connected, all we need to do is push the commit.

9 - Now, issue `git push`. You will be asked to provide your credentials. Make sure you have a Github account and that you are granted access by the owner of this repository. All repositories are read-only for anonymous users. By default, only the owner of the repository has write access. If you want to grant someone else privileges to push to your repository, you will need to add them as collaborators to your repository.

10 - You can use Github Desktop to manage your repository, but also you can use the shell or command line to do that. Here is a [Cheat Sheet](https://services.github.com/kit/downloads/github-git-cheat-sheet.pdf) for the git protocol.


### recap of commands used

NB: I assume that git is already installed on your machine.

```
    C:\git\tutorials> git clone https://github.com/elmimouni/tutorials.git
    C:\git\tutorials> echo 'Hello! I am Omar and this is my first commit.' > Readme-Omar.txt
    C:\git\tutorials> git add Readme-Omar.txt
    C:\git\tutorials> git commit -m Add Readme-Omar.txt
    C:\git\tutorials> git remote add origin https://github.com/elmimouni/tutorials.git (Jump this if already configured)
    C:\git\tutorials> git push
    ...enter credentials and go check Github!
```