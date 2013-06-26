NoopHttp is a simple HTTP server that returns only empty strings.

This can be used together with an `ad-blocking hostfile <http://someonewhocares.org/hosts/zero/>`_ to replace
ads with an empty string (instead of a browser error).

Usage:

    noophttp -a ADDRESS -p PORT

By default it binds to 0.0.0.0:80.
