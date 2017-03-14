class UrlUtil:

    def get_hostname(self, url):
        """
        Extracts and returns the hostname from the parameter URL
        """
        hostname = url
        end = hostname.find("/", len("http://"))
        if end != -1:
            hostname = hostname[:end]
        return hostname

    def normalise_url(self, url):
        """
        Returns a normalised version of the parameter URL
        """
        if url.startswith("https://"):
            url =  url.lstrip("https://")
        if not url.startswith("http://"):
            url = "http://" + url
        if not url.startswith("http://www."):
            url = "http://www." + url.lstrip("http://")
        if url.endswith("/"):
            url = url.rstrip("/")
        return url