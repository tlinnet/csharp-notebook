docker run --rm -p 8888:8888 -v "%CD%":/home/jovyan/work --name csharp tlinnet/csharp-notebook:notebooks
echo "Copy the secret token from the cmd window"
echo "Visit http://localhost:8888"
cmd /k