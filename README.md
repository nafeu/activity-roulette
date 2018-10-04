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

### Credits

Nafeu Nasir

### License

MIT