import felog.core as felog
import secproj.core as sp
import healthcheckio.hc_ping as hc

sec = sp.Secure(gitignore_overwrite=True)
PING_UUID=sec.get_var("PING_UUID")
log = felog.log('Examples',debug=True)
ping = hc.ping(PING_UUID)
log.debug(f'PING SENT: {ping.ping_send()}')