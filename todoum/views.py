from django.shortcuts import render
from django.http import HttpResponse

from todoum.models import Region
from todoum.forms import PlayerForm


def player_registration(request, region_id):

    errors = ''
    try:
        # region = Region.objects.get(pk=1)
        region = Region.objects.get(pk=region_id)
    except Region.DoesNotExist:
        region = Region(pk=region_id)
        errors = 'Invalid region, cannot create player'
        # return HttpResponse("Region {} does not exist".format(region_id))

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        player = form.save(commit=False)
        player.region = region
        player.save()

        print(player)

    else:
        form = PlayerForm()

    context = {
        'form': form,
        'region': region,
        'errors': errors,
    }
    return render(request, 'pybox/player_registration.html', context)
