import urllib2

class HtmlRequester:

    def get_html(self, url):
        """
        Requests and returns the online HTML for the parameter URL
        """
        html = []
        try:
            for line in urllib2.urlopen(url):
                html.append(line.rstrip('\n'))
        except (urllib2.HTTPError, urllib2.URLError) as err:
            # When an error occurs, abandon trying to get the HTML for the parameter URL
            pass
        return html