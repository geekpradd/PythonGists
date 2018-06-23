## PythonGists: A Python Module to create and access GitHub Gists

PythonGists is a Python 2/3 module to create, view and access data from GitHub Gists. It uses requests and oauth to function and is based on the GitHub v3 API.

### Why PythonGists?

There are numerous Python modules available for the GitHub v3 API but PythonGists is different. For starters, it is aimed only at the Gists part of the GitHub API and not the entire API. And it will never feature non Gists part of the GitHub API.

So you might be thinking that you could have used python3-github or any other module for Gists. Technically, you could but PythonGistss is more specific. In Systems where saving even a tiny amount of space matters (like your VPS), PythonGistss will take less space and do the same (provided you only want GitHub Gists Access).

### Note

This module is not to be confused with PyGist which is just a CLI. This is a python module (actually I would have picked up a different name if I knew about that module)

### Installation

Installation is done through PIP:

```
pip install PythonGists
```

### Usage

You can use PythonGists either by signing into GitHub or anonymously. Note that the syntax for logged in usage and anonymous usage is different. Here are some demos:

##### Create Gist Anonymously

```python
from PythonGists import PythonGists
link = PythonGists.Gist(description='a sample gist',content='Hey GitHub',name='demo.txt')

print("The link is {0}".format(link))
```

##### Create Gist as a logged in user

```python
from PythonGists import PythonGists
gistObject=PythonGists(username='youruser',password='somepass')
print(gistObject.createGist(description='a sample gist',content='Hey GitHub',name='demo.txt'))
'This will print the link'
```
##### Create Gist from File Anonymously

```python
from PythonGists import PythonGists
link = PythonGists.GistFromFile(description='a sample gist',file='demo.py')

print("The link is {0}".format(link))
```

##### Create Gist from File (logged in)

```python
from PythonGists import PythonGists
gistObject=PythonGists(username='youruser',password='somepass')
print(gistObject.createGistFromFile(description='a sample gist',file='demo.py'))
'This will print the link'
```
##### Get User Gists Links (same for both)

Here just replace GitHubGist in the print line with your gistObject for logged in users.

```python
from PythonGists import PythonGists
print(PythonGists.getGistsLinks('geekpradd'))
```

##### Get User Gists Data (same for both)

Here just replace GitHubGist in the print line with your gistObject for logged in users.

```python
from PythonGists import PythonGists
gistArray = PythonGists.getGistsData('geekpradd')
```

Note that gistArray will contain objects of the Gist Class which has access to the Gist data. Now, I'll show you how to access Gist data from the Gist Object.

##### Get Single Gist Data

```python
from PythonGists import Gist
gistObj = Gist('https://gist.github.com/geekpradd/a3e7a590887cf7bbf161')
print (gistObj.getFileContent()) #Will retutn a Dictionary with keys = File names and values = file content 
 ```
 
### About

This module is created by Pradipta (geekpradd) using the GitHub API and requests.
