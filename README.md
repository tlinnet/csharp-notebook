# csharp-notebook [![Build Status](https://travis-ci.com/tlinnet/csharp-notebook.svg?branch=master)](https://travis-ci.com/tlinnet/csharp-notebook)

csharp-notebook is a [community maintained Jupyter Docker Stack image](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#community-stacks). It makes i possible to try C# in Jupyter Notebooks.

# Launch on mybinder

Try the Jupyter Notebooks out online with this link. No installation needed. It up to 5 min to prepare the image.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tlinnet/csharp-notebook/master) [mybinder.org/v2/gh/tlinnet/csharp-notebook/master](https://mybinder.org/v2/gh/tlinnet/csharp-notebook/master)

# Examples of Jupyter Notebooks

Additional material is more than welcome! Please add by a [GitHub Pull Requests.](https://help.github.com/articles/proposing-changes-to-your-work-with-pull-requests/)

## Exam Ref 70-483 Programming in C#, 2nd Edition

* [Microsoft Exam 70-483: Programming in C#.](https://www.microsoft.com/en-us/learning/exam-70-483.aspx)
* Book: "**Exam Ref 70-483 Programming in C#, 2nd Edition**" by Rob Miles
* Sample code at [github.com/ExamRef70-483/Sample-Code](https://github.com/ExamRef70-483/Sample-Code)

[The sample code has been converted to more than **200** Jupyter Notebooks.](Exam_Ref_70-483_Programming_in_C%23_2nd_Edition)

# Docker Hub

* Docker Hub [hub.docker.com/r/tlinnet/csharp-notebook](https://hub.docker.com/r/tlinnet/csharp-notebook)

Docker Pull Command for Docker image with **C# kernel** installed and example Notebooks.
```
docker pull tlinnet/csharp-notebook:notebooks
```

Docker Pull Command for Docker image with **C# kernel** installed with no Notebooks.
```
docker pull tlinnet/csharp-notebook
```

# GitHub

* GitHub [github.com/tlinnet/csharp-notebook](https://github.com/tlinnet/csharp-notebook)

Git Pull Command, manual Docker build and run on Windows 10.
```
git clone https://github.com/tlinnet/csharp-notebook.git
cd csharp-notebook
.\notebooks_build.cmd
.\notebooks_run.cmd
```

# References

## iCsharp kernel
This Dockerfile is made possible by the work of https://github.com/zabirauf/icsharp

Install guides from
* https://github.com/zabirauf/icsharp/wiki/Install-on-Unix-(Debian-7.8)
* https://github.com/3Dcube/docker-jupyter-icsharp/blob/master/Dockerfile

## Jupyter Docker Stacks - Community Stack version
This project is developed with the helpful guide of [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/). The base container is **jupyter/minimal-notebook** and this **Community Stack** is setup [via the guide.](https://jupyter-docker-stacks.readthedocs.io/en/latest/contributing/stacks.html)

The setup has been slightly modified from the standard cookiecutter settings.

* **[cloud.docker.com](https://cloud.docker.com)**
  * Builds -> Configure Automated Builds
    * AUTOTEST : Off
    * REPOSITORY LINKS : Enable for Base Image
    * **Build rules:**
      * Source: master
      * Docker Tag: latest
      * Dockerfile location : Dockerfile_build
      * Build Context : **/travis-ci**
      * Autobuild : On
      * Build Caching: On
  * Uses [**/travis-ci**/hooks/post_push](/travis-ci/hooks/post_push) (See setting for Build Context location)


* **[travis-ci.com](https://travis-ci.com/)**
  * General
    * Build pushed branches : On
    * Build pushed pull requests : On
    * Limit concurrent jobs : Off
  * Auto cancellation
    * Auto cancel branch builds : Off
    * Auto cancel pull request builds : Off


## Known issues in C# Jupyter Notebooks

* **Main()** is not called automatically. Has to be called manual. Remember '**public**' in the function definition.
* **Console.ReadKey()** should not be used.
* **using static System.Math;**  When importing Math, **static** has to included in the using command
