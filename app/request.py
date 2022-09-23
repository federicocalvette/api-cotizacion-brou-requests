import requests
import user_agent_fake


def request_brou():
    response = ''
    url = "https://www.brou.com.uy/c/portal/render_portlet?p_l_id=20593&p_p_id=cotizacionfull_WAR_broutmfportlet_INSTANCE_otHfewh1klyS&p_p_lifecycle=0&p_t_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=0&p_p_col_count=2&p_p_isolated=1&currentURL=%2Fcotizaciones"


    user_agent_fk = user_agent_fake.get_user_agent_fake()

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'sec-ch-ua': '"Chromium";v="94", " Not A;Brand";v="99", "Opera";v="80"',
        'Accept': 'text/html, */*',
        'Content-Type': 'text/plain;charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': user_agent_fk,
        'sec-ch-ua-platform': '"Linux"',
        'Origin': 'https://www.brou.com.uy',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.brou.com.uy/cotizaciones',
        'Accept-Language': 'es,en-US;q=0.9,en;q=0.8',
        'Cookie': 'JSESSIONID=ycXPSMyApfyvvZGyuc48hJ8i; _ga=GA1.3.1911481949.1663886062; _gid=GA1.3.914715236.1663886062; _gat=1; _gcl_au=1.1.1737547233.1663886063; LFR_SESSION_STATE_20159=1663886097665; JSESSIONID=BxNmYHwY1aXs-ak1nx34sijt'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        
    except:
        response = 'Error'

    return response

