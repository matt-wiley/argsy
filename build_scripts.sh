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
        "build") 
            version_string="${2}"
            bump2version --current-version "0.1.0" --new-version "${version_string}" --allow-dirty minor setup.py
            python setup.py bdist_wheel
            ;;
        "publish")
            twine upload dist/* -u "${2}" -p "${3}"
            ;;
        *);;
    esac
}
main "${@}"
