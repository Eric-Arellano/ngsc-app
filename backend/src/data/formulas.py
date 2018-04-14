# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def count_if(criterion: str, range_: str) -> str:
    return f'COUNTIF({range_}, "{criterion}")'


def roster_participation_count_if(criterion: str) -> str:
    return count_if(criterion, 'I$AA$')  # `$` replaced with row index


# ---------------------------------------------------------
# Formulas
# ---------------------------------------------------------

rosters = {
    'participation': f'''=TO_PERCENT(IFERROR(
           ({roster_participation_count_if("yes")} + {roster_participation_count_if("remote")} + {roster_participation_count_if("excused")}) / 
           ({roster_participation_count_if("yes")} + {roster_participation_count_if("no")} + {roster_participation_count_if("remote")} + {roster_participation_count_if("excused")})
           , ""))'''

}

master = {

}
