# Golang

## Some Errors
- Cannot find the package: the `GOROOT` is set to what your `GOPATH` should be set to.
    - Unset the go root and set the `GOPATH`
        ```
        export GOPATH=$GOROOT
        unset GOROOT
        ```
- Vscode does not detect errors: adding the `GOROOT` to the `settings.json` of vscode
    -  `"go.goroot": "/usr/local/go"`
- Vscode does not import `Go` package
    - Update the go tools: `cmd` + `shift` + `p` and `update/install go tools`
    - Restart vscode
