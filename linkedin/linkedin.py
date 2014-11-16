import requests

class AuthorizationURL:
    api_key = '75cyxzcm381ngd'
    scope = ''
    state = 'asdfasfdasdf'
    redirect_uri = 'http://localhost:8000/auth'
    url = 'https://www.linkedin.com/uas/oauth2/authorization?' + 'response_type=code&client_id=' + api_key + '&scope=' + scope + '&state=' + state + '&redirect_uri=' + redirect_uri
    
class AccessToken:
    def getCode(request):
        return request.GET['code']
    def sendCode(code):
        auth_code = code
        redirect_uri = 'http://localhost:8000/auth'
        api_key = '75cyxzcm381ngd'
        secret_key = 'wpwT0zy4i4BAhWsv'
        url = 'https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=' + auth_code + '&redirect_uri=' + redirect_uri + '&client_id=' + api_key + '&client_secret=' + secret_key
        res = requests.post(url)
        print(res.text)
