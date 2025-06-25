from header.models import SiteSettings, cv

def global_header_data(request):
    try:
        logo_file = SiteSettings.objects.latest('id')
    except SiteSettings.DoesNotExist:
        logo_file = None

    try:
        cv_file = cv.objects.latest('id')
    except cv.DoesNotExist:
        cv_file = None

    return {
        'logo_file': logo_file,
        'cv_file': cv_file
    }
