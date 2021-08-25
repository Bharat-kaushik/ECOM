from django.contrib.sites.shortcuts import get_current_site


def get_image_url(request, image: str):
    current_site = get_current_site(request)
    domain = current_site.domain
    final_url = "http://" + domain + "/" + "media" + "/" + image
    return final_url
