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
            find ./ -regex ".*/__pycache__" | grep -vE "^\./\.venv" | xargs rm -rf
            find ./ -regex ".*/\.pytest_cache" | grep -vE "\./\.venv" | xargs rm -rf
            pytest -rA
            ;;
        "build") 
            version_string="${2}"
            # The use of "minor" (or patch or major) is necessary in order for 
            # the version bump to occur, but since we are providing both the 
            # current and new versions the version_string overrides this argument.
            bump2version --current-version "0.0.0" --new-version "${version_string}" --allow-dirty minor setup.py 
            python setup.py bdist_wheel
            ;;
        "publish")
            twine upload dist/* -u "${2}" -p "${3}"
            ;;
        *);;
    esac
}
main "${@}"
