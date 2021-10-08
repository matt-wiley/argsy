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
        "next_version")
            version_text=$(bump2version --current-version "$(git describe --tags $(git rev-list --tags --max-count=1))" "${2}" --allow-dirty --dry-run --list)
            echo $(echo "${version_text}" | sed 's/new_version=//')
            ;;
        "build") 
            echo "${1}" > version.txt
            python setup.py bdist_wheel
            ;;
        "tag")
            echo "0.1.0" > version.txt
            bump2version --current-version "0.1.0" --new-version "${2}" --tag --allow-dirty --verbose minor 
            ;;
        "publish")
            twine upload dist/* -u "${2}" -p "${3}"
            ;;
        *);;
    esac
}
main "${@}"
