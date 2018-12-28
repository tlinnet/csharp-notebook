ARG BASE_CONTAINER=tlinnet/csharp-notebook
FROM $BASE_CONTAINER

USER root

ADD "README.md" $HOME
ADD "Example_Jupyter_Notebook_with_C#.ipynb" $HOME
ADD Exam_Ref_70-483_Programming_in_C#_2nd_Edition $HOME/Exam_Ref_70-483_Programming_in_C#_2nd_Edition

ADD "dev/convert_md_to_ipynb.py" $HOME/dev/convert_md_to_ipynb.py
RUN echo "Change mod and convert" && \
  cd $HOME && \
  echo $PWD && \
  fix-permissions README.md && \
  fix-permissions Exam_Ref_70-483_Programming_in_C#_2nd_Edition && \
  cd $HOME/dev && \
  python convert_md_to_ipynb.py && \
  cd $HOME && \
  rm -rf dev && \
  find . -type f -name "*.md" -exec rm -f {} \;

USER $NB_USER
