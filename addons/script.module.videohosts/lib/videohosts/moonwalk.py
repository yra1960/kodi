# coding: utf-8
# Author: dandy

def get_key(content):
    key = ''
    value = '' 
    try:  
        script = content.split("setTimeout(function()")[-1].split("</script>")[0]    
        key = script.split("']['")[-1].split("'] = '")[0].replace("' + '", "")
        value = script.split("'] = '")[-1].split("';")[0].replace("' + '", "")
    except:
        pass 
    return key, value


def get_access_attrs(content):
    values = {}
    attrs = {}

    attrs['purl'] = '/manifests' + content.split("'/manifests")[-1].split("';")[0]

    values['mw_key'] = content.split("var mw_key = '")[-1].split("';")[0] 
    values['video_token'] = content.split("video_token: '")[-1].split("',")[0] 
    values['mw_pid'] = content.split("mw_pid: ")[-1].split(",")[0] 
    values['p_domain_id'] = content.split("p_domain_id: ")[-1].split(",")[0] 
    values['content_type'] = content.split("content_type: '")[-1].split("',")[0],
    values['ad_attr'] = '0'

    key, value = get_key(content) 

    values[key] = value

    attrs['X-Access-Level'] = content.split("'X-Access-Level': '")[-1].split("'")[0]

    return values, attrs
