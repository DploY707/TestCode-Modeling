# testCode-Modeling
Project for [testCode-Modeling] software

# How to install this project
1. $ cd [root directory of this project]
2. $ docker build -t tcm ./

<!--
# How to Use it
1. Move your APK that want you to analyze to [./data] directory
   (in this case, your APK name should not have whitespace (' ') !!)
2. $ docker run -it --rm -v [host APK directory path]:/root/workDir/data android-analyzer
3. Open another terminal to extract log file from docker container
   $ docker cp [CONTAINER_ID]:/root/results/methodLists/ [host_dir_path_to_save_extracted_data]
-->
