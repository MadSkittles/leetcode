class Solution:
    def validIPAddress(self, IP: str):
        IP = IP.lower()
        import re
        if '.' in IP:
            ip_parts = IP.split('.')
            if len(ip_parts) == 4:
                for ip_part in ip_parts:
                    if ip_part.startswith('0') and ip_part != '0':
                        return 'Neither'
                    if not (ip_part.isdigit() and 0 <= int(ip_part) <= 255):
                        return 'Neither'
                return 'IPv4'
            else:
                return 'Neither'
        elif ':' in IP:
            ip_parts = IP.split(':')
            if len(ip_parts) == 8:
                for ip_part in ip_parts:
                    if not re.match('^[0123456789abcdef]{1,4}$', ip_part):
                        return 'Neither'
                return 'IPv6'
            else:
                return 'Neither'
        else:
            return 'Neither'
