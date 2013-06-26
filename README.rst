NoopHttp is a simple HTTP server that returns only empty strings.

This can be used together with an `ad-blocking hostfile <http://someonewhocares.org/hosts/zero/>`_ to replace
adds with an empty string (instead of a browser error).

Usage:

    noophttp -a ADDRES -p PORT

By default it binds to 0.0.0.0:80.
