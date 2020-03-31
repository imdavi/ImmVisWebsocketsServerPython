# ImmVis Websocket Server

This is the websocket version of ImmVis, a framework that aims to connect different data visualization platforms to a data analysis service written in Python.

## Architecture

WIP

## Development setup

To develop for the server side, you should have installed [Python](https://www.python.org/) (3.+) and [PIP](https://pypi.org/project/pip/) (latest version available). 

If you already have them installed, please install the Python dependencies listed at `requirements.txt` file using the command `python -m pip install -r requirements.txt`. If you are not sure how to do that, please run or take a look at the scripts `install_python_dependencies.bat` (Windows) and `install_python_dependencies.sh` (Linux) available on the `scripts` folder.

## Running the server

To run the server we recommend one of the following approaches:

- Visual Studio Code: open the root folder using Visual Studio Code and run the debug configuration `Run ImmVis Websocket Server`
- Command line / Terminal: from the root folder, run the command `python -m immvis.websocket`. Please note that we are still working to be able to close the server after running it using this method. Apparently Tornado server needs some workarounds to be "closeable" using Ctrl+C. If you don't know how to close the process on your operating system, please use Visual Studio Code for now.

## Adding new features

WIP

# License

```
MIT License

Copyright (c) 2020 Felipe Pedroso

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```