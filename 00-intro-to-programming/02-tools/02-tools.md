# Tools

* **Source Code** is the text that comprises a program. Some programming
  languages are "compiled" so there's a difference between the source code
  of the program and the `.exe` or application you run. For example, when you
  use Adobe Photoshop or Google Chrome you interact with the final product,
  the application itself, not the source code.
* **Text Editors** are programs that allow us to write and edit code. Text
  editors are not as complicated as popular word processors, like Microsoft
  Word. Text editors are designed to edit the contents of text, not format
  how text is displayed. A modern text editor will allow you to open multiple
  text files at a time, navigate directories, and provide special features
  like syntax-highlighting, code auto-completion, and many other custom
  extensions you can install.
* **Integrated Development Environments (IDEs)** are custom-tailored tool
  suites programmers use to program in specific languages or use to create
  specific applications. There are IDEs to create iPhone apps, Android apps,
  Mac apps, Windows apps, video games, and more. IDEs can be custom-tailored
  to help you program in specific programming languages, creating features
  that make sense for one language that wouldn't make sense, or be possible,
  for another language.
* **Terminals** provide an interface for programmers to enter commands to control
  their computer, like creating files, navigating directories and executing
  command-line applications (programs ran in the terminal).
* **Read Eval Print Loops (REPLs))** provide an interface for programmers to
  interact with proramming languages. We can use a REPL to type in small parts
  of a program to test ideas out without having to save our code to a file. A
  REPL is like an impermanent interactive sketch pad or sandbox for programming.
* **Version Control Systems**, like Git and Github, provides a way for programmers
  to collaborate with others and save their progress as they work. Git is perhaps
  the most popular version control system in use in 2020. Git is the underlying
  version control system. Websites like GitHub, GitLab, Bitbucket, and many
  more, are systems built on top of git allowing users to interact with a great
  online UI, notifications, and tools for things like viewing code diffs and
  performing code reviews.

## The Terminal

### When God Opens Windows He Closes a Door
Excuse the title here, I'm just having a bit of fun there.

If you're on a Mac or Unix-like operating system you'll find the terminal
easy to access.

If you're on Windows you'll have to jump through a few hoops to get a
Unix-like terminal running. The default Windows terminals (Command Prompt, or
Powershell) use commands built especially for Windows.

Since 2016 Windows started to integrate Unix-like functionality with Windows
Subsystem for Linux (WSL). This provides a well-integrated Unix-like
terminal on Windows. Although it is a fantastic tool there is still some
separation between using the WSL on Windows and using a terminal on a native
Unix-like machine.

"""
Bash can access windows files, Windows cannot copy files into the Linux Sub
System directory. (it can copy then, but Bash cannot see them as it preserves
the files permissions)
"""
[src](https://superuser.com/a/1084229)
