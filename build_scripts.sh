#!/usr/bin/env bash

function main() {
    case "${1}" in
        "refresh")
            pip install -r requirements.txt -r requirements.dev.txt 
            ;;
        "clean") 
            rm -rf build dist *.egg-info
            find ./ -regex ".*/__pycache__" | grep -vE "^\./\.venv" | xargs rm -rf
            find ./ -regex ".*/\.pytest_cache" | grep -vE "\./\.venv" | xargs rm -rf
            ;;
        "test")
            pytest --cache-clear -rA
            ;;
        "build") 
            version_string="${2}"
            # The use of "minor" (or patch or major) is necessary in order for 
            # the version bump to occur, but since we are providing both the 
            # current and new versions the version_string overrides this argument.

            # !! NOTE: This will alter the setup.py file to have the new version string
            bump2version --current-version "0.0.0" --new-version "${version_string}" --allow-dirty minor setup.py 

            # Run the Python build
            python setup.py bdist_wheel

            # !! NOTE: This resets the setup.py version to 0.0.0 for the next build
            bump2version --current-version "${version_string}" --new-version "0.0.0" --allow-dirty minor setup.py 
            ;;
        "publish")
            twine upload dist/* -u "${2}" -p "${3}"
            ;;
        "get_install_requires")
                while IFS= read -r line; do
                    printf "\"%s\",\n" "$line"
                done < requirements.txt
                ;;
        *);;
    esac
}
main "${@}"
