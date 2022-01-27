#!/bin/bash
WD=$1
KEYWORD=$2

cd $WD/angeline-prabakar-keyword-usage-within-domain

source env/bin/activate
python3 -c "import searching.checking_database as check; import json; print(json.dumps(check.return_years_for_keyword('$KEYWORD')))"