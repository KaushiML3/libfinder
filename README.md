# libfinder

`libfinder` is a simple Python package that helps check if a library is installed in your environment.

## 📌 Installation

Clone the repository and install:

```bash
git clone https://github.com/KaushiML3/libfinder
cd libfinder
pip install .

```

## Uses

common step
 - pip install libfinder

1. Call the functions
    - import libfinder  

    1. Get the module names
        - lib_name=libfinder.get_lib_name() **or** libfinder.get_lib_name()
        - print(lib_name)

    2. Get the module versions and save the new_requirements.txt file
        - lib_ver=libfinder.get_lib_ver() **or** libfinder.get_lib_ver()
        - print(lib_ver)

2. Use libfinder class  
     ```python
      import libfinder
      ```

    1. Create object
        - lib=libfinder.libraryfinder()

    2. Get the module names
        - lib.get_lib_name()

    3. Get the module versions
        - lib.get_lib_ver()

    4. Get the .txt file 
        - li.to_txt("new_requirements.txt")

3. params
   
     ![image](https://github.com/KaushiML3/libfinder/blob/main/img/Screenshot%20(82).png)







