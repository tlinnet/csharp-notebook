# csharp-notebook [![Build Status](https://travis-ci.com/tlinnet/csharp-notebook.svg?branch=master)](https://travis-ci.com/tlinnet/csharp-notebook)

csharp-notebook is a community maintained Jupyter Docker Stack image. It makes i possible to try C# in Jupyter Notebooks.

# Launch on mybinder

Try the Jupyter Notebooks out online with this link. No installation needed.

* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tlinnet/csharp-notebook/master) [mybinder.org/v2/gh/tlinnet/csharp-notebook/master](https://mybinder.org/v2/gh/tlinnet/csharp-notebook/master)

# Examples of Jupyter Notebooks

## Exam Ref 70-483 Programming in C#, 2nd Edition

* [Microsoft Exam 70-483: Programming in C#.](https://www.microsoft.com/en-us/learning/exam-70-483.aspx)
* Book: "**Exam Ref 70-483 Programming in C#, 2nd Edition**" by Rob Miles
* Sample code at [github.com/ExamRef70-483/Sample-Code](https://github.com/ExamRef70-483/Sample-Code)

The sample code has been converted to Jupyter Notebooks

# Links to GitHub and Docker Hub

* GitHub [github.com/tlinnet/csharp-notebook](https://github.com/tlinnet/csharp-notebook)

Git Pull Command, Docker build and run
```
git clone https://github.com/tlinnet/csharp-notebook.git
cd csharp-notebook
notebooks_build.cmd
notebooks_run.cmd
```

* Docker Hub [hub.docker.com/r/tlinnet/csharp-notebook](https://hub.docker.com/r/tlinnet/csharp-notebook)

Docker Pull Command
```
docker pull tlinnet/csharp-notebook
```

# References

This Dockerfile is made possible by the work of https://github.com/zabirauf/icsharp

Install guides from
* https://github.com/zabirauf/icsharp/wiki/Install-on-Unix-(Debian-7.8)
* https://github.com/3Dcube/docker-jupyter-icsharp/blob/master/Dockerfile

## Known issues

* **Main()** is not called automatically. Has to be called manual. Remember '**public**' in the function definition.
* **Console.ReadKey()** should not be used.
* **using static System.Math;**  When importing Math, **static** has to included in the using command
