# Mini-Lisp Interpreter

使用 **Python 3** 實作的輕量版 [Mini-Lisp Interpreter](https://github.com/cjh5958/mini-Lisp.git "Github")。

## 1. 功能

### Basic
- [x] Syntax Validation
- [x] Print
- [x] Numerical Operations
- [x] Logical Operations
- [x] if Expression
- [x] 定義變數 Variable Definition
- [x] 匿名函式 Function
- [x] 命名函式 Named Function
### Bonus
- [x] 遞迴 Recursion
- [x] 型別確認 Type Checking
- [x] 巢狀函式 Nested Function
- [x] 一級函式 First-Class Function

## 2. 系統要求  <a name = "system_requirement"></a>

* OS: Windows10+, Unix System (MacOS & Linux)
* Python: 3.10+
* Bash (Windows用戶可以使用 **git bash**)

## 3. 如何開始 <a name = "getting_started"></a>

1. 在終端機內使用 `cd` 指令移動到你想儲存專案的資料夾內，複製遠端 git repository
```bash
cd /usr/example/
git clone https://github.com/cjh5958/mini-Lisp.git
cd ./mini-Lisp
```

2. 確認 `config.py` 正確無誤，使用 `DEBUG_MODE` 控制是否開啟 Debug 模式

3. 使用以下指令開始撰寫你的 Mini-Lisp 程式
```bash
python3 lis.py
```

4. 當完成撰寫後，輸入 `EOF` 告訴 Interpreter 可以開始執行程式了
Windows: `ctrl` + `z`
MacOS & Linux: `ctrl` + `d`

5. 順利的話應該就能看到你的程式執行結果了！
6. 當然你也可以使用外部檔案作為程式的輸入方式，只需要使用指令
```bash
python3 lis.py < MYFILE.lsp
```

## 4. 測試 <a name = "testing"></a>

在 Bash 環境下可以使用自動測試腳本。

首先，在 `testcases` 資料夾下新增一個 .lsp 檔案 `mylsp.lsp`，使用文字編輯器打開 `mylsp.lsp` 輸入你的測試程式碼後存檔，或是使用以下指令輸入測試程式：
```bash
echo YOUR_CODE_HERE > ./testcases/mylsp.lsp
```
然後在 `testcases/answers.txt` 中，新增
```
mylsp.lsp
MY_ANSWER_HERE
```
最後使用
```bash
bash run_test.sh
```
就可以看到所有測試結果了！

## 5. 專案結構 <a name = "file_structure"></a>

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