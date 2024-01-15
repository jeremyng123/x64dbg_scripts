from x64dbgpy.pluginsdk import *
import ctypes
import sys

"""
Took from telegram x64dbg group:

```python
import ctypes
from x64dbgpy.pluginsdk import x64dbg


MAX_SIZE = 256


eax = x64dbg.GetEAX()

module_text = ctypes.create_string_buffer(MAX_SIZE)
x64dbg.DbgGetModuleAt(eax, module_text)
print("module_text", module_text.value)


label_text = ctypes.create_string_buffer(MAX_SIZE)
x64dbg.DbgGetLabelAt(eax, x64dbg.SEG_DEFAULT, label_text)
print("label_text", label_text.value)
```
"""


def readchunkbytesfromIda(exportedbytes):
    addresses = []
    for addr in range(len(exportedbytes) // 8):
        addresses.append(exportedbytes[8 * addr + 6:8 * addr + 8] +
                         exportedbytes[8 * addr + 4:8 * addr + 6] +
                         exportedbytes[8 * addr + 2:8 * addr + 4] +
                         exportedbytes[8 * addr:8 * addr + 2])
    return addresses
   
def readchunkbytesfromIdaBE(exportedbytes):
    addresses = []
    for addr in range(len(exportedbytes) // 8):
        addresses.append(exportedbytes[8 * addr:8 * addr + 2] +
                         exportedbytes[8 * addr + 2:8 * addr + 4] +
                         exportedbytes[8 * addr + 4:8 * addr + 6] +
                         exportedbytes[8 * addr + 6:8 * addr + 8])
    return addresses

# Retrieve symbols
def retrievesymbols(addresses):
    MAX_SIZE = 256
    for addr in addresses:
        label_text = ctypes.create_string_buffer(MAX_SIZE)
        x64dbg.DbgGetLabelAt(int(addr,16), x64dbg.SEG_DEFAULT, label_text)
        print label_text.value
        

        # print "Address: {}, Symbol: {}".format(addr, _symbol)


if __name__ == "__main__":
    # Take the address using export bytes Shift E hotkey
    addresses = readchunkbytesfromIda("30239D77C0539C77802BB875E02EB7751062B6751031B775602FB775B016B6754031B775702FB775A02FB775502DB875E088B675C02FB775100FB7752041B775D0FB9B77D0F5B675F02EB775D0FE9C770041B775A031B7752032B7757032B775A032B775C01BB775A038B775A01BB775E00AB775701DB7759020B775C038B775E08AB675802EB775902EB775B0E7B675D032B7750033B775F01EB7756008B7757035B875C094B6754033B7755033B7753020B775D033B77510E0B675E089B6750009B775600AB775500EB77590E7B67550F5B67580F3B6757016B77520F3B6750017B775B010B7751019B77590F3B6759038B8752034B775C0C9B6755034B7753099B675F005B775C0FFB675E01DB775905D9D7760DFB67510279D77E04C037720B0047710C39E77D03BB875E006B77540E79C77D00BB77590F5B67510A9BA75B0AABA75B099B67580DFB6753006B77540DFB675E016B775C034B775D034B7755030B775D0249D77F0529C776030B7757027B7751006B7753035B775A0DFB675201FB77510CA0477000FB775F0570477A030B775C07CB6751099B6754011B775700FB77520DFB675B0DFB6759027A077D005B775C004B77570F5B675B030B775D030B775E030B77590A49F77B01BA077F0DFB6752088B6750088B6759039B775C035B775")
    retrievesymbols(addresses)
