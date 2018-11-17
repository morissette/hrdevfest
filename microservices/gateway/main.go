package main

import "log"
import "net/http/httputil"
import "net/http"
import "net/url"
import "regexp"

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {

		uri := r.RequestURI

		// Pass request to post service
		post_matched, _ := regexp.MatchString("/v1/post.*", uri)
		if post_matched {
			proxy := reverseProxy("http://post-service/")
			proxy.ServeHTTP(w, r)
		}

		// Pass request to category service
		category_matched, _ := regexp.MatchString("/v1/category.*", uri)
		if category_matched {
			proxy := reverseProxy("http://category-service/")
			proxy.ServeHTTP(w, r)
		}

		// Pass request to tag service
		tag_matched, _ := regexp.MatchString("/v1/tag.*", uri)
		if tag_matched {
			proxy := reverseProxy("http://tag-service/")
			proxy.ServeHTTP(w, r)
		}

		log.Printf("%s %s %s%s", r.Header.Get("X-Forwarded-For"), r.Method, r.Host, r.RequestURI)
	})
	log.Fatal(http.ListenAndServe(":80", nil))
}

func reverseProxy(target string) *httputil.ReverseProxy {
	url, _ := url.Parse(target)
	return httputil.NewSingleHostReverseProxy(url)
}
