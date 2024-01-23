# BKOOL

> This guide is for Debian distribution only (Ubuntu 22.04).

## 1. Prerequisites
- `python3` >= v3.10.12
- `javac` >= v11.0.21
- `antlr` = v4.9.2
  - Dowload [antlr-4.9.2-complete.jar](https://www.antlr.org/download/antlr-4.9.2-complete.jar).
  - Move into `/usr/local/lib`.
  - Add environment variable ANTLR_JAR into file `~/.profile` as follows:
    ```
    export ANTLR_JAR=/usr/local/lib/antlr-4.9.2-complete.jar
    ```
- `antlr4-python3-runtime` = v4.9.2, use the command:
    ```
    pip3 install antlr4-python3-runtime==4.9.2
    ```
To check if the installation was successful, follow these steps:
1. `cd src`: Change current directory where there is file run.py.
2. `python3 run.py gen`: Generate 7 files in `target/main/bkool/parser`.
3. Run test cases (all failed by default):
    ```
    python3 run.py test LexerSuite
    python3 run.py test ParserSuite
    python3 run.py test ASTGenSuite
    python3 run.py test CheckerSuite
    python3 run.py test CodeGenSuite
    ```
