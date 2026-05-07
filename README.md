# Mini-Lisp Interpreter

A lightweight Lisp interpreter implemented in Python 3.

## 1. Features

### Basic
- [x] Syntax Validation
- [x] Print
- [x] Arithmetic Operations
- [x] Logical Operations
- [x] `if` Expression
- [x] Variable Definition
- [x] Function
- [x] Named Function
### Bonus
- [x] Recursion
- [x] Type Checking
- [x] Nested Function
- [x] First-Class Function

## 2. Prerequisites  <a name = "system_requirement"></a>

* **Python**: 3.10 or higher
* **Shell**: Bash (or **Git Bash** for Windows)

## 3. How to start <a name = "getting_started"></a>

1. Clone this repo to wherever you want to run the program.
```bash
git clone https://github.com/cjh5958/mini-Lisp.git
```

2. Ensure `core/config.py` exists in the project directory.

3. Run the interpreter in interactive (CLI) mode:
```bash
python3 lis.py
```
4. To execute the code, signal EOF (Ctrl+D on most systems) after typing your program.

5. Alternatively, use a file stream to run a script:
```bash
python3 lis.py < MYFILE.lsp
```

## 4. Testing <a name = "testing"></a>

You can use the provided shell script to batch-test multiple `.lsp` files.

1. Create a new `.lsp` file (e.g., `mylsp.lsp`) in the `testcases` directory: 
```bash
nano ./testcases/mylsp.lsp
```
2. Add your code to the file and save it.

3. Add the expected output to ./testcases/answers.txt using the following format:
```
cat <<EOF >> ./testcases/answers.txt
mylsp.lsp
$MY_ANSWER_HERE
EOF
```
4. Run the automated test script:
```bash
bash run_test.sh
```

## 5. Project structure <a name = "file_structure"></a>

```
C:.
├─ .gitignore
├─ LICENSE
├─ lis.py               # entry point of the program
├─ README.md
├─ run_test.sh
├─ testcases/*
├─ tests/*
└─ core
   ├─ config.py         # configuration file
   ├─ environment.py    
   ├─ evaluator.py
   ├─ handler.py
   ├─ parser.py
   ├─ types.py
   └─ __init__.py
```

## 6. Reference <a name = "reference"></a>
1. [用 Python 寫一個精簡的 Lisp Interpreter](https://drakeguan.org/blog/2010/10/yong-python-xie-yi-ge-jing-jian-de-lisp-interpreter/)
2. [How to Write a (Lisp) Interpreter (in Python)](https://norvig.com/lispy.html)
