ARG BASE_CONTAINER=tlinnet/csharp-notebook
FROM $BASE_CONTAINER

ADD "Example_Jupyter_Notebook_with_C#.ipynb" $HOME
ADD Exam_Ref_70-483_Programming_in_C#_2nd_Edition $HOME/Exam_Ref_70-483_Programming_in_C#_2nd_Edition
