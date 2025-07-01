# Module 1 First-Time Software Installation

## Hardware Requirements
- Desktop/laptop computer running the latest version of macOS/Linux/Windows operating system (OS)
- Recommended 16GB onboard memory (RAM) 
- Recommended 50GB available hard disk storage space (HDD/SSD)
- Webcam and microphone for online Zoom sessions

## Software Requirements

- WSL (for Windows users only)
- Visual Studio Code (VSCode) or any source code editor
- Git Command-Line Interface (CLI)
- Conda/Miniconda
- DBeaver database viewer

## WSL for Windows

### *For Windows users only* - Windows Subsystem for Linux (WSL)

Windows users should install WSL which allows you to run Windows and Linux at the same time on a Windows machine. WSL allows you to install a Linux distribution (e.g. Ubuntu, OpenSUSE, Kali, Debian, etc.) and use Linux applications and utilities such as command-line (CLI) tools. 

Most software engineering and development tools are initially developed for Linux and then adapted for Windows. As a result, they often perform better on Linux. Although Windows versions of popular tools are widely available, we strongly recommend using the Linux version whenever possible for optimal performance.
You must be running Windows 11 or 10 version 2004 and higher. 

Follow the instructions [here](https://learn.microsoft.com/en-us/windows/wsl/install) to install Ubuntu on WSL.

You can access your WSL files using regular Windows applications, such as File Explorer. While you in your Linux directory, type: 

`explorer.exe .`

Read this [tutorial](https://learn.microsoft.com/en-us/windows/wsl/filesystems) to find out how it works.

## Visual Studio Code (VSCode)

You will need a code editor to write Python or SQL code in the course. VSCode is a popular source code editor used by developers for writing, debugging and editing code across various programminng languages. 

Download and install VSCode [here](https://code.visualstudio.com/download).

### Install the following vscode extensions

Go to the `Extensions` tab, search for the following extensions in the marketplace and install them:

- Python
- Jupyter

> Windows WSL users, install the Windows version as VSCode will work across both Windows and WSL environments.

## Git vs GitHub

Git and GitHub are two essential tools in software engineering. Git is a version control system that helps developers track changes in their code locally. GitHub is a web-based platform where developers can store and share their Git projects, facilitating collaboration and code management. Together, they enable a workflow where developers work on code locally with Git and then share it on GitHub for others to see, review, and contribute. This combination supports efficient collaboration, version control, and project management, making it indispensable for modern software engineering teams.

## Git CLI

We will be using Git extensively in this course and you will need to install the command line interface (CLI) application on your computer.

### Download and install Git CLI [here](https://git-scm.com/downloads).

Windows WSL users, read and follow the steps in this tutorial [Get Started using Git on WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git). *You may ignore the Azure setup.*



## Conda/Miniconda

Conda is a package and environment manager that we will be using throughout this program, to manage our Python packages and environments. Miniconda is a lightweight version of the Anaconda distribution, designed for users who prefer a minimal installation. It includes only the essentials: Python, conda (the package and environment manager), and their dependencies. Unlike Anaconda, which comes preloaded with hundreds of scientific packages, Miniconda allows you to install only the packages you need, making it more flexible and less resource-intensive.

### Download and install miniconda [here](https://www.anaconda.com/docs/getting-started/miniconda/main)

> Windows WSL users, please follow instructions for Linux/Unix

## DBeaver

We will be using DBeaver SQL client throughout this course to connect to databases and write SQL code. The free version is called DBeaver Community 

Download and install DBeaver Community [here](https://dbeaver.io/download/).

Windows WSL users are able to run the regular Windows version of DBeaver and access the database files stored in the WSL file system.

