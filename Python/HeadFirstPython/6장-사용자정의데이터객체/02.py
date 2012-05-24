# 이름, 생일, 데이터를 딕셔너리를 이용하고 함수형태로 만들어서 간단한 구조로 만든다.

#-------------------------------------------------------------------------------
def sanitize( time_string ):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return ( time_string )

    ( mins, secs ) = time_string.split( splitter )

    return ( mins + '.' + secs )

#-------------------------------------------------------------------------------
def get_coach_data ( filename ):
    try:
        with open ( filename ) as f:
            data = f.readline()

        templ = data.strip().split( ',' )

        return ({'Name':templ.pop(0),
                 'DOB':templ.pop(0),
                 'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})

    except IOError as ioerr:
        print ( 'File error: ' + str( ioerr ) )

        return ( None )

#-------------------------------------------------------------------------------

james = get_coach_data ( 'data\james2.txt' )
julie = get_coach_data ( 'data\julie2.txt' )
mikey = get_coach_data ( 'data\mikey2.txt' )
sarah = get_coach_data ( 'data\sarah2.txt' )

print( james['Name'] + "'s fastest times are: " + james['Times'] )
print( julie['Name'] + "'s fastest times are: " + julie['Times'] )
print( mikey['Name'] + "'s fastest times are: " + mikey['Times'] )
print( sarah['Name'] + "'s fastest times are: " + sarah['Times'] )
