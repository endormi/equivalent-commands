# Equivalent-Commands

UNIX-based and windows system equivalent commands.

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
    :: `less` command is equivalent to `more` command in windows, but `less` is more powerful.
    :: you can install `less` on windows, but `more` is on by default.

    more
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
