from footer.models import Footer

def global_footer_data(request):
    footer = Footer.objects.last()
    return {'footer_data': footer}
