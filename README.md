# shiny-garbanzo
Introducing SQLMAP into non-HTTP services.

[https://haqpl.github.io/Introducing-sqlmap-into-non-HTTP-services](https://haqpl.github.io/Introducing-sqlmap-into-non-HTTP-services)

```
usage: shiny-garbanzo.py [-h] [--host HOST] [--port PORT] [--tool TOOL]
                         [--arguments [ARGUMENTS [ARGUMENTS ...]]]
                         [--verbose VERBOSE]

Non-HTTP sqlmap proxy

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           IP to listen on.
  --port PORT           Port to listen on.
  --tool TOOL           Tool to use for non-HTTP communication.
  --arguments [ARGUMENTS [ARGUMENTS ...]]
                        Arguments passed to target tool, use SQLMAP word to
                        place SQLMAP's input where it's needed.
  --verbose VERBOSE     Verbose mode.

```

Big ups to [https://twitter.com/kolokokop](#kolokokop)
