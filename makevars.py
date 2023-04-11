import felog.core as felog
import secproj.core as sp

sec = sp.Secure()
log = felog.log('MakeVars')

sec.set_var('PING_UUID','a69514d0-419b-43c8-8f37-8cf6cdcfa4f4')
log.info('Var Set.')