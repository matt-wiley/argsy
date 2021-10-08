#!/usr/bin/env bash

function main() {
    case "${1}" in
        "pip")
            pip install -r requirements/runtime.txt -r requirements/dev.txt 
            ;;
        "clean") 
            rm -rf build dist *.egg-info
            ;;
        "test")
            pytest
            ;;
        "bumpversion")
            bump2version --current-version "$(cat version.txt)" "${1}" version.txt 
            ;;
        "build") 
            python setup.py bdist_wheel 
            ;;
        "publish")
            twine upload dist/* -u "${2}" -p "${3}"
            ;;
        *);;
    esac
}
main "${@}"
