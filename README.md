# csharp-notebook

csharp-notebook is a community maintained Jupyter Docker Stack image. It makes i possible to try C# in Jupyter Notebooks.

It includes a few Jupyter Notebooks to try it out.

# Launch on mybinder

* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tlinnet/csharp-notebook/master)

# References

This Dockerfile is made possible by the work of https://github.com/zabirauf/icsharp

Install guides from
* https://github.com/zabirauf/icsharp/wiki/Install-on-Unix-(Debian-7.8)
* https://github.com/3Dcube/docker-jupyter-icsharp/blob/master/Dockerfile

## Known issues

* Console.WriteLine() seems not to work properly always
* using System.Math;  seems to break printing to console. 