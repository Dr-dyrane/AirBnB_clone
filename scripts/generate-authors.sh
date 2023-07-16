#!/usr/bin/env bash
#
###############################################################################
# Script name: generate-authors.sh
# Description: Script to generate the AUTHORS file for the project.
#              This script retrieves the author names and emails from the Git commit history
#              and generates the "AUTHORS" file in the root directory of the project.
#
# Usage: ./scripts/generate-authors.sh
###############################################################################

set -e

# Change to the root directory of the project
cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

# Header for the AUTHORS file
# Retrieve author names and emails from Git commit history, sort, and remove duplicates
{
    cat <<-'EOH'
		# This file lists all individuals having contributed content to the repository.
		# For how it is generated, see `scripts/generate-authors.sh`.
	EOH
    echo
    git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} >AUTHORS
