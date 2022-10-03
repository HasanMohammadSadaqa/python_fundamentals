from django.db import models

class Shows(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

def show_all_shows():
    return Shows.objects.all()


def create_show(request):
    my_show = Shows.objects.create(
        title = request.POST['title'],
        network= request.POST['network'],
        release_date= request.POST['release_date'],
        desc= request.POST['desc']
    )
    return my_show

def delete(request, show_id):
    c = Shows.objects.get(id = show_id)
    c.delete()

def edit(request, show_id):
    return Shows.objects.get(id=show_id)

def update(request, show_id):
    the_show = Shows.objects.get(id=show_id)
    the_show.title=request.POST['title']
    the_show.network= request.POST['network']
    the_show.release_date= request.POST['release_date']
    the_show.desc= request.POST['desc']
    the_show.save()
    return the_show