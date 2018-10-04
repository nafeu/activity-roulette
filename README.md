# Activity Roulette

A simple interactive console program for generating a task completion log

### Requirements

Python

### Installation

```
git clone https://github.com/nafeu/activity-roulette.git <PROJECT_DIR>
cd <PROJECT_DIR>
echo "<PROJECT_PATH>:" `pwd`
```

Make note of the path to your `<PROJECT_PATH>` and add the following aliases to your `.bashrc` or `.zshrc`:

```
alias argo="python <PROJECT_PATH>/main.py"
alias arlog="cat <PROJECT_PATH>/log.txt"
alias aredit="subl <PROJECT_PATH>/activities.txt"
```

* You can swap `subl` with the text editor of your choice.

### Usage

Run the `argo`, `arlog` and `aredit` alias commands in your shell.

`argo` runs the program

`arlog` displays your log

`aredit` opens the `activities.txt` file for you to edit

When editing the `activities.txt` file, follow this format:

```
Activity 1
Activity 2 (tagA, tagB, tagC)
Activity 3 (tagB)
```

With each activity on its own line and optional tags added in brackets as shown above.

When selecting your shortlist, you can type numbers or tags separated by `,`, for example:

```
...
Arrange Your Shortlist

    [0] Activity 1
    [1] Activity 2
    [2] Activity 3

> tagB

Are you okay with these activities? (y/n)

    Activity 2
    Activity 3
...
```

### Credits

Nafeu Nasir

### License

MIT