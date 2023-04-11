import felog.core as felog
import secproj.core as sp

sec = sp.Secure()
log = felog.log('ShowVars')
log.info(f"PING UUID: {sec.get_var('PING_UUID')}")