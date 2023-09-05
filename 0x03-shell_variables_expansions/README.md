Shell Expansions

**Command Substitution**
- Syntax: `$(command)` or `` `command` ``
- Example: Assign the result of the `date` command to a variable.
  ```bash
  current_date=$(date)
  ```

**Variable Expansion**
- Syntax: `${variable_name}`
- Example: Print a greeting message using a variable.
  ```bash
  name="John"
  echo "Hello, ${name}!"
  ```

**Arithmetic Expansion**
- Syntax: `((expression))`
- Example: Perform an arithmetic operation and store the result.
  ```bash
  result=$((5 + 3))
  ```

**Parameter Expansion**
- `${variable:-default}`: Use a default value if the variable is unset.
- `${variable:=default}`: Set the variable to a default value if unset.
- `${variable:+alternate}`: Use an alternate value if the variable is set.
- `${variable:?message}`: Display a message and exit if the variable is unset.
Shell Arithmetic

**Arithmetic Operations**
- Syntax: `$((expression))`
- Example: Calculate the sum of two numbers.
  ```bash
  result=$((5 + 3))
  ```
Shell Variables

**Variable Assignment**
- Syntax: `variable_name=value`
- Example: Assign a value to a variable.
  ```bash
  name="Alice"
  ```

**Accessing Variable**
- Syntax: `$variable_name`
- Example: Display the value of a variable.
  ```bash
  echo "Hello, $name!"
  ```

**Environment Variable**
- Variables available to all processes.

**Local Variable**
- Variables limited to the current shell.

**Read-only Variable**
- Syntax: `readonly variable_name=value`
- Example: Make a variable read-only.
  ```bash
  readonly pi=3.14
  ```

**Unsetting Variable**
- Syntax: `unset variable_name`
- Example: Remove a variable.
  ```bash
  unset name
  ```
Shell Initialization Files

**~/.bashrc**
- User-specific initialization file for Bash.

**~/.bash_profile**
- User-specific login shell initialization file for Bash.

**/etc/profile**
- System-wide initialization file for Bash.

**~/.bash_logout**
- User-specific logout file for Bash.

The `alias` Command

**Creating an Alias**
- Syntax: `alias alias_name='command'`
- Example: Create an alias for a long command.
  ```bash
  alias ll='ls -l'
  ```

**Listing Aliases**
- Syntax: `alias`
- Example: List all defined aliases.
  ```bash
  alias
  ```

**Removing an Alias**
- Syntax: `unalias alias_name`
- Example: Remove an alias.
  ```bash
  unalias ll
  ```
Technical Writing

**Technical Writing**
- The practice of creating clear and concise technical documents.
- Key Elements: Clarity, Audience Awareness, Use of Visuals, Conciseness, Correctness.
`man` and `help` Commands

**`man` Command**
- Syntax: `man command_name`
- Example: View the manual page for the `ls` command.
  ```bash
  man ls
  ```

**`help` Command**
- Syntax: `help command_name`
- Example: Get help for the `cd` shell built-in command.
  ```bash
  help cd
  ```

`printenv`, `set`, `unset`, `export`

**`printenv` Command**
- Syntax: `printenv`
- Example: Display all environment variables.
  ```bash
  printenv
  ```

**`set` Command**
- Syntax: `set`
- Example: Display all shell variables.
  ```bash
  set
  ```

**`unset` Command**
- Syntax: `unset variable_name`
- Example: Unset (remove) a variable.
  ```bash
  unset name
  ```

**`export` Command**
- Syntax: `export variable_name=value`
- Example: Set an environment variable.
  ```bash
  export PATH=/usr/local/bin:$PATH
  ```

`source` Command

**`source` Command**
- Syntax: `source filename`
- Example: Execute commands from a script in the current shell.
  ```bash
  source myscript.sh
  ```

`printf` Command

**`printf` Command**
- Syntax: `printf format [arguments]`
- Example: Format and print a message.
  ```bash
  printf "Hello, %s!\n" "World"
  ```
