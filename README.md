# Equivalent-Commands

UNIX-based and windows system equivalent commands.

I will be adding many more commands.

> **NOTE**: I'm mainly focusing on command prompt on windows.

## UNIX

<details>
  <summary><code>cat</code> command</summary>
  <br />

  ```batch
    :: `cat` command is `type` on windows.

    type file.txt
  ```
</details>

<details>
  <summary><code>grep</code> command</summary>
  <br />

  ```batch
    :: `grep` command is `findstr` (Command Prompt) on windows.

    findstr "foo"
  ```

  ```powershell
    # `grep` command is `Select-String` (PowerShell) on windows.

    Select-String "foo"
  ```
</details>

<details>
  <summary><code>less</code> command</summary>
  <br />

  ```batch
    :: `less` command is equivalent to `more` command on windows, but `less` is more powerful.
    :: you can install `less` on windows, but `more` is on by default.

    more
  ```
</details>

<details>
  <summary><code>clear</code> command</summary>
  <br />

  ```batch
    :: `clear` command is `cls` command on windows.
    :: `clear` command works on PowerShell as well.

    cls
  ```
</details>

<details>
  <summary><code>ls</code> command</summary>
  <br />

  ```batch
    :: `ls` command is `dir` command on windows.
    :: `ls` command works on PowerShell as well.

    dir
  ```
</details>

<details>
  <summary><code>rm</code> command</summary>
  <br />

  ```batch
    :: `rm` command is `del` command on windows.
    :: `rm` command works on PowerShell as well.

    del file.txt
  ```
</details>

<details>
  <summary><code>touch</code> command</summary>
  <br />

  ```batch
    :: `touch` command is `copy nul` or `type nul` command on windows.

    type nul >> "file.txt"
  ```

  ```batch
    :: Does not work on PowerShell.

    copy nul "file.txt"
  ```
</details>

## Windows

<details>
  <summary><code>type</code> command</summary>
  <br />

  ```bash
    # `type` command is `cat` on UNIX.

    cat file.txt
  ```
</details>

<details>
  <summary><code>findstr</code> command (Command Prompt) or <code>Select-String</code> command (PowerShell)</summary>
  <br />

  ```bash
    # `findstr` and `Select-String` command is grep on UNIX.

    grep "foo"
  ```
</details>

<details>
  <summary><code>more</code> command</summary>
  <br />

  ```bash
    # `more` command is equivalent to `less` command on UNIX, but it's not as powerful.
    # you can install `less` on windows.

    less
  ```
</details>

<details>
  <summary><code>cls</code> command</summary>
  <br />

  ```bash
    # `cls` command is `clear` command on UNIX.
    # `clear` command works on PowerShell as well.

    clear
  ```
</details>

<details>
  <summary><code>dir</code> command</summary>
  <br />

  ```bash
    # `dir` command is `ls` command on UNIX.

    ls
  ```
</details>

<details>
  <summary><code>del</code> command</summary>
  <br />

  ```bash
    # `del` command is `rm` command on UNIX.

    rm file.txt
  ```
</details>

<details>
  <summary><code>copy nul</code> and <code>type nul</code> command</summary>
  <br />

  ```bash
    # `copy nul` or `type nul` command is `touch` command on UNIX.

    touch file.txt
  ```
</details>
