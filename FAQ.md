# CS Build Week 1 FAQ

## Contents

### Install

* [I'm getting a huge error/something about `ssl` when installing `psycopg2` with `pipenv install`](#q100)
* [`pipenv` command not found](#q300)
* [`pg_config` command not found](#q400)
* [I use OneDrive. And I'm getting `PermissionError: [Errno 13] Permission denied` when running the command `pipenv install django`](#q800)

### Backend

* [I'm getting a 404 when I try to register](#q200)
* [Do I need to add models to `api/models.py`?](#q500)
* [Error: `AnonymousUser` object has no attribute `player`](#q600)
* [Heroku: `Pipfile.lock` is out of date](#q700)

<!--

-->

## Answers

<a name="q100"></a>
### I'm getting a huge error/something about `ssl` when installing `psycopg2` with `pipenv install`

_**Mac only!** These instructions won't work for Windows!_

Buried at the bottom of this error message is something that looks like this:

```
build/temp.macosx-10.14-x86_64-3.7/psycopg/microprotocols_proto.o
build/temp.macosx-10.14-x86_64-3.7/psycopg/typecast.o -L/usr/local/lib -lpq -lssl -lcrypto -o
build/lib.macosx-10.14-x86_64-3.7/psycopg2/_psycopg.cpython-37m-darwin.so',
'    ld: library not found for -lssl',
'    clang: error: linker command failed with exit code 1 (use -v to see invocation)',
"    error: command 'clang' failed with exit status 1", '    ----------------------------------------'
```

If you don't have brew installed, [install it](https://brew.sh/).

Then:

```sh
brew install openssl
sudo cp $(brew --prefix openssl)/lib/libssl.1.0.0.dylib /usr/local/lib
sudo cp $(brew --prefix openssl)/lib/libcrypto.1.0.0.dylib /usr/local/lib
sudo ln -s /usr/local/lib/libssl.1.0.0.dylib /usr/local/lib/libssl.dylib
sudo ln -s /usr/local/lib/libcrypto.1.0.0.dylib /usr/local/lib/libcrypto.dylib
```

then try `pipenv install` again.

------------------------------------------------------------------------------

<a name="q200"></a>
### I'm getting a 404 when I try to register

The password needs to be at least 8 characters and include a number.

------------------------------------------------------------------------------

<a name="q300"></a>
### `pipenv` command not found

Install `pipenv` if not already installed.

On Windows, try a different shell, e.g. `cmd.exe` or PowerShell.

------------------------------------------------------------------------------

<a name="q400"></a>
### `pg_config` command not found

If you get this when running `pipenv install`, first do this:

```sh
export PATH="/Applications/Postgres.app/Contents/Versions/10/bin:$PATH"
```

then run `pipenv install` again. This should fix it going forward.

------------------------------------------------------------------------------

<a name="q500"></a>
### Do I need to add models to `api/models.py`?

It says

```python
# Create your models here.
```

but that's just boilerplate that Django made when the project was created. You
can ignore it.

All the models that matter are in `adventure/models.py`.

------------------------------------------------------------------------------

<a name="q600"></a>
### Error: `AnonymousUser` object has no attribute `player`

This means the server has failed to authenticate your request. Make sure the
token is in the request header in the form:

```http
Authorization: Token 0123456789ABCDEF01234567890
```

------------------------------------------------------------------------------

<a name="q700"></a>
### Heroku: `Pipfile.lock` is out of date

First run

```sh
pipenv lock
```

to regenerate the lockfile.

Then make sure `Pipfile.lock` is commited to git.

Then push to heroku.

------------------------------------------------------------------------------

<a name="q800"></a>
### * OneDrive user getting `PermissionError: [Errno 13] Permission denied` when running `pipenv install django`](#q800)

Creating your Django project within OneDrive causes problems.

Repeat setup & install steps in a new directory, _outside_ of OneDrive.

