# shiny-garbanzo
Introducing SQLMAP into non-HTTP services.

```
usage: whois_proxy.py [-h] [--host HOST] [--port PORT] [--tool TOOL]
                      [--arguments [ARGUMENTS [ARGUMENTS ...]]]

Non-HTTP sqlmap proxy

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           IP to listen on
  --port PORT           Port to listen on
  --tool TOOL           Tool to use for non-HTTP communication
  --arguments [ARGUMENTS [ARGUMENTS ...]]
                        Arguments passed to interesting tool, use SQLMAP token
                        to pass SQLMAP's input
```

Big ups to (https://twitter.com/kolokokop)#kolokokop
