
import json
import urllib2

def get_json(url, data_obj=None):
    try:
        url_final = "{0}".format(url)
        if data_obj:
            querystring = urllib.urlencode(data_obj)
            url_final = "{0}?{1}".format(url,querystring)

        get_headers={'Content-Type': 'application/json'}
        req = urllib2.Request(url_final, headers=get_headers)
        response = urllib2.urlopen(req)
        json_response = response.read()

        print(json_response)
        return json.loads(json_response)
    except urllib2.HTTPError as e:
        print(e)
        return None


if __name__ == '__main__':
    
    content = get_json('http://kde-metrics.s3-us-west-2.amazonaws.com/test/EC2ContainerService-circleci-demo-cluster.json')

    print(content)