# 이름, 생일, 데이터를 클래스에 담아서 출력한다.
# List로 부터 상속받은 클래스를 만든다.

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
class AthleteList ( list ):
    def __init__ ( self, name, dob=None, times=[] ) :
        list.__init__([])        
        self.name = name
        self.dob = dob
        self.extend( times )

    def top3 ( self ) :
        return sorted(set([sanitize(t) for t in self]))[0:3]    

#-------------------------------------------------------------------------------
def get_coach_data ( filename ):
    try:
        with open ( filename ) as f:
            data = f.readline()

        templ = data.strip().split( ',' )

        return ( AthleteList( templ.pop(0),
                              templ.pop(0),
                              templ ) )

    except IOError as ioerr:
        print ( 'File error: ' + str( ioerr ) )

        return ( None )

#-------------------------------------------------------------------------------

james = get_coach_data ( 'data\james2.txt' )
julie = get_coach_data ( 'data\julie2.txt' )
mikey = get_coach_data ( 'data\mikey2.txt' )
sarah = get_coach_data ( 'data\sarah2.txt' )

print( james.name + "'s fastest times are: " + str( james.top3() ) )
print( julie.name + "'s fastest times are: " + str( julie.top3() ) )
print( mikey.name + "'s fastest times are: " + str( mikey.top3() ) )
print( sarah.name + "'s fastest times are: " + str( sarah.top3() ) )

james.append( '1-1' )
james.extend( ['1.2', '1:3'] )
julie.append( '1-1' )
julie.extend( ['1.2', '1:3'] )
mikey.append( '1-1' )
mikey.extend( ['1.2', '1:3'] )
sarah.append( '1-1' )
sarah.extend( ['1.2', '1:3'] )

print( '===== Affter Add =====' )
print( james.name + "'s fastest times are: " + str( james.top3() ) )
print( julie.name + "'s fastest times are: " + str( julie.top3() ) )
print( mikey.name + "'s fastest times are: " + str( mikey.top3() ) )
print( sarah.name + "'s fastest times are: " + str( sarah.top3() ) )
